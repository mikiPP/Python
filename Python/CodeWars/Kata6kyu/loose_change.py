"""In this Kata you must create a function that takes an amount of US currency in cents,
 and returns a dictionary which shows the least amount of coins used to make up that amount. The only coin denominations considered in this exercise are:
 Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢). Therefor the dictionary returned should contain exactly 4 key/value pairs."""

from math import floor


def loose_change(cents):
    nickels = 0
    pennies = 0
    dimes = 0
    quarters = 0

    while cents >= 1:
        if 25 <= cents:
            quarters = floor(cents / 25)
            cents = cents % 25

        elif 10 <= cents:
            dimes = floor(cents / 10)
            cents = cents % 10

        elif 5 <= cents:
            nickels = floor(cents / 5)
            cents = cents % 5

        elif 1 <= cents:
            pennies = floor(cents / 1)
            cents = cents % 1

    change = {'Nickels': nickels, 'Pennies': pennies,
              'Dimes': dimes, 'Quarters': quarters}
    return change


if __name__ == '__main__':
    assert loose_change(29) == {'Nickels': 0,
                                'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) == {'Nickels': 1,
                                'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert loose_change(0) == {'Nickels': 0,
                               'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) == {'Nickels': 0,
                                'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {'Nickels': 0,
                                 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
