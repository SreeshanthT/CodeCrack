def sum_of_odd(n):
    if n>0:
        x=(n*2)-1
        print(x+sum_of_odd(n-1))
        return x+sum_of_odd(n-1)
    else:
        return 0

print(sum_of_odd(5))
