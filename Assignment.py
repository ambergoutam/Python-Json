import json
import os
import pathlib

class DataStore:
	def __init__(self, path=""):
		self.path = str(path) + "store.json"
		
	def create(self, dictionary):
		if not dictionary:
			print("Please give the corect value to insert")
			return -1
		dictVal = dict()
		key, value = str(dictionary[0]), str(dictionary[1])
		dictVal[key] = value
		with open(self.path, "a") as jf:
			json.dump(dictVal, jf)
		jf.close()
		return 1
	
	def read(self, key):
		with open(self.path, "a") as jf:
			data = json.load(jf)
		if key in data:
			print(data[key])
			return 1
		else:
			print("{} does not exists.".format(key))
			return -1

	def delete(self, key):
		with open(self.path, "a") as jf:
			data = json.load(jf)

		if key in data:
			del data[key]
		else:
			print("{} is not present in the json file.".format(key))
			return -1
		
		with open(self.path, "w") as jf:
			json.dump(data, jf)
		
		return 1

if __name__=="__main__":
	path = input("Enter the path(Optipnal):")
	if not path:
		path = pathlib.Path().absolute()
	os.path.exists(path)
	ds = DataStore(path)
	while True:
		print("1. Create/Insert value.")
		print("2. Read value.")
		print("3. Delete value.")
		print("4. Exit().")
		opt = int(input("Select the operation number: "))
		key = input("Enter the key: ")
		if opt==1: 
			value = input("Enter the value: ")
			dictionary = [key, value]
			val = ds.create(dictionary)
		elif opt==2:
			val = ds.read(key)
		elif opt==3:
			val = ds.delete(key)
		else:
			break
		print("Task Succesful..." if val==1 else "Task Unsuccessful.")