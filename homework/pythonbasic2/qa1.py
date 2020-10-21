# 1) Print the multiplication table from 2 to 5, each containing up to 5 times of each numbers.

for i in range(2, 6):
    for j in range(1,6):
        print(f"{i}x{j}={i*j}")
    print(".................")
