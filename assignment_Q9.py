n=int(input("no. of testcases: "))
for k in range (1,n+1):
    c=int(input("No. of cakes :"))
    max=0
    for i in range(1,c+1):
        r=c%i
        if max<=r:
            max=r
            j=i
    print("max size of each box ",j)