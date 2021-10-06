import math
from math import sqrt


def is_even(number):
    return number % 2 == 0


def is_prime(number):
    if number < 2:
        return False
    if number != 2 and is_even(number):
        return False
    for factor in range(3, number // 2 + 1, 2):
        if number % factor == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(-2) is False
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(9) is False
    assert is_prime(11) is True
    assert is_prime(19) is True
    assert is_prime(20) is False
    print("All tests for 'is_prime' function successfully passed.")


def get_largest_prime_below(n):
    if n < 3:
        return 0
    while n > 0:
        n -= 1
        if is_prime(n):
            return n
    return 0
    '''
    
    :param n: An integer number for which we want to determine the largest prime below.
    :return: An integer number representing the largest prime below 'input' if it exists, otherwise 0.
    '''


def test_get_largest_prime_below():
    assert get_largest_prime_below(7) == 5
    assert get_largest_prime_below(-2) == 0
    assert get_largest_prime_below(9) == 7
    assert get_largest_prime_below(4) == 3
    assert get_largest_prime_below(3) == 2
    assert get_largest_prime_below(2) == 0
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(78) == 73


def get_perfect_squares(start, end):
    result = []
    if start > end or start < 0:
        return result
    candidate_root = math.ceil(sqrt(start))
    candidate = candidate_root * candidate_root
    while candidate <= end:
        result.append(candidate)
        candidate += 2 * candidate_root + 1
        candidate_root += 1
    return result

    '''
    Determines all the perfect squares in an interval.
    :param start: The lower bound of the interval. Inclusive.
    :param end: The upper bound of the interval. Inclusive.
    :return: A list containing all the perfect squares bounded by 'start' and 'end'.
    '''


def test_get_perfect_squares():
    assert get_perfect_squares(5, 4) == []
    assert get_perfect_squares(5, 5) == []
    assert get_perfect_squares(-2, 4) == []
    assert get_perfect_squares(0, 4) == [0, 1, 4]
    assert get_perfect_squares(0, 20) == [0, 1, 4, 9, 16]
    assert get_perfect_squares(3, 100) == [4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert get_perfect_squares(26, 35) == []


def is_superprime(n):
    clone = n
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    if clone <= 0:
        return False
    else:
        return True
    '''
    Tests if a number is a 'superprime'. A number is a 'superprime' if all its prefixes are primes, including the given number.
    :param n: Input number to be checked if it's 'superprime'.
    :return: True if the number it's 'superprime', false otherwise.
    '''


def test_is_superprime():
    assert is_superprime(12) is False
    assert is_superprime(-5) is False
    assert is_superprime(2) is True
    assert is_superprime(233) is True
    assert is_superprime(37) is True
    assert is_superprime(373) is True
    assert is_superprime(3731) is False


def show_options():
    print('''
    1.Compute largest prime below 'n'.
    2.Compute all perfect squares between 'start' and 'end'. 
    3.Determine if a number is a superprime.
    4.Exit the interactive menu.
    ''')


def compute_largest_prime_option():
    number = int(input("Your number 'n' is:"))
    print(f"The largest prime below {number} is {get_largest_prime_below(number)}.")


def compute_bounded_squares_option():
    start = int(input("The lower bound 'start' is:"))
    end = int(input("The upper bound 'end' is:"))
    print(f"The perfect squares bounded by {start} and {end} are: {get_perfect_squares(start, end)}.")


def determine_if_superprime_option():
    n = int(input("Your number 'n' is:"))
    print(f"{n} is super prime? A:{is_superprime(n)}")


test_is_prime()
test_get_largest_prime_below()
test_get_perfect_squares()
test_is_superprime()


def interactive_menu():
    while True:
        show_options()
        option = input("Your option is:")
        if option == '1':
            compute_largest_prime_option()
        elif option == '2':
            compute_bounded_squares_option()
        elif option == '3':
            determine_if_superprime_option()
        elif option == "4":
            break
        else:
            print("Unknown option, try again.")
    print("Exiting the menu.")

interactive_menu()
