def square_equation(a: float, 
                    b: float, 
                    c: float, 
                    round_to: int = None): 
    
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
    
    # if a equals to zero, the equation becomes linear
    if a == 0:
        x = -(c / b)
        result = (x, x)
        return result
    
    d = (b**2) - (4*a*c)
    
    if d == 0:
        x = -b / (2*a)
        result = (x, x)
        return result
    
    x1 = (-b + (d**(1/2))) / (2*a)
    x2 = (-b - (d**(1/2))) / (2*a)
    
    result = (x1, x2)
    
    
    if round_to is not None:
        if (type(result[0]) == complex) and (type(result[1]) == complex):
            round_ = lambda x: complex(round(x.real, round_to), round(x.imag, round_to))
            result = (round_(x1), round_(x2))
            return result
            
        elif (type(result[0]) == float) and (type(result[1]) == float):
            result = (round(x1, round_to), round(x2, round_to))
            return result
    
    return result

