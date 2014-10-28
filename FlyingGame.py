import random
import time

item=['#############################################################']
#def TimeOut():
    #z = time.sleep(0.1)
    #print('Time Out You Lose')
    #return z

print('##############################################################')
time.sleep(2)
print('#              Welcome To Bird Flying Game                   #')
time.sleep(2)
print('#                    AKA Chidiya Udh                         #')
print('#                                                            #')
time.sleep(2)
print('#                                Programmer : Raghav Bisht   #')
time.sleep(2)
print('##############################################################')
print()
flyers = ['Snow partridge', 'Szecheny partridge', 'Tibetan snowcock',
        'Himalayan snowcock','Chukar partridge','air','koyel','witch','aeroplan','Black francolin',
         'helicopter','superman','petrel']
nonflyers = ['cat', 'dog','car','lady','batman','mario']
PScore=1
CScore=1
input('Press Enter To Start :')
print()
print(30*'*')
print()
#a = float(input('Set Level From 1-5 :'))
count = 0
while (count < 15):
    a=1
    b=2
    g=random.randint(1,2)
    if g==1:
        print()
        print('New Bird Fly :',random.choice(flyers))
        p='p'
        p=input('Enter P/q If its Flyer or nonflyer :')
    #TimeOut()
        if(p == 'p' and random.choice(flyers) in flyers):
            print('Player Score = ',PScore)
            PScore=PScore+1
        elif(p != 'p' and random.choice(flyers) in flyers):
            print('Wrong Option You Lose: ')
            print('Computer Score = ',CScore)
            CScore=CScore+1

    if g==2:
        print()
        print('New Bird Fly :',random.choice(nonflyers))
        q='q'
        q=input('Enter p/q If its Flyer or nonflyer :')
    #TimeOut()
        if(q == 'q' and random.choice(nonflyers) in nonflyers):
            print('Player Score = ',PScore)
            PScore=PScore+1
        elif(q != 'q' and random.choice(nonflyers) in nonflyers):
            print('Wrong Option You Lose: ')
            print('Computer Score = ',CScore)
            CScore=CScore+1
    count = count + 1
print('total Player Score is =',PScore)
print('total Computer Score is =',CScore)

