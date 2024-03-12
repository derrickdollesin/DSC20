"""
DSC 20 Winter 2024 Homework 09
Name: Derrick Dollesin
PID: A18133427
Source: 
"""

# Question 1
def q1_tf_answers():
    """
    Write your answers to the True/False questions in this function.
    True if a method mutates an object and False otherwise.
    """
    # YOUR CODE GOES HERE #

    answers = [False, True, False, False, True, False, False, True, False, \
    True]

    return answers


# Question 2
def q2_tf_answers():
    """
    Write your answers to the True/False questions in this function.
    True if the algorithm is in-place and False otherwise.
    """
    # YOUR CODE GOES HERE #

    answers = [True, True, False, False, True]
    
    return answers


# Question 3
def reverse_list(lst):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> x = [3, 2, 4, 5, 1]
    >>> reverse_list(x)
    >>> x
    [1, 5, 4, 2, 3]
    >>> x = []
    >>> reverse_list(x)
    >>> x
    []
    >>> x = [1]
    >>> reverse_list(x)
    >>> x
    [1]

    # Add your own doctests below
    """
    # YOUR CODE GOES HERE #

    original_list = list(lst)
    step = -1
    
    for i in range(len(lst)):
        lst[i] = original_list[step - i]

    return None

# Question 4
def swap_lists(list_1, list_2):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################


    >>> list_1 = [1, 2]
    >>> list_2 = [3, 4]
    >>> swap_lists(list_1, list_2)
    >>> print(list_1)
    [3, 4]
    >>> print(list_2)
    [1, 2]

    >>> list_3 = [4, 2, 6, 8, 90, 45]
    >>> list_4 = [30, 41, 65, 43, 4, 17]
    >>> swap_lists(list_3, list_4)
    >>> print(list_3)
    [30, 41, 65, 43, 4, 17]
    >>> print(list_4)
    [4, 2, 6, 8, 90, 45]

    # Add your own doctests below
    """
    # YOUR CODE GOES HERE #

    for i in range(len(list_1)):
        n1 = list_1[i]
        n2 = list_2[i]

        list_1[i] = n2
        list_2[i] = n1

    return None

# Question 5
def decode_password(hint):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################


    >>> hint = ["Pythonia", "is", "an", "excellent", "Place"]
    >>> decode_password(hint)
    >>> print(hint)
    [6, 3, 1, 2, 6]

    >>> hint = ["great", "to", "SEE", "U", "!", "Goodbye", "."]
    >>> decode_password(hint)
    >>> print(hint)
    [3, 7, 7, 7, 0, 3, 0]

    # Add your own doctests below
    """
    # YOUR CODE GOES HERE #
    
    for i in range(len(hint)):
        word = hint[i]

        if len(word) == 0:
            hint[i] = 0
        else:
            first_char = ord(word[0].lower())
            if 96 <= first_char <= 123:
                hint[i] = (first_char - 97) // 3 + 1
            else:
                hint[i] = 0



# Question 6 (Extra Credit)
def move_non_wishes(seq):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################


    >>> lst1 = [0, 1, 0, 3, 12]
    >>> move_non_wishes(lst1)
    >>> lst1
    [1, 3, 12, 0, 0]

    >>> lst2 = [0, 0, 0]
    >>> move_non_wishes(lst2)
    >>> lst2
    [0, 0, 0]

    >>> lst3 = []
    >>> move_non_wishes(lst3)
    >>> lst3
    []

    >>> lst4 = [1, 2, 3]
    >>> move_non_wishes(lst4)
    >>> lst4
    [1, 2, 3]
    """
    # YOUR CODE GOES HERE #
    return
