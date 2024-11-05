#!/usr/bin/env python3
"""
using context provided by raises to assert that an expected exceptio
is a part of a raised ExceptionGroup
"""
import pytest


def f():
    raise ExceptionGroup(
            "Group message",
            [
                RuntimeError(),
            ],
    )

def test_exception_in_group():
    with pytest.raises(ExceptionGroup) as excinfo:
        f()
    assert excinfo.group_contains(RuntimeError)
    assert not excinfo.group_contains(TypeError)
