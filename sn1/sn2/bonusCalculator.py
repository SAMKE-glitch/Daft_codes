#!/usr/bin/env python3
"""
As a software developer in an HR or Finance team, you might need to work on tasks related to personnel management. For instance, suppose your firm has just approved a new policy to give all developers a bonus equal to 10% of their salary. Your task is to update the database to reflect this new policy.
"""
from typing import List


class Solution:
    def bonusCalculator(self, employees: List[Dict]) -> List[Dict]:
        for employee in employees:
            bonus = 0
            if employee['role'] == 'developer':
                bonus = employee['salary'] * 0.10
            employee['bonus'] = bonus
        return employees

