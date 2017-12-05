# math.py


def my_add(a, b):
    """Adds two inputs

    Parameters
    ----------
    a : int, float
    b : int, float

    Returns
    -------
    sum : int, float
        Sum of a and b
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Input to my_add should be either integers or floats')

    return a + b
