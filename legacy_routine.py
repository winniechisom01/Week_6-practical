"""The ORIGINAL routine from the code review (Step 11), kept only so the
refactored code can be compared against it. Do not use in the application."""


def x(a, b, c, n):
    t = a + b + c
    if t >= 70:
        g = "A"
    elif t >= 60:
        g = "B"
    elif t >= 50:
        g = "C"
    else:
        g = "F"
    print(n, t, g)
    return t
