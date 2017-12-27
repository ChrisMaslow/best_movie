import requests

# 任务1
"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location)
	url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags={},{}".format(category, location)
	return url

# 任务2
response = requests.get(url)
html = response.text
