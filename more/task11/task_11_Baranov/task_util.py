from math import sin

def get_task(d1, d2):
    if sin(d1*d2) > 0.99999999:
        return (d1, d2, sin(d1*d2))