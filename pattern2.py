n = 9

for i in range(n):
    for j in range(n):

        if (j >= i and j <= n-i-1) or (j <= i and j >= n-i-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()



print("\n")

n = 5
for i in range(1, n + 1):

    # spaces
    for j in range(n - i):
        print(" ", end=" ")

    # stars / border
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()



for i in range(n - 1, 0, -1):

    # spaces
    for j in range(n - i):
        print(" ", end=" ")

    # stars / border
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()    



print("\n")

n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n // 2 or i == n - 1:
            print("*", end=" ")
        elif i < n // 2 and j == 0:
            print("*", end=" ")
        elif i > n // 2 and j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()    





print("\n")

n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# Decreasing part
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()



print("\n")

n = 5

# Upper half
for i in range(1, n + 1):

    # Spaces before stars
    for j in range(n - i):
        print(" ", end="")

    # Border
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")

    print()


# Lower half
for i in range(n - 1, 0, -1):

    # Spaces before stars
    for j in range(n - i):
        print(" ", end="")

    # Border
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")

    print()