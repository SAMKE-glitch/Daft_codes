#!/usr/bin/env python3


# CLOSURES

def mainWelcome():
    msg = "Hello Everyone"
    def subWelcomeClass():
        print("Welcome to samke Youtube Channel")
        print(msg)
        print("Please subrscibe to Samke channel")
    return subWelcomeClass()
