beatles=[]# step 1
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul Mccarteny")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
for i in range(2):
    beatles.append(input())
print("Step 3:", beatles)

# step 4
del beatles[3]
del beatles[3]#as the size decrease this shpul also be indexed as 3
print("Step 4:", beatles)

# step 5
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))