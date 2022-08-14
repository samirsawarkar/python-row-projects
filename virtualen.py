l =[4,5,10,12,20]

def no(n):
    if n % 5 == 0 :
        return True
    else:
        False    


oa = no
print(list(filter(oa,l)))