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
import chardet
import sys
import urllib.request
from urllib.parse import urlparse

def uri_validator(x):
    try:
        result = urlparse(x)
        return True if [result.scheme, result.netloc, result.path] else False
    except:
        return False

def main(argv=None):
    parser = argparse.ArgumentParser(description='Transfer URL content')
    parser.add_argument("url", metavar="URL", type=str, nargs="?", help="URL to fetch")

    args = parser.parse_args(argv)

    url = args.url

    # if len(sys.argv) != 2:
    #     parser.print_help()
    #     # print("get_url <URL>")
    #     sys.exit(0)

    url = sys.argv[1]

    if not uri_validator(url):
        print("Url:", url, "not valid")
        sys.exit(1)

    with urllib.request.urlopen(url) as f:
        data = f.read()
        enc_result = chardet.detect(data)
        print(data.decode(enc_result['encoding']))
