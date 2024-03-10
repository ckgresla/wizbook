# add a bit of fun to your prints/logs
# https://github.com/sepandhaghighi/art
from art import text2art, tprint


text = "wizbook"
font = "rand-xlarge"

# format then print
ascii_text = text2art(text, font)
print(ascii_text)

# dedicated printer func
tprint("art","white_bubble")
