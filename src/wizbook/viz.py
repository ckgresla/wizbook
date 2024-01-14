"""
Beautiful things are better! This module contains: 
- colorful printing (ala simple funcs)
- palette dicts (names to color code mappings)
- context manager to hide unnecessary stdout

"""

import os
import sys
from rich.console import Console


# Consts et al
console = Console()

catppuccin_colors = {
    # taken from the mocha palette- https://github.com/catppuccin/catppuccin
    "rosewater":  "#f5e0dc",
    "flamingo":   "#f2cdcd",
    "pink":       "#f5c2e7",
    "mauve":      "#cba6f7",
    "red":        "#f38ba8",
    "maroon":     "#eba0ac",
    "peach":      "#fab387",
    "yellow":     "#f9e2af",
    "green":      "#a6e3a1",
    "teal":       "#94e2d5",
    "sky":        "#89dceb",
    "sapphire":   "#74c7ec",
    "blue":       "#89b4fa",
    "lavender":   "#b4befe",
    "text":       "#cdd6f4",
    "subtext1":   "#bac2de",
    "subtext0":   "#a6adc8",
    "overlay2":   "#9399b2",
    "overlay1":   "#7f849c",
    "overlay0":   "#6c7086",
    "surface2":   "#585b70",
    "surface1":   "#45475a",
    "surface0":   "#313244",
    "base":       "#1e1e2e",
    "mantle":     "#181825",
    "crust":      "#11111",
}


# Quick Utils for [Errors, Warnings, Logs/Info, Good Things]
def printerr(*args, **kwargs):
    console.print(*args, **kwargs, style="red")


def printwar(*args, **kwargs):
    console.print(*args, **kwargs, style="yellow")


def printlog(*args, **kwargs):
    console.print(*args, **kwargs, style="blue")


def printok(*args, **kwargs):
    console.print(*args, **kwargs, style="green")


# TTY Helpers
def clear_screen():
    """ a python function equivalent of the `clear` cmd or the `ctrl+l` keyboard shortcut """
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
    # use this class like:
    # with HiddenPrints():
    #     print("wow")
    # 'wow' will not print
