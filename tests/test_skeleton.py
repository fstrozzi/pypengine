#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pypengine.skeleton import fib

__author__ = "Francesco Strozzi"
__copyright__ = "Francesco Strozzi"
__license__ = "none"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
