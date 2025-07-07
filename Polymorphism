class Complex:
    def __init__(self,imaginary,real):
        self.real=real
        self.imaginary=imaginary
        
    def shownumber(self):
        print(self.real,"i +",self.imaginary,"j")
    def __add__(self,num2):#Defining Methods of __add__ and __sub__ using polymorphism concept of dunder functon!
        newreal=self.real+num2.real
        newimg=self.imaginary+num2.imaginary
        return Complex(newreal,newimg)
    def __sub__(self,num2):
        newreal=self.real-num2.real
        newimg=self.imaginary-num2.imaginary
        return Complex(newreal,newimg)    
num1=Complex(2,1)
num1.shownumber()
num2=Complex(6,9)
num2.shownumber()
new_num=num1+num2
new_num.shownumber()
new_numb=num1-num2
new_numb.shownumber()
        
