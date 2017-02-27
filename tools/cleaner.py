#!/usr/bin/env python

import re, csv, sys, argparse

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
    parser = argparse.ArgumentParser(description='Clean input text with regex rules')
    parser.add_argument("--debug", dest="debug_mode", action="store_true", help="Active debug mode")
    parser.add_argument("--rules", dest="rules_file", action="store", help="Rules CSV file")
    args = parser.parse_args()

    if (args.rules_file is None):
        parser.print_help()
    else:
        rules = load_rules(args.rules_file)
        for line in sys.stdin:
            line = line
            if args.debug_mode:
                sys.stderr.write("TO_CLEAN: %s" % (line))
            if line is not None:
                result = line.lower()
                for regex, repl in rules.items():
                    result = regex.sub(repl, result)
                print(result)
