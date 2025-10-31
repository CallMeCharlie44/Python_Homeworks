def is_year_leap(year):
    return year % 4 == 0

year = 2024

if year % 4 == 0:
    print ("год", year, ":", "True")
else:
    print (False)