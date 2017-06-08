#!/usr/bin/env python

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='proc-clean', description='Clean input text with regex rules')
    parser.add_argument("--html", dest="html", action="store_true", help="Remove html tags")
    parser.add_argument("--rules", dest="rules_file", action="store", help="Rules CSV file")
    args = parser.parse_args()

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
