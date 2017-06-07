#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Apply the stemming procees to the input (previously tokenized)')
    parser.add_argument("--type", type=str, default='porter', help="Stemming type: porter, lancaster, snowball")
    parser.add_argument("--lang", type=str, default='english', help="Language (defalt: english): spanish, etc.")

    args = parser.parse_args()

    for line in fileinput.input():
        stemmer = None
        if args.type == "porter":
            from nltk.stem.lancaster import LancasterStemmer
            stemmer = PorterStemmer()
        elif args.type == "lancaster":
            from nltk.stem.lancaster import LancasterStemmer
            stemmer = LancasterStemmer()
        elif args.type == "snowball":
            from nltk.stem import SnowballStemmer
            stemmer = SnowballStemmer(args.lang)

        if stemmer is None:
            print("Invalid stemmer type")
            sys.exit(1)

        print(stemmer.stem(line.strip()))
