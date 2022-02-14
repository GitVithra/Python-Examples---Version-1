def rev_srt(my_srt):
	length = len(my_srt)
	for i in range(length-1,-1,-1):
		yield my_srt[i]
for char in rev_srt("hello"):
	print(char)