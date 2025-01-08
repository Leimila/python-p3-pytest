#!/usr/bin/env python3




# def test_return_not_none():
#     '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
#     assert False
# lib/testing/test_not_none.py

from lib.not_none_functions import not_none_function

def test_not_none():
    assert not_none_function() is not None
