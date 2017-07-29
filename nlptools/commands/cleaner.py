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

import re
import csv
import sys
import argparse
from bs4 import BeautifulSoup

def load_rules (filepath):
    rules = {}
    with open(filepath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in csvreader:
            regex = re.compile(row[0])
            repl  = row[1]
            rules[regex] = repl

    return rules


def main(argv=None):
    parser = argparse.ArgumentParser(prog='proc-clean', description='Clean input text with regex rules')
    parser.add_argument("--html", dest="html", action="store_true", help="Remove html tags")
    parser.add_argument("--rules", dest="rules_file", action="store", help="Rules CSV file")
    args = parser.parse_args(argv)

    if (args.html):
        for line in sys.stdin:
            soup = BeautifulSoup(line, 'html.parser')
            print(soup.text)
    elif (args.rules_file is None):
        parser.print_help()
    else:
        rules = load_rules(args.rules_file)
        for line in sys.stdin:
            line = line
            if line is not None:
                result = line.lower()
                for regex, repl in rules.items():
                    result = regex.sub(repl, result)
                print(result)
