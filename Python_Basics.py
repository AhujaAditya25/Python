'''
#TUPLES
a =1
b = 2
mytuple = (("first" , a) , ("Second",b))
print(mytuple)
mylist = ["Aditya is the greatest of all time","Here we are, Doing stuff that challenges us.",
          "Change lifes and dont be stressed","Look at the bright side"]
print(mylist)
for a in mylist:
    print(a)



x = int(input())
for a in range(1,x+1):
    print(a, end='')
    print()

for a in range(5):
    print("Hey ",end ='')
print()

#LIST
mynewList = []
a = int(input())
while(a>=0):
    mynewList.append(a)
    a = int(input())

print(mynewList)

# mytuple = ()
# print("Please Enter an Integer")
# a = int(input())
# while(a>=0):
#     mytuple = mytuple + (1,2,3)
#     a=int(input())
# 
# print(mytuple)








f = int(input())
if mynewList.__contains__(f):
    print("Yes the number is included in the list.")
else:print("Nope , no such content.")

aditya=[1,2,3,4,5,6]
aditya.sort(reverse=True)
print(aditya)

'''''
#DICTIONARY
''''
mydict= dict()
mydict = {'Phone':100000}
print('Enter Name')
name = str(input())
print('Enter Number')
number = int(input())
mydict[name] = number
print(mydict)

print('Enter name to be deleted')
x = str(input())
if mydict.__contains__(x):
    mydict.__delitem__(x)


print(mydict)
'''''
#SETS
# myset = {1,2,3,4,5,6,6,7}
# print(myset)
#

#OPERATORS#
''''
a = int(input("Please enter a number : "))
if a> 0:
    print("The value is positive")

else:
    print("The value is negative")
    
'''''

#LOOPS

#WHILE_LOOP
'''''
seconds=10
while(seconds>=0):
    print(seconds,end='->')
    seconds-=1
print('BlastOff')

'''''

array = ['Aditya','Binod','Chaitanya','Duggu']

# array.sort(reverse=True)
# for name in array:
#         print(name,end=" ")



# FOR WITH INDEX
'''''

a = len(array)
for i in range(a):
    print (i+1,array.__getitem__(i),end=' ')

'''''






