import datetime, time

date = datetime.datetime.now()
print(date)
date2 = datetime.datetime(2023, 5, 15)
print(date2)
date3 = date.strftime("%Y-%m-%d-%H:%M %p")
print(date3)
date4 = date.strftime("%Y-%m-%d-%I:%M %p")
print(date4)

dateList = []
for i in range(5):
    dateList.append(date.strftime("%Y-%m-%d-%I:%M:%S %p"))
    print(dateList[i])
    time.sleep(2)

#for i in dateList:
#    print(i)
