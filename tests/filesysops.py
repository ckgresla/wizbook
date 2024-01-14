from rich.console import Console
from rich.table import Table
import os
from wizbook.config import DATA_DIR
from wizbook.io import write_delim_data, read_delim_data


filepath = os.path.join(DATA_DIR, "wiz.tsv")


data = [['Hello, world!', 'AI'], ['Example', 'Test']]

write_delim_data(
    filepath,
    data,
    "\t"
)

data = read_delim_data(filepath, "\t")


# visualize it elegantly
console = Console()

table = Table(show_header=True, header_style="magenta")
for row in data:
    table.add_row(*row)

console.print(table)
