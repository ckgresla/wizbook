"""
Beautiful things are better! This module contains: 
- colorful printing (ala simple funcs)
- palette dicts (names to color code mappings)
- context manager to hide unnecessary stdout

"""

import os
import sys
import time

from rich.console import Console
from rich.progress import Progress, track
from rich.progress import TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn, TimeElapsedColumn, SpinnerColumn
from rich.theme import Theme
from rich.text import Text
from rich.style import Style


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



# a tasteful black and white pbar, ala rich 
class BWTimeRemainingColumn(TimeRemainingColumn):
    def render(self, task):
        remaining = task.time_remaining
        if remaining is None:
            return Text.from_markup("[white]?:??:??")
        return Text.from_markup("[white]{:02}:{:02}:{:02}".format(int(remaining // 3600), int((remaining % 3600) // 60), int(remaining % 60)))

class BWTimeElapsedColumn(TimeElapsedColumn):
    def render(self, task):
        elapsed = task.elapsed
        return Text.from_markup("[white]{:02}:{:02}:{:02}".format(int(elapsed // 3600), int((elapsed % 3600) // 60), int(elapsed % 60)))

bwpbar = Progress(
    TextColumn("[progress.description]{task.description}"),
    SpinnerColumn(style=Style(color="white")),
    BarColumn(
        complete_style=Style(color="white"),
        finished_style=Style(color="white"),
    ),
    TaskProgressColumn(text_format="[white]{task.percentage:>3.0f}%"),

    # customs, very tasteful
    BWTimeRemainingColumn(),
    BWTimeElapsedColumn(),
    # defaults, not tasteful
    # TimeRemainingColumn(),
    # TimeElapsedColumn(),
)


# functional usage (similar to the tqdm api)
# NOTE: that for enumeration, you have to wrap the *inside* of the enumerate w this func!
def bw_pbar(iterable, description="grinding...", total=None):
    """
    to call like tqdm, one might use as follows 
    for item in bwpbar_iter(range(100), description='processing...'):
        # do something
        ...
    """
    CustomProgressBar = Progress(
        TextColumn("[progress.description]{task.description}"),
        SpinnerColumn(style=Style(color="white")),
        BarColumn(
            complete_style=Style(color="white"),
            finished_style=Style(color="white"),
        ),
        TaskProgressColumn(text_format="[white]{task.percentage:>3.0f}%"),
        BWTimeRemainingColumn(),
        BWTimeElapsedColumn(),
    )

    # actual iteration
    with CustomProgressBar:
        task_id = CustomProgressBar.add_task(description, total=total or len(iterable))
        for item in iterable:
            yield item
            CustomProgressBar.advance(task_id)



