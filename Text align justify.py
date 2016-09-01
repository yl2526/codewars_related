# -*- coding: utf-8 -*-
"""
Description:

Your task in this Kata is to emulate text justification in monospace font. 
You will be given a single-lined text and the expected justification width. 
The longest word will never be greater than this width.

Here are the rules:

Use spaces to fill in the gaps between words.
Each line should contain as many words as possible.
Use '\n' to separate lines.
Gap between words can't differ by more than one space.
Lines should end with a word not a space.
'\n' is not included in the length of a line.
Large gaps go first, then smaller ones: 'Lorem---ipsum---dolor--sit--amet' (3, 3, 2, 2 spaces).
Last line should not be justified, use only one space between words.
Last line should not contain '\n'
Strings with one word do not need gaps ('somelongword\n').
Example with width=30:

Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.
Also you can always take a look at how justification works in your text editor 
or directly in HTML (css: text-align: justify).

Have fun :)
"""

def find_next(text, width):
    if width >= len(text):
        return text.strip(), None
    elif text[width] == ' ':
        return text[: width], text[(width + 1): ]
    else:
        for backspace, letter in enumerate(reversed(text[: width])):
            if letter == ' ':
                return text[: (width - backspace - 1)], text[(width - backspace): ]

def pad_line(line, width):
    words = line.split(' ')
    if len(words) == 1:
        return words[0]
    total_spaces_needed = width - sum(map(len, words))
    
    space_size = total_spaces_needed // (len(words) - 1)
    bigger_total_spaces_needed = total_spaces_needed % (len(words) - 1)
    spaces = [space_size + int(nth < bigger_total_spaces_needed) for nth in range(len(words) - 1)]
    spaces.append(0)
    
    return ''.join(w + ' ' * s for w, s in zip(words, spaces))

def justify(text, width):
    padded_text = ''
    while text:
        line, text = find_next(text, width)
        if text:
            padded_text += pad_line(line, width) + '\n'
        else:
            padded_text += line
    return padded_text

justify('123 45 6', 7)


text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.'
p = justify(text, 15)


# solution form bennieswart
def justify(text, width):
    length = text.rfind(' ', 0, width+1)  # rfind !!!
    if length == -1 or len(text) <= width: return text
    line = text[:length]
    spaces = line.count(' ')
    if spaces != 0:
        expand = (width - length) / spaces + 1
        extra = (width - length) % spaces
        line = line.replace(' ', ' '*expand)
        line = line.replace(' '*expand, ' '*(expand+1), extra)
    return line + '\n' + justify(text[length+1:], width)






