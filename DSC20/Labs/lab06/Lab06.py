"""
DSC 20 Winter 2024 Lab 06
Name: Derrick Dollesin  
PID: A18133427
Source: 
"""

# Question 1.1
def flamestrike_spell(*args):
    """
    l 
    Takes in an unknown number of nonnegative integers and applies the formula
    10*arg**2 for each arg in args.

    Args:
        *args: an unknown amount of nonnegative integers
    
    Returns:
        a list of modified input values

    >>> flamestrike_spell(1, 2, 3, 4, 5)
    [10, 40, 90, 160, 250]
    >>> flamestrike_spell(0, 1, 2, 3)
    [0, 10, 40, 90]
    >>> flamestrike_spell(78, 142)
    [60840, 201640]
    """
    return [i**2 * 10 for i in args] 

# Question 1.2
def levitation_incantation(weights, weight_threshold=10):
    """
    Returns a list of weights that are at or below the weight threshold.

    Args:
        weights: list of integers (weights)
        weight_threshold: nonnegative integer, default 10
    
    Returns:
        list of integers below/at weight_threshold

    >>> levitation_incantation([5, 8, 12, 15, 18])
    [5, 8]
    >>> levitation_incantation([10, 20, 30, 40, 50], 35)
    [10, 20, 30]
    >>> levitation_incantation([22, 33, 44], weight_threshold = 44)
    [22, 33, 44]
    """
    return list(filter(lambda x: x <= weight_threshold, weights))

# Question 1.3
def enchanted_spell_counter(*args, length=15):
    """
    Returns the number of spells that contain 'Enchanted' and are longer or
    equal to the given length.

    Args:
        *args: unknown number of strings
        length: nonnegative int representing minimum length, default 15

    Returns:
        integer representing number of valid strings

    >>> enchanted_spell_counter("Enchanted Fireball Spell", \
        "Levitation Incantation", "Enchanted Charm", "Teleportation Spell")
    2
    >>> enchanted_spell_counter("Mystic Incantation", "Enchanted Spellbook", \
        "Crystal Ball Gaze", length=20)
    0
    >>> enchanted_spell_counter("Enchanted Spellbook", "Mystic Incantation")
    1
    """
    return len(list(filter(lambda x: "Enchanted" in x and len(x) >= length, \
    args)))

# Question 2
def spell_showcase(length_threshold, **kwargs):
    """
    Returns a dictionary summarizing how many echanted spells (see Q1.3) each
    spellcaster knows.

    Args:
        length_threshold: integer of minimum length to consider enchanted
        **kwargs: dictionary of strings as keys and lists with strings as vals
    
    Returns:
        dictionary of names and number of enchanted spells per name

    >>> spell_showcase(5, hermione=['Enchanted Charm', 'Teleportation Spell'],\
          dumbledore=['Mystic Incantation'])
    {'hermione': 1, 'dumbledore': 0}
    >>> spell_showcase(10, harry=['Wingardium Leviosa', 'Expelliarmus'], \
        voldemort=['Avada Kedavra'])
    {'harry': 0, 'voldemort': 0}
    >>> spell_showcase(20, gandalf=['Enchanted Spellbook', \
        'Crystal Ball Gaze', 'Enchanted Teleportation Spell'], \
            saruman=['Mystic Incantation'])
    {'gandalf': 1, 'saruman': 0}
    """
    return {key: sum([enchanted_spell_counter(i, length=length_threshold) for \
    i in value]) for key, value in kwargs.items() }

