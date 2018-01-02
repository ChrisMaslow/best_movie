import csv

movie1 = '肖申克的救赎,9.6,美国,剧情,https://movie.douban.com/subject/1292052/,https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p480747492.jpg'
movie2 = '霍伊特团队,9.0,香港,动作,https://movie.douban.com/subject/1307914/,https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2329853674.jpg'

movie1 = movie1.split(',')
movie2 = movie2.split(',')
rows = [movie1, movie2]


with open('movies.csv', 'w', newline='') as f:
    csvwriter = csv.writer(f)
    for row in rows:
        print(type(row))
        csvwriter.writerow(row)
