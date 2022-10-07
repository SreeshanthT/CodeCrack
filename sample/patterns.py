"""
Pattern 1
"""
n=4
for row in range(n*2):
    if row >= n:
        for col in range(row):
            print(" ",end="")
        for col in range(n*2 - row):
            print("*",end=" ")
        print()

    else:
        for col in range(n-row):
            print(" ",end="")
        for col in range(row + 1):
            print("*",end=" ")
        print()