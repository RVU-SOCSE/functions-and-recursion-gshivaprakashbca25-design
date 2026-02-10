#NAME-G.SHIVAPRAKASH
#USN-1RUA25BCA0031
#FIBONACCI NUMBERS USING RECURSION

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter number of terms: "))
for i in range(num):
    print(fibonacci(i), end=" ") 
