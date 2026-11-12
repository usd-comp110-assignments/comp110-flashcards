"""
Module: comp110_lab11

Lab 11: A flash card program.
"""
import random

def test_get_flash_cards():
    """Test function for the get_flash_cards function."""

    # Test 1
    # To Do: Fill out filename and expected result for test 1
    test_description = "No cards"
    filename = ''
    expected_result = {}
    actual_result = get_flash_cards(filename)

    if actual_result == expected_result:
        print("PASSED: Test 1:", test_description)
    else:
        print("FAILED: Test 1:", test_description)
        print("\tExpected Return:", expected_result)
        print("\tActual Return:", actual_result)

    # Test 2
    # To Do: Fill out the filename and expected result for test 2
    test_description = "One card"
    filename = ''
    expected_result = {}
    actual_result = get_flash_cards(filename)

    if actual_result == expected_result:
        print("PASSED: Test 2:", test_description)
    else:
        print("FAILED: Test 2:", test_description)
        print("\tExpected Return:", expected_result)
        print("\tActual Return:", actual_result)

    # Test 3
    # To Do: Fill out filename and expected result for test 3
    test_description = "Multiple cards"
    filename = ''
    expected_result = {}
    actual_result = get_flash_cards(filename)

    if actual_result == expected_result:
        print("PASSED: Test 3:", test_description)
    else:
        print("FAILED: Test 3:", test_description)
        print("\tExpected Return:", expected_result)
        print("\tActual Return:", actual_result)


def get_flash_cards(filename):
    """To Do: Write a docstring for this function, using the proper formatting."""
    
    return {} # To Do: remove this line and implement this function


# To Do: Define your quiz function immediately AFTER this line.


def main():
    """Implements a flash card game to test someone's memory.
    
    The user will enter the name of a file with flash cards and a target score and the
    program will continually quiz them on the flash cards until they get the target amount
    correct.
    """
    
    pass # To Do: Remove this line and implement the function.


""" DO NOT MODIFY ANYTHING BELOW THIS LINE! """
if __name__ == "__main__":
    
    selection = int(input("Enter function to test:\n 1) test_get_flash_cards\n 2) quiz\n 3) main:\n "))
    if selection == 1:
        test_get_flash_cards()
    elif selection == 2:
        quiz_dictionary = {'cow': 'vaca', 'cat': 'gato', 'food': 'comida', 'apple': 'manzana', 'smile': 'sonrisa'}
        target_score = 1
        questions_asked = quiz(quiz_dictionary, target_score)
        print(f"Questions asked to get to target score of {target_score} = {questions_asked}")
        target_score = 3
        questions_asked = quiz(quiz_dictionary, target_score)
        print(f"Questions asked to get to target score of {target_score} = {questions_asked}")
    elif selection == 3:
        main()