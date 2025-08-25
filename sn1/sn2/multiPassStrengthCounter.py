#!/usr/bin/env python3
"""
Alright, Space Voyager! Let's apply our knowledge to something a tad trickier - an array of passwords, each one a unique mystery to be solved. Imagine you're working as a security analyst, huh? Your mission, if you choose to accept it, is to create a program to evaluate the strength of multiple passwords.

You are to write a function that takes a list of passwords as input. Each password in the list will be a non-empty string. The function should output a list of dictionaries, with each dictionary corresponding to a password in the original list. Each dictionary will have five keys: 'length', 'digit', 'uppercase', 'lowercase', and 'special_char'. The value for each key will be a Boolean indicating whether the password meets a particular criterion: has at least 8 characters for 'length', contains a digit for 'digit', contains an uppercase letter for 'uppercase', contains a lowercase letter for 'lowercase', and contains a special character (one of "!@#$%^&*()-+") for 'special_char'.

Get ready to dive into the world of security analysis – this is where the real fun begins!
"""
from typing import List

class Solution:
    def multi_password_strength_counter(self, password: List[str]) -> List[dict]:
        special_characters = "!@#$%^&*()-+"

        results = []

        for pwd in passwords:
            stength = {
                "length": len(pwd) >= 8
                "digit": any(ch.isdigit() for ch in pwd)
                "lowercase": any(ch.islower() for ch in pwd)
                "uppercase": any(ch.isupper() for ch in pwd)
                "special_char": any(ch in special_char)
            }
            results.append(strength)

        return results
