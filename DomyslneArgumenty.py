"""
Domyślne argumenty
Jeżeli nie podamy drugiego argumenty to będzie on domyślne wynosił 1
"""

def increment(x, amount = 1):
    return x + amount

print(increment(1))