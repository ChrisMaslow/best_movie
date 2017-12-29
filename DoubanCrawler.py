import expanddouban

# 任务1
"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
	url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,{},{}".format(category, location)
	return url

# 任务2
html = expanddouban.getHtml(url)

# 任务3
class Movie:
	def __init__(self, name, rate, location, category, info_link, cover_link):
		self.name = name
		self.rate = rate
		self.location = location
		self.category = category
		self.info_link = info_link
		self.cover_link =cover_link

	def print_data(self):
		return "{},{},{},{},{},{}".format(self.name, self.rate, self.location, self.category, self.info_link, self.cover_link)
