mon={'jan':1,'feb':4,'mar':4,'apr':0,'may':2,'jun':5,'jul':0,'aug':3,'sept':6,'oct':1,'nov':4,'dec':6}
day=["Saturday",'Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday']

gc={}
for i in range(10,100):        
    gc[i]=0
    if(i%4==0):
        gc[i]+=6
    elif i%2==0:
        gc[i]+=2
    elif i%4==1:
        gc[i]+=4

date=int(input("enter date: "))
m=input("enter the month abrevation in lowercase: ")
yr=int(input("4 digits years only: "))

f2=yr//100
l2=yr%100

ny=yr

if (m=='jan' or m=='feb') and (yr%4==0 or yr%400==0):
    res=(date + (l2//4)) + mon[m] - 1

else:
    res=(date + (l2//4)) + mon[m]

while(ny//100 not in gc.keys()):
    ny-=400

f=res+gc[ny//100]+l2

if(yr==1000):
    print(day[f%7-1])
else:
    print(day[f%7])
