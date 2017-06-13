#!/usr/bin/env python
# -*- coding: utf8 -*-

import argparse
import sys
from nltk.stem import WordNetLemmatizer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='proc-lmtz', description='Lemmatize input (previously tokenized)')
    parser.add_argument("--lang", type=str, default='english', help="Language (defalt: english): spanish, etc.")

    args = parser.parse_args()

    wordnet_lemmatizer = WordNetLemmatizer()
    for line in sys.stdin:
        print(wordnet_lemmatizer.lemmatize(line.strip()))
