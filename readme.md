# Intro

`py_bash_colors` is a little package for Python for printing text in colors. It's just a Python version of my [bash-colors](https://github.com/jrc03c/bash-colors) JS library.

# Installation

Install with `pip`:

```bash
pip install -U git+https://github.com/jrc03c/py_bash_colors
```

Or install with `conda`:

```bash
conda install pip git
pip install -U git+https://github.com/jrc03c/py_bash_colors
```

# Usage

```python
import py_bash_colors as colors

print(colors.fg.red("This text is red!"))
print(colors.bg.cyan("This text has a cyan background!"))
print(colors.fx.blink("This text is blinking!"))
```

# API

All of the following are callable as functions that take a single string argument and return that argument wrapped in [Bash color codes](https://gist.github.com/jrc03c/f7a05f2e14876707f5f78f280856da90). You'll usually want to `print` the return value.

**Text effects:**

```
py_bash_colors.fx.reset
py_bash_colors.fx.bright
py_bash_colors.fx.dim
py_bash_colors.fx.underscore
py_bash_colors.fx.blink
py_bash_colors.fx.reverse
py_bash_colors.fx.hidden
```

**Foreground colors:**

```
py_bash_colors.fg.black
py_bash_colors.fg.red
py_bash_colors.fg.green
py_bash_colors.fg.yellow
py_bash_colors.fg.blue
py_bash_colors.fg.magenta
py_bash_colors.fg.cyan
py_bash_colors.fg.white
```

**Background colors:**

```
py_bash_colors.bg.black
py_bash_colors.bg.red
py_bash_colors.bg.green
py_bash_colors.bg.yellow
py_bash_colors.bg.blue
py_bash_colors.bg.magenta
py_bash_colors.bg.cyan
py_bash_colors.bg.white
```
