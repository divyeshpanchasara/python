my_file=open("chk.txt","w")
if my_file:
    print("file opened\n")
    my_file.write("hello world\n")
    my_file=open("chk.txt","r+")
    content=my_file.read(10);
    print(type(content))
    print(content)
my_file.close()
if my_file:
    print("\nclosed\n")