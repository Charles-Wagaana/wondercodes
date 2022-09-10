# 1

my_array = [[1, 3, 5, 7], [2, 4, 6, 8]]

print(my_array[1][1])

# 2

new_array = [6, 7, 3, 4, 9, 1, 2, 8, 5]
new_array.sort()        #Ascending order
print(new_array)

new_array1 = [6, 7, 3, 4, 9, 1, 2, 8, 5]
new_array1.sort(reverse=True)       #Descending order
print(new_array1)

# 3

array1 = [[1, 3, 5, 7], [2, 4, 6, 8]]
_array = list()
for i in array1:
    for n in i:
        _array.append(n)
print(f"Minimum number is {min(_array)}\nMaximum number is {max(_array)}")
        

# 4

n_subjects = 5
total = 0

for m in range(1, n_subjects):
    marks_ = int(input("Enter marks: "))
    total += marks_   
    
    if (marks_//total)*100 < 50:
        print("Grade C")
    elif 50 < ((marks_//total)*100) < 80:
        print("Grade B")
    else:
        print("Grade A")

# 5

with open("file1.txt", 'w') as f:
    f.write("Name: John Doe\n")
    f.write("Mobile Number: 788-934-657\n")
    f.write("Roll Number: 45\n")
    f.write("Email ID: johndoe45@gmail.com")

with open('file1.txt', 'r') as f:
    for line in f.readlines():
        if '@' in line:
            print("Email ID: {}".format(line[10:]))

# 6

# def speed_check(speed):
#     limit = 70
#     point = None
#     if speed < limit:
#         print("Ok")
#     else:
#         if (speed - limit) == 5:
#             point = 



# 7

def show_stars(rows):
    for i in range(1,rows+1):
        print("*"*i)

show_stars(5)

# 8

for n in range(2000, 3200): 
    if n%7==0 and n%5!=0:
        print(n, end=',')

# 9

# 10

from math import sqrt
C = 50
H = 30
Q = None
x = [int(x) for x in input("Enter multiple value: ").split(",")]
for i in x:
    Q = sqrt((2*C*i)//H)
    print(Q, end=',')

# 11

div = None
try:
    div = 5/0
    print(div)
except ZeroDivisionError:
    print("Zero is not a divisor")

# 12

car = [['Black'], ['Honda']]

print("Color of car: {}".format(car[0][0]))
print("Brand of car: {}".format(car[1][0]))

# 13

def manual_sort(numbers):
    descend_sorted = list()
    for i in range(len(numbers)):
        largest = max(numbers)
        descend_sorted.append(numbers.pop(numbers.index(largest)))
    return descend_sorted

numbers = [1, 8, 9, 6, 2, 3, 1, 4, 5]
print(manual_sort(numbers))
