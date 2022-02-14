def length_and_index(para):
	print(len(para))
	for each in para:
		print(each,":",para.count(each))
length_and_index([1,3,4,5,6,7,3,7])