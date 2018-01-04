import expanddouban
from bs4 import BeautifulSoup
import csv

# 任务1
"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
	url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,{},{}".format(category, location)
	return url

# 任务2
"""
已安装 selenium 和 chromedriver，成功调取expanddouban.getHtml()。
"""

# 任务3
class Movie:
	def __init__(self, name, rate, location, category, info_link, cover_link):
		self.name = name
		self.rate = rate
		self.location = location
		self.category = category
		self.info_link = info_link
		self.cover_link = cover_link

# 任务4
"""
return a list of Movie objects with the given category and location.
"""
def getMovies(category, location):
	movies = []
	for cat in category:
		for loc in location:
			html = expanddouban.getHtml(getMovieUrl(cat, loc),True)
			soup = BeautifulSoup(html,'html.parser')
			a_tags = soup.find(class_='list-wp').find_all('a', recursive=False)
			for a_tag in a_tags:
				m_name = a_tag.find(class_='title').string
				m_rate = a_tag.find(class_='rate').string
				m_location = loc
				m_category = cat
				m_info_link = a_tag.get('href')
				m_cover_link = a_tag.find('img').get('src')
				movies.append([m_name, m_rate, m_location, m_category, m_info_link, m_cover_link])
	return movies

# 任务5
category_list = ['动作', '喜剧', '爱情']
location_list = ['美国', '香港', '日本']
movies_list = getMovies(category_list,location_list)
with open('movies.csv', 'w') as f:
    writer = csv.writer(f)
    for row in movies_list:
        writer.writerow(row)

# 任务6
with open('movies.csv', 'r') as f:
	reader = csv.reader(f)
	movies_csv = list(reader)

message = '{}电影数量排名前三的地区是{}、{}、{}，分别占此类别电影总数的百分比为{}、{}、{}。\n'

# 计算单个地区电影数量与总量的百分比
def percentage(count, sum):
	pct = '%.2f%%' % (count / sum * 100)
	return pct

with open('output.txt', 'w') as f:
	for cat in category_list:
		temp = []
		sum = 0
		for loc in location_list:
			count = 0
			for movie in movies_csv:
				if movie[3] == cat and movie[2] == loc:
					count += 1
					sum += 1
			temp.append((loc, count))
			temp = sorted(temp, key=lambda x:x[1], reverse=True)

		pct = []
		for i in range(3):
		 	pct.append(percentage(temp[i][1], sum))

		print(message.format(cat, temp[0][0], temp[1][0], temp[2][0], pct[0], pct[1], pct[2]))
		f.write(message.format(cat, temp[0][0], temp[1][0], temp[2][0], pct[0], pct[1], pct[2]))
