day1= int(x[1])
day_of_week = calendar.weekday(year,month,day1 )
print(day_of_week)
day2 = '0'

if day_of_week==1 :
    day2 = 'Monday'
elif day_of_week==2 :
    day2 = 'Tuesday'
elif day_of_week == 3:
    day2 = 'Wednesday'
elif day_of_week==4 :
    day2 = 'Thursday'
elif day_of_week==5 :
    day2 = 'Friday'
elif day_of_week==6 :
    day2 = 'Saturday'

m2 = ''
if month == '01':
   m2 = 'January'
elif month == '02':
   m2 = 'February'
elif month == '03':
   m2 = 'March'
elif month == '03':
   m2 = 'March'
elif month == '04':
   m2 = 'April;'
elif month == '05':
   m2 = 'May'
elif month == '06':
   m2 = 'June'
elif month == '07':
   m2 = 'July'
elif month == '08':
   m2 = 'August'
elif month == '09':
   m2 = 'September'
elif month == '10':
   m2 = 'October'
elif month == '11':
   m2 = 'November'
elif month == '12':
   m2 = 'December'

print('the day on '+str(day_of_week)+'th of'+m2+','+str(year)+' is ' + day2)
#print(calendar.weekday(x[])x[0],x[1])