# Question 3
def level_up(leveling_factor, *args, **kwargs):
    """
    Returns a dictionary with number of levels leveled up for each caster,
    factoring in additional experience (if any).

    Args:
        leveling_factor: integer to divide total experience
        *args: tuples containing name (str) and current experience (int)
        **kwargs: additional experience for each spellcaster
    
    Returns:
        dictionary of each person's levels gained
    
    >>> factor = 10
    >>> level_up(factor, ("merlin", 350), ("hermione", 500), merlin = 100, \
        hermione = 50)
    {'merlin': 45, 'hermione': 55}

    >>> factor = 50
    >>> level_up(factor, ("merlin", 350), ("gandalf", 500), ("hermione", 250),\
          ("dumbledore", 700), merlin = 100, hermione = 50)
    {'merlin': 9, 'gandalf': 10, 'hermione': 6, 'dumbledore': 14}

    >>> factor = 30
    >>> level_up(factor, ("harry", 200), ("ron", 150), ("hermione", 250), \
        ("neville", 175), harry = 50, neville = 30)
    {'harry': 8, 'ron': 5, 'hermione': 8, 'neville': 6}
    """
    return {i[0]: (i[1] + value)//leveling_factor if i[0] in kwargs else i[1] // leveling_factor for key, value in kwargs.items() for i in args}

# Question 4
def open_cages(**kwargs):
    """
    Returns a function that compares potency of kwargs values to potency
    threshold.

    Args:
        **kwargs: dictionary of spell(str)-strength(int) pairs
    
    Returns:
        inner function

        Returns either a tuple or a string. If formula result is above
        threshold, returns highest strength spell and "Good Job!" in a tuple.
        If below, returns lowest strength spell and "Try Again!" in a tuple.
        Otherwise returns "One more round!"

        Args:
            threshold: positive number (int or float)
        
        Returns:
            tuple or string depending on result

    >>> magic = open_cages(Levitation_Incantation = 4, \
        Enchanted_Charm = 10)
    >>> magic(1000)
    ('Enchanted_Charm', 'Good Job!')
    >>> magic(6000)
    ('Levitation_Incantation', 'Try Again!')
    >>> magic(1852)
    'One more round!'
    """
    return

# Question 5
def spell_resources(limit, *args, **kwargs):
    """
    Returns a dictionary of amounts of ingredients left to get to meet the
    spell casting limit.

    Args:
        limit: non-negative int for number of times to cast the spell
        *args: tuples containing spell names and current quantities
        **kwargs: dictionary containing amounts of each ingredient needed to
        cast a spell once
    
    Returns:
        dictionary with names of ingredients you don't have enough of with
        amounts left to buy to meet the limit

    >>> spell_resources(2, ('unicorn_hair', 4), ('phoenix_feather', 2), \
        unicorn_hair = 3, dragon_scale = 5)
    {'unicorn_hair': 2, 'dragon_scale': 10}
    >>> spell_resources(3, ('moonstone_dust', 0), ('starlight_petals', 2), \
        moonstone_dust = 3, starlight_petals = 5)
    {'moonstone_dust': 9, 'starlight_petals': 13}
    """
    return

# Question 6 (EC, optional)
def cast_attack_spell(sum_powers_limit, defeat_threshold):
    """
    Returns two functions to help create combined spells and reduce the
    sorcerer's HP with said spells.

    Args:
        sum_powers_limit: non-neg int limit of attack power of combined spell
        defeat_threshold: non-negative int
    
    Returns:
        combine_spells and cast_spell functions


        Returns a combined spell tuple of the form (name, power, effect) based
        on a set of rules.
        Name: Sorted alphabetically and joined by hyphens, respecting case.
        Power: Sum of powers, or sum_powers_limit if sum exceeds it
        Effect: "Neutral" unless more than half of spells have same effect

        Args:
            *spells: tuples in (name, power, effect) format
        
        Returns:
            a single tuple in the same format as above


    >>> combine_spells, cast_spell = cast_attack_spell(200, 20)
    >>> combined = combine_spells(('Fireball', 50, 'fire'), \
        ('Fireball', 60, 'fire'))
    >>> print(combined)
    ('Fireball-Fireball', 110, 'fire')
    >>> cast_spell(combined, 40)
    'Sorcerer is defeated by Fireball-Fireball with the fire effect.'
    >>> combined = combine_spells(('Fireball', 50, 'fire'), \
        ('Iceball', 40, 'ice'), ('Lightning', 120, 'lightning'))
    >>> print(combined)
    ('Fireball-Iceball-Lightning', 200, 'neutral')
    >>> cast_spell(combined, 500)
    'Try again'
    """
    return
    
