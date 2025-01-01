#Integer's Type consists of Integer values

p=5 
q=10
s=15

#Boolian Type consists True and Flase only

5>3
3>5
2<1
1<2

#Complex Type consists of two parts:the real part and the imaginary part

c=2+4j

#String Type consists of words

name="hello"
place='chennai'

#Typle Type In Python Data Types, tuples are created by placing a sequence of values separated by a ‘comma’  with or without the use of parentheses for grouping the data sequence.

t=()
t1 = (1,2,3,4,5,)
print(t1[1])
print(t1[-1])
print(t1[0])
t2 = ('Amit', 'sulma',2,13,1.2,'a','b')
print("\nTuple with the use of String: ", t2)

#List Type In python data types , It's like Typle type where ti is imutable

l=[]
list=[1,2,3,4,5,]
print(list)
morelist=["hello",1,2,'world']
a = ["Pain", "For", "Good"]
print("Accessing element from the list")
print(a[0])
print(a[2])

print("Accessing element using negative indexing")
print(a[-1])
print(a[-3])

#Set Datatype will not duplicate the element

set=(1,2,3)
s1 = set("TimeisGold")
print("Set with the use of String: ", s1)
s2 = set(["Time", "Is", "Time"])
print("Set with the use of List: ", s2)

#Dictinory Type is unorder collection of values ,Dictionary contains  pair of element key: , value:

d={1:'a',2:'b',3:"hi",4:'7'}
newd={'a':1,'u':2,'h':4} 
print(d)
print(d.get(1))