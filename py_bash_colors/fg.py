# Foreground colors
from .fx import reset


def black(x):
    return reset("\x1b[30m" + x)


def red(x):
    return reset("\x1b[31m" + x)


def green(x):
    return reset("\x1b[32m" + x)


def yellow(x):
    return reset("\x1b[33m" + x)


def blue(x):
    return reset("\x1b[34m" + x)


def magenta(x):
    return reset("\x1b[35m" + x)


def cyan(x):
    return reset("\x1b[36m" + x)


def white(x):
    return reset("\x1b[37m" + x)
