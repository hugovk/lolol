#!/usr/bin/env python
"""
Replace every "lo" in Project Gutenberg with a "lol".
Usage:
gutengrep.py -i "\blo\b" "*.txt" --cache --sort --correct -o /tmp/lolol.txt
    --andnext --language en
lolol.py lolol-sort.txt  > lolol.md
multimarkdown lolol.md > lolol.html && lolol.html
"""
from __future__ import print_function, unicode_literals
import fileinput
import re

CHARS = "\`*_{}[]()>#+-.!$"


def front():
    front_matter = [
        "Title:          lolol\n"
        "CSS:            lolol.css\n"
        "HTML Header:    <link rel='stylesheet' type='text/css' href='https://fonts.googleapis.com/css?family=Gentium+Book+Basic:400,700,400italic'>",
        "",
        'lo<span class="lol">lol</span>',
        "=====",
        "*<center>or</center>*",
        'ol the <span class="lol">lol</span>s',
        "-----------",
        "*<center>or</center>*",
        "The Big Jolly Book of Humorous Observations",
        "-----------------------------------------------------",
        "",
        '<p class="author">lo<span class="lol">lol</span>.py</p>',
        "",
        '<p class="auth-desc">for NaNoGenMo 2014</p>',
        "",
        '<p class="source">source code at https://github.com/hugovk/lo<span class="lol">lol</span></p>',
        "",
    ]
    print("\n".join(front_matter))


if __name__ == '__main__':
    front()

    print("### Chapter 1\n")
    for line in fileinput.input():
    # for i, line in enumerate(fileinput.input()):
        # if i % 120 == 0:
            # print("### Chapter " + str(i+1) + "\n")
        line = line.decode('utf-8-sig').rstrip()  # No BOM
        for c in CHARS:
            if c in line:
                line = line.replace(c, '\\' + c)

        # lo -> *lol*
        line = re.sub(r"\blo\b", '<span class="lol">lol</span>', line)
        line = re.sub(r'\bLO\b', '<span class="lol">LOL</span>', line)
        line = re.sub(r'\bLo\b', '<span class="lol">Lol</span>', line)

        print(line.encode('utf-8'))

# End of file
