import random

a=int(input("Enter a no."))
b=int(input("Enter a no."))
c=int(input("Enter a no."))
if a>=b and a>=c:
    print("A is Greater ")
elif b>=a and b>=c:
    print("B is Greater ")
else:
    print("C is Greater ")

a=int(input("Enter a no."))
b=int(input("Enter a no."))
match Calculator1:=int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\nEnter your choice:")):
    case 1:
        print("Addition is ",a+b)
    case 2:
        print("Subtraction is ",a-b)
    case 3: 
        print("Multiplication is ",a*b)
    case 4:
        print("Division is ",a/b)

# write a program to check students eligibility for scholarship or following conditions
# Students must have to score 75% marks
# Students must have a family income of less than 5 lakh per annum
# If both conditions are satisfied then only student is eligible for scholarship otherwise not eligible
# eligible
marks = float(input("Enter your percentage marks: "))
income = float(input("Enter your family income (in lakhs per annum): "))

if marks >= 75 and income < 5:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")
    if marks < 75:
        print("Reason: Marks less than 75%")
    if income >= 5:
        print("Reason: Family income is 5 lakh or more per annum")
def count_words(sentence):
    return len(sentence.split())

def count_characters(sentence):
    return len(sentence)

def reverse_sentence(sentence):
    return sentence[::-1]

def to_uppercase(sentence):
    return sentence.upper()

def to_lowercase(sentence):
    return sentence.lower()

def break_sentence(sentence):
    # Break sentence at each newline character
    return sentence.split('\n')

sentence = input("Enter a sentence (use \\n for new lines): ")
print("1. Count words")
print("2. Count characters")
print("3. Reverse sentence")
print("4. Convert to uppercase")
print("5. Convert to lowercase")
print("6. Break sentence at '\\n'")
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Number of words:", count_words(sentence))
    case 2:
        print("Number of characters:", count_characters(sentence))
    case 3:
        print("Reversed sentence:", reverse_sentence(sentence))
    case 4:
        print("Uppercase:", to_uppercase(sentence))
    case 5:
        print("Lowercase:", to_lowercase(sentence))
    case 6:
        print("Broken sentence:", break_sentence(sentence))
    case _:
        print("Invalid choice")

print("Helllo \nHiworld\nPython" \
"is a programming language")
print("Hello")
# Example of .find()
text = "Hello, welcome to the world of Python."
position = text.find("Python")
print("Position of 'Python':", position)

a=int (input("Enter a no."))
b=int(input("Enter a no."))
area=0.5*a*b
print("Area of triangle is ",area)

import random
print(f"Random number between 1 and 100: {random.randint(1, 100)}")

km=int(input("Enter distance in KM:"))
cf=0.621371
miles=km*cf
print("Distance in Miles is ",miles)

import calendar
yy=int(input("Enter year:"))
mm=int(input("Enter month:"))
print(calendar.month(yy,mm))

import math
#roots of ax^2+bx+c=0
a=int(input("Enter a no."))
b=int(input("Enter a no."))
c=int(input("Enter a no."))
d=b**2-4*a*c
if d>0:
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print("Roots are real and different")
    print("Roots are ",r1,r2)
elif d==0:
    r1=r2=-b/(2*a)
    print("Roots are real and same")
    print("Roots are ",r1,r2)
else:
    realpart=-b/(2*a)
    imagpart=math.sqrt(-d)/(2*a)
    print("Roots are complex and different")
    print("Roots are ",realpart,"+",imagpart,"i and ",realpart,"-",imagpart,"i")

a=1
b=11
print("Prime numbers between",a,"and",b,"are:")
for i in range(a,b):
    if i>1:
        for j in range (2,i):
            if(i%j==0):
                break
        else:
            print(i)

a=int(input("Enter a no."))
fact=1
for i in range(1,a+1):
    fact=fact*i
print("Factorial of ",a,"is",fact)

a=int(input("Enter a no."))
sum=0
for i in range(1,a+1):
    sum=sum+i
print("Sum is ",sum)
x=int(input("Enter limit"))
sum=0
for i in range(1,x+1):
        sum=sum+i
print("Sum is ",sum)

def find_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while True:
        if greater%x==0 and greater%y==0:
            lcm=greater
            break
        greater+=1
    return lcm
a=int(input("Enter a no."))
b=int(input("Enter a no.")) 
print("LCM of ",a,"and",b,"is",find_lcm(a,b))


