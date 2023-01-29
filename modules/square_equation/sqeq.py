def square_equation(a: float, 
                    b: float = None, 
                    c: float = None, 
                    round_to: int = None) -> tuple: 
    
    # documentation
    """
    Description
    -----------
        Function for quadratic equation.
    
    Parameters
    ----------
        a (float): quadratic coefficient
        b (float): linear coefficient
        c (float): constant coefficient
        round_to (bool): rounding values if you need to
    
    Result
    ------
        tuple: contains two values, float or complex
    
    """
    
    global result
    global x1
    global x2
    
    # if 'b' or 'c' values were forgotten, they are 0
    c = 0 if c is None else c
    
    if b is None:
        x1 = (-c / a)**(1/2)
        x2 = -((-c / a)**(1/2))
        result = (x1, x2)
        return result
    
    # if 'a' equals to zero, the equation becomes linear
    if (a == 0) or (a is None):
        x = -c / b
        result = (x, x)
        return result
    
    # discriminant
    d = (b**2) - (4*a*c)
    
    if d == 0:
        x = -b / (2*a)
        result = (x, x)
        return result
    
    # final result
    x1 = (-b + (d**(1/2))) / (2*a)
    x2 = (-b - (d**(1/2))) / (2*a)
    
    result = (x1, x2)
    
    # rounding values
    if round_to is not None:
        if (type(result[0]) == complex) and (type(result[1]) == complex):
            round_ = lambda x: complex(round(x.real, round_to), round(x.imag, round_to))
            result = (round_(x1), round_(x2))
            return result
            
        elif (type(result[0]) == float) and (type(result[1]) == float):
            result = (round(x1, round_to), round(x2, round_to))
            return result
    
    return result

