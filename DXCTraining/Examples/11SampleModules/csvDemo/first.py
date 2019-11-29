import csv
reader = csv.reader(open('C:/Users/rkhanna36/Documents/Python/DXCTraining/Examples/11SampleModules/csvDemo/demo.csv','r'),delimiter=',')
for data in reader:
	print(data)
