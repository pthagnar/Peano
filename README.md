# *Peano*
Set Theory and Beeping

## Mathematics

There is a bit of mathematical formalism about how to define numbers, from sound foundational principles. The usual method is set theory -- numbers are equivalent to sets, or sets of sets, a set being an object made of other objects grouped together in curly brackets: {x,y,z}.

The most basic set is the empty set, variously written {∅} or {}. This shares several properties, which we won't go into, with the number 0. Indeed, the cardinality, or number of members, of the empty set is 0, so we can say 0 = {∅}

If you make a set which contains the empty set, you get {{∅}}, or {{}}. The cardinality of this set is 1: it has one member, {∅}. If the empty set does well as be a definition of 0, this does well for 1 and so 1 = {0} = {{∅}}.

And then you can get 2 by having {0,1}, that is, { {∅}, {{∅}} }, cardinality 2.

3 is {0,1,2} = { {∅}, {{∅}}, {{∅},{{∅}}} } and so on. Keep doing this and you construct the natural numbers. This gets confusing quickly, especially if you leave the ∅s out, so 3 = {{},{{}},{{},{{}}}}

But there are other kinds of numbers: the two relevant ones for the purposes of this explanation are the integers: which extend the natural numbers to include negative numbers; and rational numbers, which are all the numbers you can get when you divide one natural number by another. Unsuprisingly perhaps, these can also be defined, or constructed set theoretically. Wikipedia is your friend here:

http://en.wikipedia.org/wiki/Integers#Construction

http://en.wikipedia.org/wiki/Rational_numbers#Formal_construction

## *Peano*

Suffice it to say, that if you write these things out, you get things like:

-5 = {{{{{}},{}},{{{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}},{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}}}}}}},{{{{{}}},{}},{{{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}},{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}}},{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}},{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}}}}}}}}}

and

¾ = {{{{{{{{{{},{{}},{{},{{}}}}},{}},{{{}}}},{{{{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}}}},{}},{{{{}}}}}}},{}},{{{{{{{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}}}},{}},{{{}}}},{{{{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}},{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}}}}},{}},{{{{}}}}}}}}},{{{{{{{{}},{}},{{{{},{{}},{{},{{}}}}}}},{{{{{}}},{}},{{{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}}}}}}}},{}},{{{{{{{}},{}},{{{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}}}}}},{{{{{}}},{}},{{{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}},{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}}}}}}}}}}}}

These have some interesting, if repetitive, structure to them and I wondered if they might sound nice. Suppose you go up an interval when you see a { and down one when you see a } (and, say, repeat the last note when you hit a comma)-- what would it sound like? The answer is produced by *Peano*, named after a mathematician who did work on this sort of thing, and which also sounds like the word 'piano'.

You can download it here. You will need numpy. Running it in linux, with the command line LAME encoder installed will also be a great help.

You feed it an integer or rational number (either between, or with numerators and denominators between -10 and 10, unless you modify it to take these safety locks off) and it produces an mp3 (all going well) of beeping noises. There are parameters you can twiddle with, including:

    How many intervals the octave is divided into (default: 12)
    What frequency it starts on (default: 110 Hz)
    How many semitones it moves by (default: 2 (1 is a little dull))
    Length of each tone (default: 0.2s)
    A series of bright organ beep tones (default: saworgan: odd harmonics of the sine, filtered exponentially to produce a sort of sawtooth effect) 

Typical output sounds like this: http://www.oligomath.co.uk/peano/peano--5-12TET-110Hz-2st-0.2s-saworgan.mp3

It is not unmusical.

I got the sine generation code from: http://codingmess.blogspot.co.uk/2008/07/how-to-make-simple-wav-file-with-python.html.
The bad additive synthesis is all my addition.

This is also hosted at http://www.oligomath.co.uk/peano/
