basic=int(input("enter your salary"))
if(basic<10000):
        hra=(67/100)*basic
        da=(73/100)*basic
elif(basic<20000):
        hra = (69/100) * basic
        da = (76 / 100) * basic
else:
        hra = (73 / 100) * basic
        da = (78 / 100) * basic
gross = hra + da + basic
print("gross_salary",gross)