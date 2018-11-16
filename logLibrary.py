import csv

def dbRead(filename, rcolumn, rrow):
	print('db read initiated')
	with open(filename, 'r') as file:
		reader = csv.reader(file)
		column = []
		for row in reader:
			column.append(row)

		rvc = column[rrow][rcolumn]
		file.close()
		return(rvc)
	#not implemented
def dbWrite(filename, column, row):
	print('db edit initiated')
	#not implemented
def dbAppend(filename, c1, c2, c3):
	print("append triggered")
	with open(filename, 'a') as file:
		appender = csv.writer(file)
		#
		appender.writerow([c1, c2, c3, 0])
	file.close()
def dbCount(filename):
	print('db count initiated')
	with open(filename, 'r') as file:
		reader = csv.reader(file)
		trv = 0
		for row in reader:
			trv+=1
		file.close()
	return(trv)

#dbappend('inlog.csv', "sender", "date", "body")
