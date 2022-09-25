import random
while(True):
    temp=random.randint(10,100) 
    hum=random.randint(10,100) 
    if(temp>35 and hum<70): 
        print("Temperature : {0} and Humidity : {1}.".format(temp,hum),"Alarm is ON") 
    elif(temp<35 and hum>70): 
        print("Temperature : {0} and Humidity : {1}.".format(temp,hum),"Alarm is OFF")
        break
