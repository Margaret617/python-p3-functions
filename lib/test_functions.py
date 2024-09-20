import io
import sys
import pytest
from functions import greet_programmer, greet, greet_with_default, add, halve


def test_greet_programmer(capfd):
    greet_programmer()
    captured = capfd.readouterr()
    assert captured.out == "Hello, programmer!\n"


def test_greet(capfd):
    greet("Guido")
    captured = capfd.readouterr()
    assert captured.out == "Hello, Guido!\n"


def test_greet_with_default_no_arg(capfd):
    greet_with_default()
    captured = capfd.readouterr()
    assert captured.out == "Hello, programmer!\n"


def test_greet_with_default_with_arg(capfd):
    greet_with_default("Sunny")
    captured = capfd.readouterr()
    assert captured.out == "Hello, Sunny!\n"


def test_add():
    assert add(45, 55) == 100


def test_halve_int():
    assert halve(100) == 50


def test_halve_float():
    assert halve(99.0) == 49.5
