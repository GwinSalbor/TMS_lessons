#




year=2100 # установить некоторый год
month=2 # установить некоторый месяц
#
# определение высокосного года
f_leap_year=True # в начале принять, что год высокосный
if year/400==0:
    print("год высокосный")
elif year/100==0:
    print("год невысокосный")
    f_leap_year=False
elif year/4==0:
    print("год высокосный")
else:
    print("год невысокосный")
    f_leap_year=False
print("---------------------")
#
# определение количества дней в месяце
print("Количество дней в месяце:")
nDays=31 # в начале количество дней равно 31
if (month==2)and(f_leap_year==True): nDays=29
elif (month==2)and(f_leap_year==False): nDays=28
elif (month==4)or(month==6)or(month==9)or(month==11):
    nDays=30
print(nDays)


a=10
c=0
if a>=10:
    c=100
else :
    c=200
print(c)