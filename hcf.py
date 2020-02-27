def find_hcf(a,b):
    if a<b:
        smaller=a
    else:
        smaller=b
    for i in range(1,smaller+1):
        if a%i==0 and b%i==0:
            hcf=1
    return hcf

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
result=find_hcf(a,b)
print("HCF is: ",result)