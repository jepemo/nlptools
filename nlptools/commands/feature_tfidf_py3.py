# -*- coding: utf-8 -*-
# nlptools - Unix inspired utilities for Natural Language Processing.
#
# Copyright (C) 2017-present Jeremies Pérez Morata
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

def calculate_tf(word, sentence):
    if word not in sentence:
        return 0.0
    return sentence[word]/len(sentence)

def calculate_tfidf(word, sentence, all_sentences):
    tf = calculate_tf(word, sentence)
    idf = calculate_idf(word, all_sentences)
    return tf * idf

def main(argv=None):
    parser = argparse.ArgumentParser(prog='feat-tfidf', description='Calculate tfidf, tf and idf features from a list of words')
    parser.add_argument("--type", type=str, default='tfidf', help="Calculation type: tfidf, tf or idf (Default tfidf)")
    parser.add_argument("--sep", type=str, default=None, help="Document separator")
    parser.add_argument("--inv", dest="inverse", action="store_true", help="Show inverse output")

    args = parser.parse_args(argv)

    all_sentences = []
    sentence = Counter()
    for line in sys.stdin:
        word = line[:-1].lower()

        if args.sep is not None and word.strip() == args.sep:
            all_sentences.append(sentence)
            sentence = Counter()
        else:
            sentence.update([word])

    dwords = sorted(list(set([item for sublist in [list(s.elements()) for s in all_sentences] for item in sublist])))
    if args.inverse:
        ind=0
        for word in dwords:
            print(word, end=' ')
        print('')

        for sent in all_sentences:
            for word in dwords:
                result = 0.0
                if args.type == 'tf':
                    result = calculate_tf(word, sent)
                elif args.type == 'idf':
                    result = calculate_idf(word, all_sentences)
                elif args.type == 'tfidf':
                    result = calculate_tfidf(word, sent, all_sentences)

                print(str(result) + " ", end='')
            print('')
    else:
        for word in dwords:
            print(word + " ", end='')
            for sent in all_sentences:
                result = 0.0
                if args.type == 'tf':
                    result = calculate_tf(word, sent)
                elif args.type == 'idf':
                    result = calculate_idf(word, all_sentences)
                elif args.type == 'tfidf':
                    result = calculate_tfidf(word, sent, all_sentences)

                print(str(result) + " ", end='')

            print('')
