# -*- coding: utf-8 -*-
"""
@author: jiale

2025-2-20

"""

def question(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        elif answer in {"n", "no"}:
            return False
        else:
            print("Invalid input. Please enter 'y' (yes) or 'n' (no).")
