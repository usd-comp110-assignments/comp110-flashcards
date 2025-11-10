"""
Module: comp110_lab11

Lab 11: A flash card program.
"""
import random

def test_get_flash_cards():
    """
    Test function for get_flash_cards.
    """

    # TODO: update inputs and expected outputs of the test cases. Delete this line when you are done.

    # Mulitiple quiz questions
    input = ''
    expected = {}
    actual = get_flash_cards(input)

    if actual == expected:
        print("Test 1 PASSED")
    else:
        print("Test 1 FAILED!")
        print("Expected:", expected)
        print("Actual:", actual)

    #TODO: fill out test equivalency class
    input = ''
    expected = {}
    actual = get_flash_cards(input)

    if actual == expected:
        print("Test 2 PASSED")
    else:
        print("Test 2 FAILED!")
        print("Expected:", expected)
        print("Actual:", actual)

    #TODO: fill out test equivalency class
    input = ''
    expected = {}
    actual = get_flash_cards(input)

    if actual == expected:
        print("Test 3 PASSED")
    else:
        print("Test 3 FAILED!")
        print("Expected:", expected)
        print("Actual:", actual)

def get_flash_cards(filename):
    """
    You will add the docstring for this function.
    """
    pass


# To Do: Define your quiz function immediately AFTER this line.


def main():
    pass # remove this line when implementing main


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