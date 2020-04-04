import unittest


def before_all_tests():
    print("Hello test suite!")

def after_all_tests():
    print("Goodbye test suite!")

def run_it():
    before_all_tests()

    #all the tests
    
    after_all_tests()