n=int(input("Enter the no"))
if n==0 or n==1:
    print("factorial=1")
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print('factorial=',fact)    
