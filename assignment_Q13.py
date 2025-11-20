n=int(input("Enter number of stones: "))
i=0
while i<=n:
    r=n-i
    s=r-2*i
    if r==1:
        print("Ramesh")
        break
    else:
        print("Suresh")
        break
