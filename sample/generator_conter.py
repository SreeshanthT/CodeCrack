N = 100000
def generador():
    global N
    while True:
        N += 1
        yield N
a= generador()    


while True:
    input("click enter")
    print(next(a))
    