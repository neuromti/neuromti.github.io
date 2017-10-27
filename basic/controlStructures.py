'''
Created on Sep 13, 2017

@author: maximilianscherer
'''

"""
    This module describes basic control structures
"""

import random
#https://docs.python.org/3/library/random.html
random.seed()

#Example use of the control structure if
def condition():
    """
    Syntax:    if (condition_1):            <- required
                    What to do here_1       <- required
               elif(condition_2):           <- optional
                    What to do here_2       <- required, if "elif(condition_2)" exists, otherwise optional
               elif(condition_3):           <- optional
                    What to do here_3       <- required, if "elif(condition_3)" exists, otherwise optional
               else:                        <- optional
                    What to do here_4       <- required, if "else" exists, otherwise optional
    """
    
    x = random.random() #Return the next random floating point number in the range [0.0, 1.0).
    
    if (x < 1/3): # Checks whether x is smaller than 1/3
        print("Smaller than 1/3")
    elif (x < 2/3): # Is only checked if the previous condition is "False"
        print("Larger than 1/3, but smaller than 2/3")
    else: # In any case not matching either conditions, else is execute
        print("Larger than 2/3")

#Example use of the control structure for
def forLoop():
    """
    Syntax:    for (variable/tuple) in (list/range/Basically anything which is iterable)    <- required
                    What do do here                                                         <- required
    """
    for x in range(0, 10):
        print(x)
        
        
#Example use of the control structure while
def whileLoop():
    """
    Syntax    while (condition = True):    <- required
                   What to do here         <- required
    """
    x = 0
    while(x < 10):
        print(x)
        x += 1
