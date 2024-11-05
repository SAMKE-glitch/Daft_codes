#!/usr/bin/env python3
"""
pytesting sysexit
"""
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
