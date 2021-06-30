from typing import no_type_check_decorator
import typing_extensions


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    
    try:
        new_num = int(message)
    except:
        message
print(not_number_rejector(ten))