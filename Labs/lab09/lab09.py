"""
DSC 20 Winter 2024 Lab 09
Name: Derrick Dollesin  
PID: A18133427
Source: 
"""

# Utility data structures
landscapes = ['Return vs Print', 'Dictionaries', 'Files', 'List Comprehension',
              'Lambda Functions', 'Iterators', 'Complexity', 
              'Scope of variables', 'Classes and Objects', 'Inheritance', 
              'Special Methods','Mutable data']
num_landscapes = 12

# Question 1
def admission_checker(xp_levels):
    """
    Checks necessary conditions for admission into Javania. Raise an exception
    when condition check fails. If all necessary conditions pass, evaluate
    capability to survive in Javania -- return True if it passes 
    and False otherwise.

    >>> xp_levels = {'Return vs Print': 20, 'Dictionaries': 20, 'Files': 20,\
        'List Comprehension': 20, 'Lambda Functions': 20, 'Iterators': 20,\
        'Complexity': 20, 'Scope of variables': 20, 'Classes and Objects': 20,\
        'Inheritance': 20, 'Special Methods': 20, 'Sorting': 20}
    >>> admission_checker(xp_levels)
    Traceback (most recent call last):
    ...
    KeyError: 'Landscape Sorting does not exist in Pythonia!'
    >>> xp_levels = {'Return vs Print': 20, 'Dictionaries': 20, 'Files': 20,\
        'List Comprehension': 20, 'Lambda Functions': 20, 'Iterators': 20,\
        'Complexity': 20, 'Scope of variables': 20, 'Classes and Objects': 20,\
        'Inheritance': 20, 'Special Methods': 20, ('Mutable data',): 20}
    >>> admission_checker(xp_levels)
    Traceback (most recent call last):
    ...
    TypeError: Landscape is represented in a wrong way!
    >>> xp_levels = {'Return vs Print': 20, 'Dictionaries': 20, 'Files': 20,\
        'List Comprehension': 10, 'Lambda Functions': 10, 'Iterators': 10,\
        'Complexity': 10, 'Scope of variables': 10, 'Classes and Objects': 10,\
        'Inheritance': 10, 'Special Methods': 10, 'Mutable data': 10}
    >>> admission_checker(xp_levels)
    False
    >>> xp_levels = {'Return vs Print': 20, 'Dictionaries': 20, 'Files': 20,\
        'List Comprehension': 20, 'Lambda Functions': 20, 'Iterators': 20,\
        'Complexity': 20, 'Scope of variables': 20, 'Classes and Objects': 20,\
        'Inheritance': 20, 'Special Methods': 20, 'Mutable data': 20}
    >>> admission_checker(xp_levels)
    True
    """
    # YOUR CODE GOES HERE #
    
    if not isinstance(xp_levels, dict):
        raise TypeError("Survey result is represented in a wrong way!")

    if not all([isinstance(key, str) for key in xp_levels]):
        raise TypeError("Landscape is represented in a wrong way!")

    for key in xp_levels:
        if not isinstance(xp_levels[key], int):
            raise TypeError(f"Experience level for {key} is represented in a \
wrong way!")

        if not xp_levels[key] % 10 == 0:
            raise ValueError(f"Experience level for {key} is incorrectly \
entered!")

        if not key in landscapes:
            raise KeyError(f"Landscape {key} does not exist in Pythonia!")

    if len(xp_levels) < 6:
        raise KeyError("You miss too many Pythonia landscapes!")

    if len(xp_levels) >= 9 and (sum(list(xp_levels.values())) / \
    len(xp_levels)) >= 20:
        return True
    else:
        return False

# Question 2
class Javanian():
    '''
    Implementation of a Player in Javania.

    >>> kate = Javanian({'LinkedLand': 20, 'QueueChannel': 10,\
            'Stack Sand Dunes': 50})
    >>> jim = Javanian({'Javalake': 20, 'Interface Canyon': 10,\
            'this.valley': 30, 'BST': 40})
    >>> gabi = Javanian({'LinkedLand': 30, 'Disjoint Forest': 40})
    >>> gabi
    LinkedLand, Disjoint Forest
    >>> print(gabi)
    I visited 2 places and have a total of 70 XP points.
    >>> jim
    Interface Canyon, Javalake, this.valley, BST
    >>> print(jim)
    I visited 4 places and have a total of 100 XP points.
    >>> kate
    QueueChannel, LinkedLand, Stack Sand Dunes
    >>> print(kate)
    I visited 3 places and have a total of 80 XP points.
    >>> gabi > 100
    False
    >>> jim > kate
    True
    >>> kate > gabi
    True
    >>> len(gabi)
    2
    >>> len(jim)
    4
    >>> len(kate)
    3
    '''
    # Question 2.1 (Initialization)
    # YOUR CODE GOES HERE #

    def __init__(self, xp_levels):
        self.xp_levels = xp_levels
    
    # Question 2.2 (String Representations)
    # YOUR CODE GOES HERE #

    def __repr__(self):
        sorted_xp_levels = dict(sorted(self.xp_levels.items(), key=lambda \
        item: item[1]))

        return ", ".join(list(sorted_xp_levels.keys()))

    def __str__(self):
        return f"I visited {len(self.xp_levels)} places and have a total of \
{sum(list(self.xp_levels.values()))} XP points."
    
    # Question 2.3 (Greater than Method)
    # YOUR CODE GOES HERE #
    
    # Question 2.4 (Length Method)
    # YOUR CODE GOES HERE #
