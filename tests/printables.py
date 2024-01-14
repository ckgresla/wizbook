# sample usage here
from wizbook.viz import *


text = ("yo dude!")
data = [
    {
        "wiz": "bang"
    },
    lambda x: x**2
]
printerr(text)
printwar(text)
printlog(text)
printok(text)


printok(text, text, "pretty nice?", sep=" --> ", end="\n\n")

printlog(data)