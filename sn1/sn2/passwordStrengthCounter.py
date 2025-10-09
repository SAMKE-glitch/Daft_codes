#!/usr/bin/env python3
"""
As an application developer, ensuring the security of user data is pivotal. A common measure to ensure robust security is testing the strength of passwords. A 'strong' password is usually defined as one that is long (at least 8 characters) and includes a mix of uppercase characters, lowercase characters, and digits.
"""


class Solution:
    def passwordStrengthCounter(self, password:str) -> str:
        strength = {
            'length': False,
            'digit': False,
            'lowercase': False,
            'uppercase': False,
        }

        if len(password) >= 8:
            strength['length'] = True

        for char in password:
            if char.isdigit():
                strength['digit'] = True
            elif char.islower():
                strength['lowercase'] = True
            elif char.isupper():
                strength['uppercase'] = True

        score = sum(strength.values())

        if score == 4:
            return 'Strong'
        elif score == 3:
            return 'Moderate'
        else:
            return 'Weak'

if __name__ == "__main__":
    s = Solution()
    print(s.passwordStrengthCounter("P4ssword"))  # Strong
    print(s.passwordStrengthCounter("password"))  # Weak
    print(s.passwordStrengthCounter("Pass12"))    # Moderate
