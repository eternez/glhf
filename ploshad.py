def ploshad():
    import math
    x=int(input("x==?"))
    y=int(input("y==?"))
    z=int(input("z==?"))
    p=(x+y+z)/2
    S=math.sqrt(p*(p-x)*(p-y)*(p-z))
    print(S)
ploshad()
