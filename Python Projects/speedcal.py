from time import *
import random as r

def mistake(partest,usertest): 
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error = error + 1
        except:
                error = error + 1
    return error            

def speed_time(time_1,time_2,userinput):
    time_delay = time_2 - time_1 
    time_R = round(time_delay,2)
    speed = len(userinput)/ time_R
    return round(speed)
   


test = ['A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea ',
        'My name is Riya Thakare',
        'Welcome to the world of coding']
test1 = r.choice(test)
print('      ***** typing speed *****')
print(test1)
print()
print()
time_1 = time()
testinput = input(' Enter :')
time_2 = time()

print('Speed : ', speed_time(time_s,time_e,testinput),' w/sec')
print('Error : ', mistake(test1,testinput))