"""
Simple function for quadratic equation.

"""

# MAIN FUNCTION
def quadratic_equation(a: float, 
                       b: float = None, 
                       c: float = None, 
                       real_only: bool = None,
                       round_to: int = None) -> tuple: 
    
    # documentation
    """
    Description
    -----------
        Function for quadratic equation
    
    Parameters
    ----------
        a (`float`): quadratic coefficient
        b (`float`): linear coefficient
        c (`float`): constant coefficient
        real_only (`bool`): returns real parts only if roots are complex numbers
        round_to (`int`): rounding values if you need to
    
    Result
    ------
        `tuple`: contains two roots of equation (x1, x2), `float` or `complex`
    
    """

    
    # if 'b' or 'c' values were forgotten, they are 0
    c = 0 if c is None else c
    
    if b is None:
        x1 = (-c / a)**0.5
        x2 = -x1
        
        return x1, x2
    
    # if 'a' equals to zero, the equation becomes linear
    if (a == 0) or (a is None):
        
        if (b == 0) or (b is None):
            x = c 
        else:
            x = -c / b
            
        return x, x


    # discriminant
    d = (b**2) - (4*a*c)
    
    if d == 0:
        x = -b / (2*a)
        return x, x
    
    
    # final result
    x1 = (-b + (d**0.5)) / (2*a)
    x2 = (-b - (d**0.5)) / (2*a)

    result = (x1, x2)
    
    
    # boolean variable - does result contain complex numbers?
    iscomplex = ((type(result[0]) == complex) and 
                 (type(result[1]) == complex))
    
    # rounding values
    if round_to is not None:
        if iscomplex:
            round_ = lambda x: complex(round(x.real, round_to), 
                                       round(x.imag, round_to))
            
            result = (round_(x1), round_(x2))
            
        else:
            result = (round(x1, round_to), round(x2, round_to))
    
    # return real part only
    if (iscomplex) and (real_only is not None):
        if round_to is not None:
            result = (round(x1.real, round_to), 
                      round(x2.real, round_to))
        else:
            result = (x1.real, x2.real)
    
    
    return result 


# ALIASES
qe = q_eq = quadeq = sqeq = square_eq = square_equation = quadratic_equation