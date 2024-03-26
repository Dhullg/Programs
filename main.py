n=eval(input("enter"))
ip=True
i=2
while i<n and ip:
    if n%i==0:
        ip=False
    i+=1
print("i is",i)
if ip:
    print(n,"is prime")
else:
    print(n,"is not prime")
