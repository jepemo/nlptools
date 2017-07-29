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

def main(argv=None):
    parser = argparse.ArgumentParser(prog='proc-stem', description='Apply the stemming procees to the input (previously tokenized)')
    parser.add_argument("--type", type=str, default='porter', help="Stemming type: porter, lancaster, snowball")
    parser.add_argument("--lang", type=str, default='english', help="Language (defalt: english): spanish, etc.")

    args = parser.parse_args(argv)

    stemmer = get_stemmer(args.type, args.lang)
    if stemmer is None:
        print("Invalid stemmer type")
        sys.exit(1)

    for line in sys.stdin:
        print(stemmer.stem(line.strip()))
