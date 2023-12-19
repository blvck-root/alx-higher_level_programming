#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return a / b
    except (TypeError, ZeroDivisionError):
        return None
