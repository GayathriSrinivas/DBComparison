#! /usr/bin/python

import sys
from random import randint, choice
from string import ascii_lowercase, digits

num_words = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
input_file = "input_data.txt"
with open(input_file, 'w') as f:
    for i in range(num_words):
        length = randint(5, 50)
        random_str = ''.join(choice(ascii_lowercase + digits) for _ in range(length))
        f.write(random_str)
        f.write("\n")
