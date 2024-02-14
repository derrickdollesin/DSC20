"""
DSC 20 Winter 2024 Homework 05
Name: Derrick Dollesin
PID: A18133427
Source: 
"""
# Question 1
def complexity_tf():
    """
    Write your answers to time complexity True/False questions in this
    function. No new doctests required.

    >>> answers = complexity_tf()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, bool) for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (True/False) #
    return [True, False, True, False, False, False, False, False, True, True]


# Question 2
def complexity_mc():
    """
    Write your answers to time complexity multiple-choice questions in this
    function. No new doctests required.
    
    >>> answers = complexity_mc()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    15
    >>> all([isinstance(ans, int) and 1 <= ans <= 10 for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (1-10, duplicates allowed) #
    return [1, 6, 4, 5, 4, 7, 1, 7, 7, 3, 2, 1, 6, 10, 6]


# Problem 3
def decipher_text(key1, key2, key3):
    """
    Utilizes an inner function that takes in a text, and deciphers the text \
    using three characters and set rules as follows:

    Rule One:
        - The letter is key1 and
        - the index of the character is odd -> convert letter to "i"
        - the index of the character is even -> convert to letter "e"

    Rule Two:
        - The letter is key2 and
        - The index of the character is odd -> convert to letter "o"
        - The index of teh character is even -> convert to letter "a"

    Rule Three:
        The letter is key3 -> convert letter to "u"

    Args:
        key1: length-one string (char)
        key2: length-one string (char)
        key3: length-one string (char)

    Returns:
        an inner function that takes in a string, cipher_text, and returns a \
        decoded new string (all in lowercase)

    >>> decipher_text('Q', 'b', 'C')('bNswqR')
    'answer'
    >>> decipher_text('W', 'J', 'Z')('TESTYJZRCJDE')
    'testyourcode'
    >>> decipher_text('W', 'J', 'Z')('ONWTWST')
    'onetest'
    >>> decipher_text('D', 's', 'c')('')
    ''

    # Add at least 3 doctests below here #

    >>> decipher_text("a", "4", "3")("g4s3g")
    'gosug'

    >>> decipher_text("#", "&", "%")("aebfskjdf")
    'aebfskjdf'

    >>> decipher_text("f", "z", "g")("vksnfzgioe")
    'vksneouioe'

    """
    # YOUR CODE GOES HERE #

    def cipher(cipher_text):
        output = list(cipher_text)
        check_odd = lambda x: x % 2 != 0
        count = 0

        for i in output:

            if i.lower() == key1.lower():

                if check_odd(count):
                    output[count] = "i"
                else:
                    output[count] = "e"

            elif i.lower() == key2.lower():

                if check_odd(count):
                    output[count] = "o"
                else:
                    output[count] = "a"

            elif i.lower() == key3.lower():

                output[count] = "u"

            count += 1

        return "".join(output).lower()

    return cipher
  
  
# Problem 4
def grade_calculator(w1, w2):
    """
    Calculates the grade in DSC20 based off weights of labs and homeworks

    Args:
        w1: float number for weights of labs
        w2: float number for weights of homeworks

    Returns:
        two functions, both functions take two tuples of integers \
        representing the score you got for your labs and homeworks

    >>> output = grade_calculator(0.4, 0.6)
    >>> len(output) == 2
    True
    >>> output[0]((1, 1, 0.5), (1, 1, 1))
    0.93
    >>> output[1]((0.6, 0.7, 0.8), (0.8, 0.8, 0.8))
    'C'
    >>> output[1]((0.5,), (1,))
    'B'
    >>> output[1]((), ())
    'F'
    >>> output[0]((), ())
    0.0
    >>> output[0]((1,), (1,))
    1.0
    >>> output[0]((1,), ())
    0.4

    # Add at least 3 doctests below here #
    
    >>> output = grade_calculator(0.1, 0.9)

    >>> output[1]((1, 1, 1, 1, 1, 1), (0, 0.5, 0.6, 0.9, 0.7, 0.2))
    'F'
    >>> output[0]((1, 1, 1, 1, 1, 1), (0, 0.5, 0.6, 0.9, 0.7, 0.2))
    0.54

    >>> output = grade_calculator(0.5, 0.5)

    >>> output[0]((1, 0.5, 0.9), (0.7, 0.3, 1))
    0.73

    """
    # YOUR CODE GOES HERE #

    def percentage_grade(labs, homeworks):
        num_labs = len(labs)
        num_homeworks =  len(homeworks)

        if num_labs == 0:
            num_labs = 1

        if num_homeworks == 0:
            num_homeworks = 1

        grade = (w1/num_labs)*sum(labs) + (w2/num_homeworks)*sum(homeworks)

        return round(grade, 2)

    def letter_grade(labs, homeworks):

        grade = percentage_grade(labs, homeworks)

        if grade >= 0.9:
            return "A"
        elif grade >= 0.8:
            return "B"
        elif grade >= 0.7:
            return "C"
        elif grade >= 0.6:
            return "D"
        else:
            return "F"

    return percentage_grade, letter_grade
