#!/usr/bin/env python
# -*- coding: utf8 -*-

from nltk.stem import WordNetLemmatizer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lemmatize input (previously tokenized)')
    parser.add_argument("--lang", type=str, default='english', help="Language (defalt: english): spanish, etc.")

    args = parser.parse_args()

    for line in fileinput.input():
        wordnet_lemmatizer = WordNetLemmatizer()
        print(wordnet_lemmatizer.lemmatize(line.strip()))
