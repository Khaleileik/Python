'''
Created on Mar 7, 2020

@author: ITAUser
'''

import time

second = input('seconds:')

minute = input('minutes:')

seconds = int(second)

minutes = int(minute)

#next section of code creates constraints to number values

if(seconds < 0):
    print("plz type in value greater than or equal to 0")
    
elif(seconds > 60):
    print("plz type in value less than 60")
    
elif(minutes < 0):
    print("plz type in value greater than or equal to 0")
    
elif(minutes > 60):
    print("plz type in value less than 60")

else:
    print(minutes,':', seconds)

    timerOn = True

    while(timerOn == True):
        while(minutes > -1):
            while(seconds > 0):
                seconds = seconds - 1
                time.sleep(1) #time.sleep(1) delays stuff by one second
                print(minutes,':', seconds)
                  
            minutes = minutes - 1
            seconds = 60     
              
    print("thx for using my countdown timer (͡ ͡° ͜ つ ͡͡°) ")








