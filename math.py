import matplotlib.pyplot as plt
import numpy as np

questions_bank =['when you go to sleep','what is your clg time ']
store = [25,25,25,25]

def con(val,value):
    if value == "pm" and val !="12"and 12  :
        values = int(val) + 12
    else :
        values = val   
    # print(f"values {values}")    
    return  values    


def time(value1,value2):
    num1 = value1.split()
    nu1 =con(num1[0],num1[1])
    print(nu1)
    num2 = value2.split()
    nu2 =con(num2[0],num2[1])
    if int(nu1) > int(nu2) and int(nu1) != 12:
        value =int(nu1) - int(nu2)
        oa = 24 - value
        # print('this')
    elif int(nu1) < int(nu2) and int(nu1) != 12:
        value =int(nu2) - int(nu1)
        oa =  value
    else:
        oa =int(nu1) - int(nu2)


  
    return oa

print(time("7 am","6 am"))

i = 2
while i < 2:
    print(questions_bank[i])
    user = input("From \n")
    userend =input("To \n")
    times = time(user,userend)
    store.append(times)
    i = i + 1
    
    
def week(num):
    newdata =[]
    for i in num:
        weekamount = i *7
        newdata.append(weekamount)
    return newdata    
    
def perweek (value):
    newdata =[]
    weeks =week(value)

    for i in weeks:
        weekper = (int(i)*100)/168
        final ="{:.2f}".format(weekper)
        newdata.append(final)
    return newdata

def total(value,values):
    newdata = []
    perweeks =perweek(value)
    new =100.00
    for i,e in zip(perweeks,values):  
        new = float(new) - float(i)
        newdata.append(f"you spend {i} for {e} ")
    return newdata,f"you have remaining {new}"
    
    


print(total(store,questions_bank))


# y = np.array(week(store))
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# plt.pie(y, labels = mylabels, startangle = 90)
# plt.show() 