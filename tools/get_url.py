#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("get_url <URL>")
        sys.exit(0)

    url = sys.argv[1]

    if not uri_validator(url):
        print("Url:", url, "not valid")
        sys.exit(1)

    with urllib.request.urlopen(url) as f:
        data = f.read()
        enc_result = chardet.detect(data)
        print(data.decode(enc_result['encoding']))