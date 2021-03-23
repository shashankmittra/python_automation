import os
import shutil
import datetime

# to find if any new file has been created in the directory

def findNewFile():
	
	arr = os.listdir('.')
	numberOfFiles = len(arr)
	informationList = []
	if numberOfFiles > 0:
		informationList.append(1)
		for i in arr:
			informationList.append(i)
		return informationList

# to remove the main.py and creating the final list of files for processing

def filterDirectory(namesOfFiles):
	
	if namesOfFiles[0] == 1:
		checkingTheIndex = 0
		finalList = []
		
		for i in namesOfFiles:
			if checkingTheIndex != 0 and i != 'main.py':
				finalList.append(i)
			checkingTheIndex = checkingTheIndex + 1
		movefiles(finalList)

# to cut paste files from one to another directory

def movefiles(filteredList):
	
	for i in filteredList:
		partitionningFile = i.partition('.')
		formatOfFile = partitionningFile[2]
		
		if formatOfFile == 'py':
			destination = '/home/shashank/shashank/practise/python/test/python/'
		
		if formatOfFile == 'txt':
			destination = '/home/shashank/shashank/practise/python/test/text/'
		
		source = f'/home/shashank/shashank/prg/python_automation/{i}'
		shutil.move(source, destination)
		renameFile(source, destination, i)

# to rename any particular file 

def renameFile(source, destination, fileName):
	newFileName = f'{datetime.date.today()}'
	count = fileCount(destination, fileName)
	
	if count < 10:
		finalCount = f'0{count}'
	else:
		finalCount = f'{count}'	
	
	newDestination = f'{destination}{newFileName}_{finalCount}_.txt'
	print(newDestination)
	os.rename(f'{destination}{fileName}', newDestination)	

# determine the file count for proper renaming

def fileCount(destination, fileName):
	fileNames = os.listdir(destination)
	count = 0
	print('length of FileNames - ', len(fileNames))
	if len(fileNames) == 1:
		count = 1
	else:
		for i in fileNames:
			arr = i.partition('_')
			print('arr - ', arr)
			middle = arr[2].partition('_')
			print('middle - ', middle)
			final = middle[0]
			print('final - ', final)
			initalCount = int(final)
			print(initalCount)
			count = max(initalCount,count)
	print(count, 'count')
	return count

newList = findNewFile()
filterDirectory(newList)