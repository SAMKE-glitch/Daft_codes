#!/usr/bin/env python3
"""
Alright, my friend! Time to put on your coding cap!
Imagine you are in a corporate setting and you have a list of employee votes represented as integers like
[a1, a2, ...an]
These integers actually represent the IDs of your fellow employees. And yes, people can indeed vote for themselves!
An employee gets elevated to the exclusive board member position only if they bag at least n / 3 votes, with n being the total number of votes. Your task: find out the ID of this popular employee. If no one hits the vote mark, return -1. If multiple employees received at least n / 3 votes, return any of them!

The votes are delivered to you in list format. As an illustration, [1, 2, 3, 3, 3] means employees 1 and 2 voted for themselves, and employee 3 received three votes. Hang tight-there can be edge cases, such as no votes or everybody voting for themselves.

Your end goal is to return the lucky candidate's ID if they secure a seat on the board. If no one qualifies, return -1. Got it, superstar? Now it's time to put your coding prowess to the test and sort out this corporate election pronto!
"""
from typing import List



class Solution:
    def elect_board_member(self, votes: List[int]) -> int:
        count_dict = {}

        for id_member in votes:
            count_dict[id_member] = count_dict.get(id_member, 0) + 1
            if count_dict[id_member] > len(votes) / 3:
                return id_member
        return -1
