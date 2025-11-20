n=int(input("Enter number of rows:"))
nst=1
for i in range(1,n+1):
    for j in range(nst,i+1):
        if i==j  or j==1 and i<=n:
            j=1
            print(" ",j,end="")
        else:
            print(" ",i-1,end="")  
    print("")