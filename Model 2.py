#Number pattern
'''n=int(input("Enter number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()'''


#Multiplication grid

'''n=int(input("Enter n:"))
for i in range(1,n+1):
    print("Table of {i}")
    for j in range(1,11):
        print(i,"X",j,"=",i*j)
    print()'''          


#Even-odd Matrix
'''n=int(input("Enter Number: "))
num=1
for i in range(n):
    for j in range(n):
        if num%2==0:
            print("E",end=" ")
        else:
            print("O",end=" ")
        num+=1
    print()'''


#prime Numbers in range

'''n=int(input("Enter number:"))
for i in range(2,n+1):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i,end=" ")'''


#student grade classificaation
'''marks=list(map(int,input("Enter marks: ").split()))
for m in marks:
    if m >= 75:
        print(m,"- Distinction")
    elif m >= 50:
        print(m,"- Pass")
    else:
        print(m,"- Fail")'''



#Matrix addition
n = int(input("Enter rows: "))
m = int(input("Enter columns: "))

print("Enter Matrix A:")
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter Matrix B:")
B = []
for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

# Addition
result = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Result Matrix:")
for row in result:
    print(row)







        








