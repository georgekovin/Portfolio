def square_equation(a, b, c):
    
    x1 = float
    x2 = float
    
    d = (b**2) - (4*a*c)
    
    try:
        x1 = ((-1*b) + (d**(1/2))) / (2*a)
        x2 = ((-1*b) - (d**(1/2))) / (2*a)
    except ZeroDivisionError:
        return None 
    
    if d == 0:
        x1 = (-1*b) / (2*a)
        x2 = x1
    
    return x1, x2 


f = square_equation(0, 2, 3)

print(f)