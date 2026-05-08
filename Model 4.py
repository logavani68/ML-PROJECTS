#welcome funtion
'''def welcome(name):
    print("welcome",name)
welcome("abii")'''   

#square funtion
'''def sqr(a,b):
    return(a**b)
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
print(sqr(a,b))'''


#area of circle
'''def area_circle(radius):
    area = 3.14 * radius * radius
    return area
rad = float(input("Enter radius: "))
result = area_circle(rad)
print("Area of Circle =", result)'''

#withdraw function
def withdraw(balance, amount):
    if amount % 100 != 0:
        print("Amount should be multiple of 100")
    elif amount > balance:
        print("Insufficient Balance")
    else:
        balance = balance - amount
        print("Withdrawal Successful")
        print("Remaining Balance =", balance)
balance = int(input("Enter balance: "))
amount = int(input("Enter withdrawal amount: "))
withdraw(balance, amount)




