import pytest
import sys, os
import numpy as np

sys.path.append(os.path.join(
    os.path.dirname(__file__),
    "../"))

from src.plotting as plotting

plotting.plot()

def hello():
    return "Hello World"

def test_hello():
    assert(hello() == "Hello World")