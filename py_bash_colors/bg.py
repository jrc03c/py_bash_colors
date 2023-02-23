# Background colors
from .fx import reset


def black(x):
    return reset("\x1b[40m" + x)


def red(x):
    return reset("\x1b[41m" + x)


def green(x):
    return reset("\x1b[42m" + x)


def yellow(x):
    return reset("\x1b[43m" + x)


def blue(x):
    return reset("\x1b[44m" + x)


def magenta(x):
    return reset("\x1b[45m" + x)


def cyan(x):
    return reset("\x1b[46m" + x)


def white(x):
    return reset("\x1b[47m" + x)
