#bubble sort
import array 
size=int(input("Enter the size of array : "))
a=array.array("i")
print("Enter the values :")
for i in range(size):
    value=int(input())
    a.append(value)
for i in range(size):
    for j in range(size-i-1):
        if a[j]<=a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)
    