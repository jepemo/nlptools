#!/usr/bin/env python
# -*- coding: utf8 -*-

import argparse
import fileinput
import nltk


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tokenize input and results one token per line')
    parser.add_argument("--lang", type=str, default='english', help="Language (defalt: english): spanish, etc.")

    args = parser.parse_args()

    for line in fileinput.input():
        # tokens = nltk.word_tokenize(line.decode('utf-8'), language=args.lang)
        tokens = nltk.word_tokenize(line, language=args.lang)
        for t in tokens:
            # print(t.encode('utf-8').strip())
            print(t.strip())
