n=int(input("No. of testcases: "))
for i in range (1,n+1):
    a=int(input("a= "))
    b=int(input("b= "))
    c1=0
    while a>0:
        r=a%10
        c1=c1*10+r
        a=a//10
    c2=0
    while b>0:
        r=b%10
        c2=c2*10+r
        b=b//10
    sum=c1+c2
    c3=0
    while sum>0:
        r=sum%10
        c3=c3*10+r
        sum=sum//10
    print("",c3)