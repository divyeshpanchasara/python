my_file=open("file.txt","w")
if my_file:
    print("file opened\n")
    my_file.write("this is a new file\n it shall first write\n and then read i.e print the contents\n")
    my_file=open("file.txt","r")
    contents=my_file.read()
    print("\n",contents)
if my_file.close:
    print("the file is closed 1\n")
print("now this file is to be appende by a string\n\n")
my_file=open("file.txt","a+")
if my_file:
    print("appending...\n")
    my_file.write("this is the appended statement\n")
    my_file.seek(0)
    contents=my_file.read()
    print(contents)
if my_file.close:
    print("the file is closed 2\n")
    