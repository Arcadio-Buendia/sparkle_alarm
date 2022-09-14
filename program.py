from datetime import datetime as dt
from datetime import timedelta

no_of_tests=int(input())
output=[]
#loop through the total number of tests specified by user. Take input for each test and process them
for i in range(0,no_of_tests): 
    #take first line of a test and get the no. of tasks as well as bed time
    while True:
        nHM=input().strip()
        try:
            n=int(nHM.split()[0])
            bed_time=dt.strptime(nHM.split(' ',1)[1],"%H %M")
        except:
            print("Please enter data in proper format")
            continue
        break

    #create a list of alarms as date-time objects from user input for a single test
    alarms=[]
    for case in range(0,n):
        while True:
            try:
                alarms.append(dt.strptime(input().strip(),"%H %M"))
            except:
                print("Please enter data in proper format")
                continue
            break




    #find the duration between bed time and the alarm closest to bed time
    sleep_time=timedelta.max.seconds
    for alarm in alarms:
        delta=(alarm-bed_time).seconds;
        sleep_time=delta if delta<sleep_time else sleep_time

    #convert duration in seconds to hour and minutes then store them.
    (minutes,seconds)=divmod(sleep_time,60)
    (hours,minutes)=divmod(minutes,60)
    output.append("{} {}".format(hours,minutes))

#show user the result in specified format
print("\n")
for sleep in output:
    print(sleep)
