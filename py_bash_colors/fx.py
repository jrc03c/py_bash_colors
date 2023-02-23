RESET = "\x1b[0m"


def reset(x):
    return x + RESET


def bright(x):
    return reset("\x1b[1m" + x)


def dim(x):
    return reset("\x1b[2m" + x)


def underscore(x):
    return reset("\x1b[4m" + x)


def blink(x):
    return reset("\x1b[5m" + x)


def reverse(x):
    return reset("\x1b[7m" + x)


def hidden(x):
    return reset("\x1b[8m" + x)
