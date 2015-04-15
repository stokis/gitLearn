# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 19:32:27 2015

@author: yd
"""

#x="i am yandong hahaha"
#for c in x.split(' '):
#    print (c,end='')

#
#x="i am yandong hahaha"
#for c in x.split(' '):
#    continue
#    print (c,end='')
#else:
#    print ('for end')

#x="i am yandong hahaha"
#for c in x.split(' '):
#   #continue
#    print (c,end='')
#else:
#    print (x)

#大小写变换
#a="khsaeuhaKJHSGIU"
#print (a.swapcase())
#
#取出全部数字组成数列
#a="k5sa67euha7982KJHS76GIU"
#print ([s for s in a if s.isdigit()])
#l=[]
#for s in a:
#    if s.isdigit():
#        l.append(s)
#print(l)
#        

#a="k5sa67euha7982KJHS76GIU"
#print([(x,a.count(x)) for x in a])
#print  (dict([(x,a.count(x)) for x in set(a)]))


#class test():
#    '''
#    get被称为是test对象的方法
#    '''
#    def _init_(self),var1):
#        pass
#    
#    def get(self):
#        return 'heihei'
#        
#    
#    
#    
#    pass
#def get():
#    return 'heihei'
#'''
#t是类test的一个实例
#'''
#t=test()
#'''
#如何使用对象内置的方法
#1.实例化这个class
#2.使用class.method()的方式去调用class内置的方法
#'''
#
#print (t.get())
#print (get())


#def add(x,y,f):
#    return f(x)+f(y)
#print(add(-1,-6,abs))
#
#
#def stand(str):
#    return  str[0].upper()+str[1:].lower
#print (list(map(stand,['adam','LiSA','barT'])))

#hw='Hello World'
#c=76
#def pr(x):
#    print (x)
#if (__name__=='__main__'):
#    print ('learn0做为主程序运行')
#else:
#    print ('learn0被其他程序调用')


#class Hello:
#    '''hello class'''
#    def printHello():
#        '''print hello world'''
#        print('hello world!')
#print (Hello.__doc__)
#print (Hello.printHello.__doc__)

#import sys
#print('命令行参数如下')
#for i in sys.argv:
#    print (i)
#print ('\n Python 语言的路径为：',sys.path,'\n')


#print(dir())


#def multi(a=2,b=5):
#    return (a*b)
#print (apply(multi,(1,3)))

#def func(x):
#    if x.isupper():
#        return x
#print (list(filter(func,['name','boy','Yan','Stokis','Dong,'])))
#
#def func(x):
#    if x.islower():
#        return x
#print (list(filter(func,['name','boy','Yan','Stokis','Dong,'])))
#
#def func(x):
#    if x.istitle():
#        return x
#print (list(filter(func,['name','boy','Yan','Stokis','Dong,'])))

#def power1(x):
#    return x**x
#print (list(map(power1,range(1,6))))
#
#def power2(x,y):
#    return x**y
#print (list(map(power2,range(1,4),range(1,4))))
#
#print(list(range(1,7)))
#import fuctools
#
#
#def sum(x,y):
#    return x+y
#print (fuctools.reduce(sum,range(5,10)))
#print (fuctools.reduce(sum,range(5,10)))
#print (fuctools.reduce(sum,range(5,10)))


#if __name__=='__main__':
#    print ("做为主程序运行")
#else:
#    print ("初始化子包subpackage1")

#
#class Fruit:
#    price=0
#    
#    def __init__(self):
#        self.color='red'
##        country="China"
#
#if __name__=="__main__":
#    print(Fruit.price)
#    apple=Fruit()
#    print (apple.color)
#    Fruit.price=Fruit.price+15
#    print("apple's price:"+str(apple.price))
#
#banana=Fruit()
#print ("banana's price:"+str(banana.price))
#    

    
#class people:
#    def __init__(self,name,age,sex):
#        self.Name=name
#        self.Age=age
#        self.Sex=sex
#    def speak(self):
#        print('my name'+self.Name)
#    def __str__(self):
#        msg='my name is:'+self.Name+','+'my age is:'+self.Age+','+'my sex is:'+self.Sex
#        return msg
#yandong=people('yandong','24','man')
#print (yandong)

#class person:
#    def __init__(self,name):
#        self.name=name
#    def sayHi(self):
#        print('Hello,my name is',self.name)
#
#p=person('yandong')
#p.sayHi()

#class SchoolMember:
#    '''represents any school member'''
#    def __init__(self,name,age,sex):
#        self.name=name
#        self.age=age
#        self.sex=sex
#        print('initialized SchoolMenber：',self.name)
#    
#    def tell(self):
#        '''tell any tetails'''
#        print('Name:',self.name,',''Age:',self.age,',''Sex:',self.sex)
#        
#class Teacher(SchoolMember):
#    '''represent a teacher'''
#    def __init__(self,name,age,sex,salary):
#        SchoolMember.__init__(self,name,sex,age)
#        self.salary=salary
#        print('initialized Teacher:',self.name)
#        
#    def tell(self):
#        SchoolMember.tell(self)
#        print('Salary:',self.salary)
#
#class Student(SchoolMember):
#    '''represents a student'''
#    def __init__(self,name,age,sex,marks):
#        SchoolMember.__init__(self,name,age,sex)
#        self.marks=marks
#        print('initialized student:',self.name)
#    
#    def tell(self):
#        SchoolMember.tell(self)
#        print('Marks:',self.marks)
#        
#t=Teacher('yandong',24,'man',10000)
#s=Student('xiaoxian',24,'women',99)
#        
#members=[t,s]
#for member in members:
#    member.tell()




#import math
#import random
#
#lenthOfSide=50
#radius=5
#pi=3.14
#volumeFraction=0
#coordinates_x=[]
#coordinates_y=[]
#coordinates_z=[] 
#numOfBalls=70
#i=1        
#while i<=numOfBalls:
#        a=random.uniform(radius,lenthOfSide-radius)
#        b=random.uniform(radius,lenthOfSide-radius)
#        c=random.uniform(radius,lenthOfSide-radius)
#        if i!=1:
#           k=1
#           while k<i:
#            if math.sqrt((coordinates_x[k-1]-a)**2+(coordinates_y[k-1]-b)**2+(coordinates_z[k-1]-c)**2)>(2*radius):
#                   k=k+1
#            else :
#                k=i+1
#           if k==i:
#            coordinates_x.append(a)
#            coordinates_y.append(b)
#            coordinates_z.append(c)
#            volumeFraction=i*4*pi*radius**3/(3*lenthOfSide**3)
#            i=i+1
#                
#        else:
#            coordinates_x.append(a)
#            coordinates_y.append(b)
#            coordinates_z.append(c)
#             
#            i=i+1
#print ((coordinates_x,coordinates_y,coordinates_z),len(coordinates_x),volumeFraction,i)





##learn class

#class Student(object):
#    
#    def __init__(self,name,score):
#        self.name=name
#        self.score=score
#        
#    def print_score(self):
#        print(self.name,self.score)
#
#    def get_grade(self):
#        if self.score>=90:
#           print ('a')
#        elif self.score>=60:
#            print ('b')
#        else:
#            print ('c')
#              
#      
#yan=Student('dong',90)
#
#yan.print_score()
#yan.get_grade()


#class Animal(object):
#    def run(self):
#        print('Animal is running')
#        
#class Dog(Animal):
#    def run(self):
#        print('Dog is running')
#    pass
#class Cat(Animal):
#     def run(self):
#        print('Cat is running')
#     pass
#dog=Dog()
#dog.run()
#cat=Cat()
#cat.run()







































