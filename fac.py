#NAME-G.SHIVAPRAKASH
#USN-1RUA25BCA0031
#FACTORIAL USING FUNCTIONS

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))
    
