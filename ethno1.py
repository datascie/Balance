from bs4 import BeautifulSoup
import csv

attrs = set()
all_files = ['Angela_Q_2.txt', 'Anne_Q_2.txt', 'Gary_Q_2.txt', 'Jon_Q_3.txt']

# read the attributes and make a header row in csv
for file in all_files:

	file_object = open(file, 'r')

	soup = BeautifulSoup(file_object.read(), "lxml")

	for tag in soup.findAll('q'):
		#print(tag.attrs)
		
		for key in tag.attrs:
			#print(key)
			attrs.add(key)

print(attrs)
print('attributes compiled for') 
print(all_files)

csvfile=[]
header=['quote']

for attr in attrs:
	header.append(attr)
csvfile.append(header)

# read the quotes and decide if attributes are t or f
#print(csvfile)

for file in all_files:
	file_object = open(file,'r')

	soup = BeautifulSoup(file_object.read(), "lxml")

	for tag in soup.findAll('q'):
		#print(tag.attrs)

		#print(tag.contents[0])
		row=[tag.contents[0]]
		for attr in attrs:
			if tag.has_attr(attr):
				row.append('T')
			else:
				row.append('F')
		csvfile.append(row)
#print(csvfile)

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(csvfile)
