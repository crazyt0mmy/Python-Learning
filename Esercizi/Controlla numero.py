def num_check(x):
    try:
        float(x)
        return True
    except ValueError:
        return False