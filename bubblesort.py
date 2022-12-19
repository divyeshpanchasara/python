lst=[]
size=int(input("enter the size of the list: "))
for i in range(size):
    lst.append(input())
print("my list: ",lst)
j=len(lst)
for k in range(j):
    for k in range(j-1):
        if lst[k]>lst[k+1]:
            lst[k],lst[k+1]=lst[k+1],lst[k]
print("after rearrangeing: ",lst)
