#!/usr/bin/env python3
"""
grouping multiple tests in a class
"""

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    
    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
