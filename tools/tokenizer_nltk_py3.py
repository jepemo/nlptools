#!/usr/bin/env python

# -*- coding: utf8 -*-

import nltk
import fileinput

for line in fileinput.input():
    tokens = nltk.word_tokenize(line.decode('utf-8'), language='spanish')
    for t in tokens:
        print(t.encode('utf-8').strip())
