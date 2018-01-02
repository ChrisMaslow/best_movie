from bs4 import BeautifulSoup
import expanddouban
import csv

# 任务1
"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
	url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,{},{}".format(category, location)
	return url

# 任务3
class Movie:
	def __init__(self, name, rate, location, category, info_link, cover_link):
		self.name = name
		self.rate = rate
		self.location = location
		self.category = category
		self.info_link = info_link
		self.cover_link =cover_link

# 任务4
"""
return a list of Movie objects with the given category and location.
"""
def getMovies(category, location):
	movies = []
	for loc in location:
		html = expanddouban.getHtml(getMovieUrl(category, loc),True)
		soup = BeautifulSoup(html,'html.parser')
		a_tags = soup.find(class_='list-wp').find_all('a', recursive=False)
		for a_tag in a_tags:
			m_name = a_tag.find(class_='title').string
			m_rate = a_tag.find(class_='rate').string
			m_location = loc
			m_category = category
			m_info_link = a_tag.get('href')
			m_cover_link = a_tag.find('img').get('src')
			movies.append([m_name, m_rate, m_location, m_category, m_info_link, m_cover_link])
	return movies

category= '剧情'
location_list = ['瑞典']
movies_csv = getMovies(category,location_list)
print(movies_csv)
'''
with open('movies.csv', 'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(movies_csv)
'''
with open('movies.csv', 'w', newline='') as f:
    csvwriter = csv.writer(f)
    for row in movies_csv:
        csvwriter.writerow(row)
