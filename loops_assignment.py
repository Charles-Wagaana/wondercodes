#1. First 10 natural numbers
n = 1
while n < 11:
    print(n)
    n = n + 1


#2. 
_sum = 0
count = 1
num = int(input("Enter a number: "))

while count <= num:
    _sum += count
    count += 1
print("The sum of ", num, " numbers is", _sum)

#3. Multiplication table

x = int(input("Enter a number: "))
counter = 0

while counter <= 11: # setting limit to be 12 numbers
    counter += 1
    print(x * counter)

#4.
numbers = [12, 75, 150, 180, 145, 525, 50]
for n in numbers:
    if n % 5 == 0:
        print(n)
        
    if n > 150:
        continue
        print(n)
    if n > 500:
        break
        print(n)
#5.
y = 4673453
counts = 1

while counts <= (len(str(y)) - 1):
    counts += 1
print("Number of digits in", y, "is", counts)

#6.
z = -10
while z <= -1:
    print(z)
    z = z + 1


