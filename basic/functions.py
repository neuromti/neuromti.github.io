'''
Created on Sep 13, 2017

@author: maximilianscherer
'''

"""
This module describes functions including the preferred naming conventions

Each function consists of an declaration and a definition.
The declaration consists of the function name, what "goes in" and what "comes out".
The definition is the body of the function, meaning what actually happens in the function.
In Python, declaration and definition are in the same spot. Each function follows this pattern

def functionName(Parameterlist):    <- Part of the declaration
    Body of the function            <- Part of the definition
    
    return something                <- Part of the declaration


def functionName(Parameterlist):    <- required
    Body of the function            <- required
    
    return something                <- optional, defaults to "None" if missing


Each function should be named and documented in a way that it can be considered a black box.
One knows what goes in and knows what comes out, but "how" this is actually done does not matter.
Any function that does not match this idea is either insufficiently named, commented or both.

"""

def emptyFunction():
    """
    This function does nothing
    
    Functions always start with a small letter. Function names should be matching one of the two following patterns:
       - CamelCase            -> emptyFunction
       - Underscore separated -> empty_function
    Regardless whether pattern you choose, be consistent in your code!
    
    This is an empty function 
    """
    print("This is the function body")
    
#Not part of auto-completion    
def returnFunction():
    """
    Part of auto-completion    
    
    This is an empty function
    @return: None
    """
    
    return None                 # return type can be anything, None, a variable/object

    #This code is never executed! The reason is that after the first return, the function is exited, therefore the code afterwards is ignored.

    return (None, None, None)   # return type can also be a tuple, ...
    
    
def paramFunction(param1, param2, param3, param4):
    """
    This function displays how to use multiple parameters
    
    @param:    param1    This is a dummy parameter
    @param:    param2    This is a dummy parameter
    @param:    param3    This is a dummy parameter
    @param:    param4    This is a dummy parameter    
    @return:             This function returns the first parameter
    """
    
    print(param1)
    print(param2)
    print(param3)
    print(param4)
    
    return param1   # Returns param1, whatever it is
        
def defaultValueFunction(param1 = True, param2 = 2, param3 = "Text", param4 = emptyFunction):
    """
    This function displays how to use default parameters.
    Default parameters can be anything, boolean, integer, strings or even functions.
    
    @param:    param1    This is a dummy parameter
    @param:    param2    This is a dummy parameter
    @param:    param3    This is a dummy parameter
    @param:    param4    This is a dummy parameter    
    @return:             This function returns the first parameter
    """

    print(param1)
    print(param2)
    print(param3)
    print(param4)
    
    return param1   # Returns param1, whatever it is

    
def add(summand1, summand2):
    """
    The first real function calculating the sum of two variables
    
    @param:    summand1    This is the first summand
    @param:    summand2    This is the second summand
    @return:               First parameter
    """
    
    return summand1 + summand2

def sub(minuend, subtrahend = 5):
    """
    This function calculates the sum of minuend - subtrahend
    The default value of the subtrahend is 5
    In case the function is called with a single argument, sub(x), the result is x - 5
    whereas if the function is called with two arguments, sub(x, y), the result is x - y
    
    @param:    minuend        first part of the equation
    @param:    subtrahend     second part of the equation
    @return:                  minuend - subtrahend 
    
    """
    
    return minuend - subtrahend

def complexCalculation(a, b = 5, c = 2, d = 10, e = -7, f = 3, g = 99):
    """
    This function demonstrates advanced use of a multiple of input arguments. This can easily be the case when
    calculating any numerical solution. 
    When calling the function with "complexCalculation(10, 11, d = 55, g=32)", the parameters are assigned as follows:
    a = 10, b = 11, c = 2, d = 55, e = -7, f = 3, g = 32
    
    @param:    a    This is a dummy parameter
    @param:    b    This is a dummy parameter
    @param:    c    This is a dummy parameter
    @param:    d    This is a dummy parameter   
    @param:    e    This is a dummy parameter   
    @param:    f    This is a dummy parameter   
    @param:    g    This is a dummy parameter    
    @return:        Sum of all parameters
    """
    
    #This function returns the sum of all parameters 
    return a + b + c + d + e + f + g

def mathOperation(x, y, f = add):
    """
    This function takes two input parameters called x and y.
    The third input parameter is another function.
    When executed, f(x,y) is calculated. As f defaults to add (default argument), the default return
    value is x + y. Otherwise it depends on what function f is provided.
    
    Note: The parameter "f" is set to "add" without opening and closing brackets!
    
    
    @param:    x    Goes into f as first parameter
    @param:    y    Goes into f as second parameter
    @param:    f    A function to be applied on x and y
    @return:        return of f(x, y)
    """
    
    return f(x, y)
    

sub(5, 2)
sub(5)
complexCalculation(10, 11, d = 55, g=32)
mathOperation(2, 5)
mathOperation(2, 5, sub)