def cube_sum(n):
    return sum(i**3 for i in range(1, n+1))
num = int(input("Enter a number: "))
result = cube_sum(num)
print(f"The sum of cubes from 1 to {num} is: {result}")

a=input("Enter a string")
c=0
for i in range (len(a)):
    if a[i].isspace():
        c=c+1
    else:
        print(f"count:{c}")

def Product_of_three_n():
    p=a*b*c
    return p

a=5
b=6
c=1

p=Product_of_three_n()
# print(p)
string = input("Enter a string: ")
print("Menu:")
print("1. Remove all leading and trailing spaces")
print("2. Count number of vowels")
print("3. Count the number of words")
choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    match choice:
        case 1:
            print("String after removing spaces:", string.strip())
        case 2:
            vowels = 'aeiouAEIOU'
            count = 0
            for char in string:
                if char in vowels:
                    count += 1
            print("Number of vowels:", count)
        case 3:
            print("Number of words:", len(string.split()))
        case _:
            print("Invalid choice")
elif choice == 2:
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    print("Number of vowels:", count)
elif choice == 3:
    print("Number of words:", len(string.split()))
else:
    print("Invalid choice")

for i in range(1, 101):
    total = 0
    for ch in i:
        total += int(ch)
    if total % 5 == 0:
        print(i)


s = input("Enter a string: ")
s = ' '.join(s.split())      # Remove extra spaces
s = s.lower()                # Convert to lowercase
s = s.replace(' ', '_')      # Replace spaces with underscore
print("Cleaned string:", s)

# Number of terms in the series
n = int(input("Enter the number of terms: "))

# First two terms
a, b = 0, 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("* " * i)


num =[1,2,3,4,5,6,7,8,9]
n=[1,2,4,5,6]
common_elements = set(num) & set(n)
print("Common elements:", common_elements)

l=[1,2,3,4,5,]
target=5
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==target:
            print(f"Pair found ({l[i]},{l[j]})")

total=0
price=[]
quantity=[]
items=[]
for i in range (5):
    items.append(input("enteritem"))
    price.append(float(input("enter price")))
    quantity.append(int(input("enter quantity")))
    total=total+price[i]*quantity[i]
print("\nSummary:")


l=[]
for _ in range(10):
    val=int(input("Enter the values:"))
    l.append(val)
print (l)

l=[x for x in l if x%3!=0]
print(l)

l.clear()
print(l)

l=[2, 3, 5, 7, 11, 13, 2, 3, 5]
x=l.count(2)
print(x)
Copy = l.copy()
print(Copy)
l.clear()
print(l)
print(Copy)
list1 = ['apple', 'banana', 'cherry'] 
list2 = ['orange', 'grape']
list1.extend(list2)
print(list1)
print(list1.index('grape'))
l=[10,20,30,40,50]
l.insert(2,25)
print(l)
x=l.pop()
print(x)
print(l)
import random

l=[]
for _ in range(5):
    l.append(random.randint(1,50))
print(l)
for num in l:
    print(f"Occurs at index {l.index(num)}")
print("Max:",max(l),"at position",l.index(max(l)))
print("Min:",min(l),"Deleting at position",l.index(min(l)))
l.remove(min(l))
print(l)
lst2=l.copy()
print("Copying to another list",lst2)
print(l)

