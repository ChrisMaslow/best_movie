import csv

category_list = ['动作', '喜剧', '爱情']
location_list = ['美国', '香港', '日本']

with open('movies.csv', 'r') as f:
	reader = csv.reader(f)
	movies_csv = list(reader)

cat_quantity = {}
for movie in movies_csv:
    if movie[3] in cat_quantity:
        cat_quantity[movie[3]] += 1
    else:
        cat_quantity[movie[3]] = 1

print(cat_quantity)
'''
dic_keys = list(cat_quantity.keys())
print(dic_keys)
print(type(dic_keys))
'''

movies_cats = []
movies_cat = []
i = 0
print(list(cat_quantity.keys())[2])
for i in range(len(cat_quantity)):
    for movie in movies_csv:
        if movie[3] == list(cat_quantity.keys())[i]:
            movies_cat.append(movie)
    movies_cats.append(movies_cat)

# print(movies_cats)
