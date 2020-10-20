
# Write a function called show_stars(rows). If rows is 5, it should print the following:



n = int(input("Enter a number: "))
for i in range(0,n):
    for j in range(i+1):
        print("*", end = "")
    print("\n")
