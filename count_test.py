import csv

category_list = ['动作', '喜剧', '爱情']
location_list = ['美国', '香港', '日本']

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
