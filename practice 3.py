num1=[]
for i in range(1,11):
    num1.append(i)
    print("number from 1 to 10...\n",num1)
for j,i in enumerate(num1):
    if(i%2==1):
        del num1[j]
print("the value after removed odd number...\n",num1)

