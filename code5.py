sec = int(input("number of seconds ?"))
if(sec<60):
    print(sec)
elif(sec>=60 & sec<3600):
   minutes = int((sec/60))
   seconds = (minutes+1)*60-sec
   print(minutes,".",seconds)
elif(sec>=3600 & sec<86400):
    hours = int((sec/3600))
    minutes = int((sec/60))
    minutes = hours*60-minutes
    seconds = minutes*60-sec
    print(hours,".",minutes,".",seconds)
elif(sec>=86400) :
    days = int((sec/8400))
    hours = int((sec/3600))
    hours = days*24-hours
    minutes = int((sec/60))
    minutes = hours*60-minutes
    seconds = minutes*60-sec
    print(days,".",hours,".",minutes,".",seconds)