l=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed=[[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
flat=[]
for row in transposed:
    flat.extend(row)
flat.sort(reverse=True)
print(flat)



lst = [9,1,8,2,7,3,6,4,5]
lst.sort()
lst.reverse()
x = lst.pop(4)
print("the element removed is",x )
lst.insert(0, x)
print(lst)
l=[]
for _ in range(5):
    name=(input("Enter the Names:"))
    l.append(name)
print (l)
l.sort()
l.append("John")
l.append("Alice")
print("After adding two names",l)
l.pop(2)
print("After removing 3rd index",l)
print ("Last name index",l.index(l[-1]))
l.clear()
list1 = ['abc', 123, 'ab12', '456', 'xyz', '78xy']
list1=[x for x in list1 if not (isinstance(x,str) and any(c.isdigit() for c in x)and any(c.isalpha() for c in x))]
print(list1)
list2 = ['10', 'apple', '20', 'banana', '30', 'grape']
list2=[x for x in list2 if not (x.isdigit())]
print(list2)
list3 = [10, 'text', 25.5, 30, 'hello', 45] 
list3=[x for x in list3 if not (isinstance(x,str))]
print(list3)
list4= [1, 2, 3, 4, 2, 5, 3, 6, 7, 1]
list4=list4.set()
print(list4)
for item in list4:
    print(f"Occurs at index {list4.index(item)}")

def find_sum(x,y=2):
    return x+y
print(find_sum(4,3))
def func(n):
    if n==0:
        return 0
    return n+func(n-2)
print(func(5))

choice=int(input("Enter a no. for you r choice:\n1.Check no. is prime or not\n2.Reverswe a no. using function\n3.Check if sum of divisors is greater than the no. or not"))
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
def reverse(n):
    rev=0
    while n>0:
        dig=n%10
        rev=rev*10+dig
        n=n//10
    return rev
def sum_of_divisors(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return sum
match choice:
    case 1:
        num=int(input("Enter a no."))
        if prime(num):
            print(f"{num} is prime")
        else:
            print(f"{num} is not prime")
    case 2:
        num=int(input("Enter a no."))
        print(f"Reverse of {num} is {reverse(num)}")
    case 3:
        num=int(input("Enter a no."))
        if sum_of_divisors(num)>num:
            print(f"Sum of divisors of {num} is greater than {num}")
        else:
            print(f"Sum of divisors of {num} is not greater than {num}")
    case _:
        print("Invalid choice")        
try:
    std=int(input("Enter no. of students:"))
    chocolates=100
    print("each student will get",chocolates//std,"chocolates")
except:
    print("Invalid input")
finally:
    print("Thank you")

no_of_years=int(input("Enter no. of years:"))
current_salary=int(input("Enter current salary:"))
if no_of_years>=10:
    new_salary=current_salary+current_salary*0.05
    print("New salary is",new_salary)
elif no_of_years>=5:
    new_salary=current_salary+current_salary*0.1
    print("New salary is",new_salary)
elif no_of_years>=2:
    new_salary=current_salary+current_salary*0.2
    print("New salary is",new_salary)
else:
    print("No bonus")
choice=int(input("Enter a no. for your choice\n1.convert into title\n2.Count 'the' in sentence\n3.Display last five characters\n4.Check for python\n5Check if starts with 'The'."))
def title_case(s):
    return s.title()
def count_the(s):
    return s.lower().split().count('the')
def last_five(s):
    return s[-5:]
def check_python(s):
    return 'python' in s.lower()
def starts_with_the(s):
    return s.lower().startswith('the')  
s=input("Enter a sentence:")
match choice:
    case 1:
        print("Title case:",title_case(s))
    case 2:
        print("Count of 'the':",count_the(s))
    case 3:
        print("Last five characters:",last_five(s))
    case 4:
        if check_python(s):
            print("The sentence contains the word 'python'.")
        else:
            print("The sentence does not contain the word 'python'.")
    case 5:
        if starts_with_the(s):
            print("The sentence starts with 'The'.")
        else:
            print("The sentence does not start with 'The'.")
    case _:
        print("Invalid choice")

list=['apple', 'dog', 'elephant', 'cat', 'giraffe']

list=[x for x in list if len(x)>3]

print(list)


l=['Python', 100, 'JavaScript', 3.14, 'Java', 42]
l=[x for x in l if not isinstance(x,(int,float))]
print (l)

list7 = [10, -5, 23, -42, 17, -8, 7]
list7=[x for x in list7 if x>=0]
print(list7)
l=['basketball', 'baseball', 'cricket', 'ball', 'football']
l=[x for x in l if not 'ball' in x ]
print(l)
list13 = [10, 20, 30, 40, 50, 60]
list13=[list13[i] for i in range (len(list13)) if i %2 !=0]
print(list13)

list=['a','b','c']
l=[1,2,3]
d={(list[i],l[j]) for i in range(len(list)) for j in range(len(l)) if i==j}
print(d)
list18= ['banana', 'apple', 'grape', 'cherry']
list18.sort(key=len,reverse=True)
print(list18)
list20 = ['python', 'java', 'c++', 'ruby']
for i in range(len(list20)):
    x=list20[i]
    list20[i]=x[-1::-1]
print(list20)
list21 = ['one two', 'three four', 'five six'] 
list21=[i for i in ' '.join(list21).split()]
print(list21)
list22 = ['apple', 'orange', 'banana']
vowels = 'aeiou'
list22=[([x for x in c if x not in vowels])for c in list22]
print(list22)

i=1
while i<=3:
    j=1
    while j<=3:
        k=1
        while k<=3:
            if i==j or j==k or k==i:
                k+=1
                continue
            else:
                print(i,j,k)
            k+=1
        j+=1
    i+=1




def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
for i in range(10):
    print (fibo(i),end=" ")

def sum(n):
    if n==0:
        return 0
    if (n%10)%2==0:
     print(n%10)
    return n%10+sum(n//10)
print(sum(1234))

items=[]
total=0
for _ in range(5):
    item=input("Enter item name:")
    price=float(input("Enter price:"))
    quantity=int(input("Enter quantity:"))
    items.append((item,price,quantity))
    total+=price*quantity

for item,price,quantity in items:
    print(f"{item}: Price={price}, Quantity={quantity}, Subtotal={price*quantity}")
print(f"Total bill amount: {total}")

if total>1000:
    discount=total*0.9
    print(f"Discount applied: {discount}")
    total-=discount
    print(f"Total amount after discount: {total}")

import random
target=random.randint(1,100)
gueses=0
while gueses<5:
    guess = random.randint(1,10)
    gueses+=1
    if guess==target:
        print(f"Congratulations! You've guessed the number {target} correctly in {guesses} attempts.")
        break
    elif guess<target:
        print(f"Attempt {gueses}: Your guess {guess} is too low.")
    else:
        print(f"Attempt {gueses}: Your guess {guess} is too high.")

n=int(input("Enter a no."))
for i in range(2,n):
    if n%i==0:
        print(f"{n} is not prime")
        break
else:
    print(f"{n} is prime")

n = int(input("Enter n: "))
div10 = len([x for x in range(1, n+1) if x % 10 == 0])
div15 = len([x for x in range(1, n+1) if x % 15 == 0])
both = len([x for x in range(1, n+1) if x % 10 == 0 and x % 15 == 0])
print("Div by 10:", div10, "Div by 15:", div15, "Both:", both)

salary=int(input("Enter salary:"))
for i in range(1,11):
    if i %3==0:
        salary*=2
print("Final salary is",salary)

def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
for i in range(10):
    print (fibo(i),end=" ")

class Shape:
    def area(self):
        print("Calculating area...")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
# Example of polymorphism
shapes = [Circle(5), Square(7), Circle(3)]

for shape in shapes:
    print(shape.area())  # Output: 78.53975, 49, 28.2743

class Hello:
    def __init__(self,greeting):
        self.greeting=greeting
    def greet(greeting):
        return "Hello, World!"
class Message(Hello):
    def __init__(self,greeting):
        super().__init__(greeting)
    def show_message(self):
        return self.greeting
msg=Message("Welcome to Python programming!")
print(msg.show_message())
import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("students.csv")

print("Dataset:")
print(df)

# Step 2: Calculate correlation matrix
corr_matrix = df[["Maths", "Physics", "Chemistry"]].corr()
print("\nCorrelation Matrix:")
print(corr_matrix)

# Step 3: Find the highest correlation pair
# Flatten the matrix and remove self-correlations
corr_unstacked = corr_matrix.unstack()
corr_unstacked = corr_unstacked[corr_unstacked < 1]  # remove diagonal (self = 1)

highest_pair = corr_unstacked.idxmax()
highest_value = corr_unstacked.max()

print(f"\nHighest correlation is between {highest_pair[0]} and {highest_pair[1]}: {highest_value:.3f}")

# Write a Python program to square and cube every number in a given list of integers using Lambda.
l=[1,2.3,2,66,5,8]
squared=list(map(lambda x:x**2,l))
cubed=list(map(lambda x:x**3,l))
print("Squared:",squared)
print("Cubed:",cubed)

import math
n=int(input("Enter a no."))
n_sum_of_even_digits=lambda n:sum(int(digit) for digit in str(n) if int(digit)%2==0)
n_product_of_odd_digits=lambda n:math.prod(int(digit) for digit in str(n) if int(digit)%2!=0)
dict_data = {"apple": 100, "banana": 200, "orange": 150}
x = input("Enter key to find: ")
if x in dict_data:
    print ("Key found:", x)
    dict_data.pop(x)
    print("Updated dictionary:", dict_data)
else:
    print("Key not found. Removing a random key.")
    print("Updated dictionary:", dict_data)

import re

def extract_digits(s):
    return re.findall(r"[a-zA-Z0-9]+@gmail\.com", s)

s = input("Enter a string: ")
digits = extract_digits(s)
print("Digits found:", digits)
import re

def extract_digits(s):
    return len(re.findall(r"\w+", s))

s = input("Enter a string: ")
digits = extract_digits(s)
print("Digits found:", digits)


class Employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    def display(self):
        print(f"Name:{self.name}, ID:{self.emp_id}, Salary:{self.salary}")

class Manager(Employee):
    def __init__(self,name,emp_id,salary,department):
        super().__init__(name,emp_id,salary)
        self.department=department
    def display(self):
        super().display()
        print(f"Department:{self.department}")
class Developer(Employee):
    def __init__(self,name,emp_id,salary,programming_language):
        super().__init__(name,emp_id,salary)
        self.programming_language=programming_language
    def display(self):
        super().display()
        print(f"Programming Language:{self.programming_language}")
mgr=Manager("Alice",101,75000,"IT")
dev=Developer("Bob",102,60000,"Python")
mgr.display()
dev.display()


import numpy as np
l=[1,2,3,4]
l2=[5,6,7,8]
l3=[9,10,11,12]
print(np.array([l,l2,l3]))
x=np.array([l,l2,l3])
print("Shape:",x.shape)
print("Size:",x.size)   
print("Dimension:",x.ndim)
import numpy as np
import random
# print(np.eye(3))
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[9,8,7],[6,5,4],[3,2,1]])
print("Addition:\n",a+b)
print(np.mod(a,b))


import re
# with open("MYPython.py", "r") as file:
#     content = file.read()
# matches=re.findall(r"def\s+(\w+)\s*\(.*?\):", "def is_prime(n):\n    if n<=1:\n        return False \n    for i in range (2,n):\n        if n%i==0:\n            return False\n    return True\n\ndef factorial(n):\n    if n==0 or n==1:\n        return 1\n    result=1\n    for i in range(2,n+1):\n        result*=i\n    return result\n \ndef convert_to_binary(n):\n    if n==0:\n        return \"0\"\n    binary=\"\"\n    while n>0:\n        binary=str(n%2)+binary\n        n=n//2\n    return binary")
# print("Functions found in math_utils.py:", matches)
# p = re.compile(r"\d+")
# print("Digits found in the string:", p.findall("123 and 456"))
text = "User123 scored 98 marks in Test_1."
words=re.findall(r"\w+", text)
numbers=re.findall(r"\d+", text)
print("Words found:", words)
print("Numbers found:", numbers)
class Father():
    def __init__(self):
        self.height = None
    
    def show_father_info(self, height):
        self.height = height
        print(f"Father's height is {self.height} cm")

class Mother():
    def __init__(self):
        self.weight = None
    
    def show_mother_info(self, weight):
        self.weight = weight
        print(f"Mother's weight is {self.weight} kg")

class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.age = None
    
    def show_child_info(self, age):
        self.age = age
        print(f"Child's age is {self.age} years")

child = Child()
child.show_father_info(180)
# child.show_mother_info(70)
# child.show_child_info(10)

import re
def extract_emails(text):
    pattern = r'\b[a-zA-Z0-9._%+-]+@gmail\.com\b'

    return re.findall(pattern, text)
sample_text = "Contact us at acb123@gmail.com 9654785432"
pattern2=r'\b[1-9][0-9]{9}\b'
x=re.findall(pattern2,sample_text)
emails = extract_emails(sample_text)
print("Extracted emails:", emails)
print("Extracted phone numbers:", x)


import numpy as np
import pandas as pd

# Create sample data
data = {
    'Income': [3200, 3400, 3100, 3300, 3250, 3500, 3600, 3400, 3700, 12000]
}
df = pd.DataFrame(data)

# Calculate quartiles
Q1 = df['Income'].quantile(0.25)
Q3 = df['Income'].quantile(0.75)
IQR = Q3 - Q1

# Calculate bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Detect outliers
df['Outlier'] = (df['Income'] < lower_bound) | (df['Income'] > upper_bound)

print("Detecting outliers using the IQR method:")
print(df)
