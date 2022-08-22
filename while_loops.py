# finding the sum of the first 5 numbers
_sum = 0
counter = 1

n = int(input('Enter a number: '))  

while counter <= n:
    _sum = _sum + counter
    counter += 1
print(_sum)
