"""
a progress bar example, using the `rich` pkg (it avoids the chance flickering of tqdm progress bars)
Docs- https://rich.readthedocs.io/en/stable/progress.html
"""

import time
from rich.progress import Progress, track
from rich.progress import TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn, TimeElapsedColumn, SpinnerColumn
from rich.console import Console
from rich.theme import Theme
from rich.style import Style

# Define the theme with black and white color
custom_theme = Theme({"bar.back": "black", "bar.complete": "white"})
console = Console(theme=custom_theme)


def take_action(num):
    num**num


# Custom Class
# more "columns" defined here- https://arc.net/l/quote/xmmpxkhk
# i.e; modules for customizing the pbar --> go crazy with a custom definition
bwpbar = Progress(
    TextColumn("[progress.description]{task.description}"),
    SpinnerColumn(style=Style(color="white")),
    BarColumn(
        complete_style=Style(color="white"),
        finished_style=Style(color="white"),
    ),
    TaskProgressColumn(text_format="[white]{task.percentage:>3.0f}%"),
    # TimeRemainingColumn(),
    # TimeElapsedColumn(),
)

# with Progress() as progress: #default, custom below
with bwpbar as progress:
    task1 = progress.add_task("[black]Downloading", total=1000)
    task2 = progress.add_task("[blue]Processing", total=1000)
    task3 = progress.add_task("[white]Cooking", total=1000)

    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=3.0)
        progress.update(task3, advance=0.9)
        time.sleep(0.02)

for step in track(range(100), description="iterating", ):
    time.sleep(0.001*step)
    take_action(step)
