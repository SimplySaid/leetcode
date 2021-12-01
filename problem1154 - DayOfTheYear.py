def dayOfYear(date):
    y, m, d = map(int,date.split('-'))
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    numdays = 0

    if (y%400==0) or (y%100 != 0 and y%4==0):
        month_days[1] = 29

    for i in range (0, m-1):
        print(numdays)
        numdays += month_days[i]
    
    return numdays + d
    
print(dayOfYear("1910-10-20"))