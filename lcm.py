def find_lcm(a,b):
    if a>b:
        greater=a
    else:
        greater=b
    while(1):
        if greater%a==0 and greater%b==0:
            lcm=greater
            break
        greater+=1
    return lcm


a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
k=find_lcm(a,b)
print("LCM is ",k)