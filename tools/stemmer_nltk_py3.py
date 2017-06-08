#!/usr/bin/env python
# -*- coding: utf8 -*-

import argparse
import fileinput
import sys

def get_stemmer(stype, lang):
    stemmer = None
    if stype == "porter":
        from nltk.stem.porter import PorterStemmer
        stemmer = PorterStemmer()
    elif stype == "lancaster":
        from nltk.stem.lancaster import LancasterStemmer
        stemmer = LancasterStemmer()
    elif stype == "snowball":
        from nltk.stem import SnowballStemmer
        stemmer = SnowballStemmer(lang)

    return stemmer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='proc-stem', description='Apply the stemming procees to the input (previously tokenized)')
    parser.add_argument("--type", type=str, default='porter', help="Stemming type: porter, lancaster, snowball")
    parser.add_argument("--lang", type=str, default='english', help="Language (defalt: english): spanish, etc.")

    args = parser.parse_args()

    stemmer = get_stemmer(args.type, args.lang)
    if stemmer is None:
        print("Invalid stemmer type")
        sys.exit(1)

    for line in fileinput.input():
        print(stemmer.stem(line.strip()))
