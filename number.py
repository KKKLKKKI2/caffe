import time
import random
# coding=Big5
a=0
while (4 != 3 or a != 4):
    a=input("hi")
    print(a)
    if (int(a) == 3 or int(a) == 4):
           break
    print("wrong")
tt=input()
for t in range(int(tt)):
    number = ''
    word = ''
    for i in range(int(a)) :
        c=random.randrange(65,91)
        w=chr(c)
        word=word+w
    for i in range(3) :
        c=random.randrange(48,58)
        w=chr(c)
        number=number+w
    print(word+"-"+number)

#print("go")
#

