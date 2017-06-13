#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from collections import Counter
import sys

def calculate_idf(word, all_sentences_counter):
    num_documents = len(all_sentences_counter)
    appearance_in_docs = 0
    for sentence in all_sentences_counter:
        if word in sentence:
            appearance_in_docs += 1

    return num_documents / appearance_in_docs

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='feat-tfidf', description='Calculate tfidf, tf and idf features from a list of words')
    parser.add_argument("--type", type=str, default='tfidf', help="Calculation type: tfidf, tf or idf (Default tfidf)")
    parser.add_argument("--sep", type=str, default=None, help="Document separator")

    args = parser.parse_args()

    all_sentences = []
    sentence = Counter()
    for line in sys.stdin:
        word = line[:-1].lower()

        if args.sep is not None and word.strip() == args.sep:
            all_sentences.append(sentence)
            sentence = Counter()
        else:
            sentence.update([word])

    if args.type == 'tf':
        for sentence in all_sentences:
            for word in sentence:
                print(word, sentence[word]/len(sentence))
    elif args.type == 'idf':
        dwords = sorted(list(set([item for sublist in [list(s.elements()) for s in all_sentences] for item in sublist])))
        for word in dwords:
            print(word, calculate_idf(word, all_sentences))
