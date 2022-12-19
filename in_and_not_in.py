my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
size=len(my_list)
for i in range(size):
    for i in range(size-1):
        if my_list[i] == my_list[i+1]:
            del my_list[i+1]
print("The list with unique elements only:")
print(my_list)
