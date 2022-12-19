def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

def days_in_month(year, month):
    if is_year_leap(year)==True:
        if month==2:
            print("29")
        elif month==1 or 3 or 5 or 7 or 8 or 10 or 12:
            print("31")
        else:
            print("30")
    if is_year_leap(year)==False:
        if month==2:
            print("28")
        elif month==1 or 3 or 5 or 7 or 8 or 10 or 12:
            print("31")
        else:
            print("30")

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
