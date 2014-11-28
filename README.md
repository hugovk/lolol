lolol
=====

*or*

ol the lols
-----

*or*

The Big Jolly Book of Humorous Observations
-------------------------------------------

 * [PDF](https://hugovk.github.io/lolol/lolol.pdf) | 
[HTML](https://hugovk.github.io/lolol/lolol.html) | 
[MD](https://github.com/hugovk/lolol/blob/gh-pages/lolol.md) | (103,915 words)

In the [Project Gutenberg CD corpus of 600 books](http://www.gutenberg.org/wiki/Gutenberg:The_CD_and_DVD_Project), find every English sentence containing the word **lo** – but also include the next sentence because the parser sometimes breaks things like "**lo!** and behold" into two.

Then replace each **lo** with **lol**.

    gutengrep.py -i "\blo\b" "*.txt" --cache --sort --correct -o /tmp/lolol.txt --andnext --language en
    lolol.py lolol-sort.txt  > lolol.md
    multimarkdown lolol.md > lolol.html && lolol.html

Uses [gutengrep.py](https://github.com/hugovk/gutengrep).

Then print to PDF using Chrome. Big thanks to [@moonmilk for the CSS](https://github.com/moonmilk/nanogenmo2014).
