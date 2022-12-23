a = "abddefghi"

def replace(string:str,c:str,d:str)->str:
    return(string[:string.find(c)] + d + string[string.find(c)+1:])
    
print(replace(a,'d','c'))