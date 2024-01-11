num = int(input("Enter a number "))

print("Numbers Forward:")

def forward(num):
    for x in range (1, num+1):
        print(x, end = " ")
    return num

forward(num)

print()
print("Numbers Backward:")


def backward(n):
    for x in range (num, 1-1, -1):
        print(x, end = " ")
    return num
backward(num)
    
print()
print("Sum of Odd Numbers:")


sum = 0
for x in range (1, num+1, 2):
    sum = sum + x

print(sum)


print("Sum of Even Numbers:")

sum = 0
for x in range (0, num+1, 2):
    sum = sum + x
   
print(sum)
