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
'''
# 任务6
with open('movies.csv', 'r') as f:
	reader = csv.reader(f)
	movies_csv = list(reader)

movie_cat = [[], [], []]

sum = 0
quantity = []
percentage = []

with open('output.txt', 'w') as f:
	for movie in movies_csv:
		if movie[3] = category_list[0]:
			movie_cat[0].append(movie)
		elif movie[3] = category_list[1]:
			movie_cat[1].append(movie)
		else:
			movie_cat[2].append(movie)

	i = 0
	message = '{}电影数量排名前三的地区是{}、{}、{}，分别占此类别电影总数的百分比为{}、{}、{}。\n'
	for i in range(len(category_list)-1):
		movie_loc = {}
		j = 0
		for j in range(len(movie_cat[i]-1))
			if movie_cat[i][j][2] not in movie_loc:
				movie_loc[movie_cat[i][j][2]] = 1
			else:
				movie_loc[movie_cat[i][j][2]] += 1


		f.write(message.format(category_list[i], ))
'''
