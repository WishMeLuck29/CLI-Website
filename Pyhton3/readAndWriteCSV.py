# i want make a py program
# that can read CSV file

# module

import csv


#functions definision

def readCSV ():

	found = False

	while (found == False):
		try:
			csv_name = input("Input your file name (with the extension) : ")
			with open(csv_name, newline='') as f:
			    reader = csv.reader(f)
			    for row in reader:
			        print(row)
	        
		except:
			print ("the file can\'t be found!")
			found = False

		else:
			found = True
			f.close()

def prSpecificRow ():


	csv_name = input("Input your file name (with the extension) : ")
	with open(csv_name, newline='') as f:
		reader = csv.reader(f)
		info = []
		i = 0
		for row in reader:
			info.append(row)
			i = i + 1
	
	i=0
	for row in info:
		if i == 2 :
			print (row)
		i = i + 1

	

#main program

readCSV()
