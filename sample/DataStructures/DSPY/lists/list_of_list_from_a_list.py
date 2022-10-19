n = [1,2,3,4,5,6,7,8,9]
m=3

# list to list of list in order to elements in list of list
print([n[i:i+m] for i in range(0,len(n),m)])

# list of list to a single list  
print([j for i in [n[i:i+m] for i in range(0,len(n),m)] for j in i])