hour, minute = map(int,input().split())

if minute >= 45:
    minute -= 45
else:
    remain  = 45 - minute 
    minute = 60 - remain

    if hour > 0:
        hour -= 1
    else:
        hour = 23
print(hour,minute)