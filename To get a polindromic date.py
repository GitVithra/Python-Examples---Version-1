def palindromic_date(date):
	x,y,z = date.split('/')
	return(x+y)[::-1]==y and (y+x)[::-1]==y
print(palindromic_date("01/01/2022"))
		
