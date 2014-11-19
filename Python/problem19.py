#You are given the following information, but you may prefer to do some research for yourself.
#
#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

weekday = 1
months = [31,28,31,30,31,30,31,31,30,31,30,31]
count = 0

for year in range(1900,2001):
    for month in range(0,12):
        if month == 1 and year % 4 == 0:
            if year % 100 == 0 and not year % 400 == 0:
                days = 28
            else:
                days = 29
        else:
            days = months[month]
        for day in range(0,days):
            weekday = weekday + 1
            if weekday > 7:
                weekday = 1
            if weekday == 7 and day == 0 and year > 1900:
                count = count + 1
    print([year,count])

print(count)
