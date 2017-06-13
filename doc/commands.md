# Commands

- [fetch-url](#fetch-url)
- [fetch-tweets](#fetch-tweets)
- [proc-clean](#proc-clean)
- [proc-lmtz](#proc-lmtz)
- [proc-stem](#proc-stem)
- [proc-tkn](#proc-tkn)
- [feat-tfidf](#feat-tfidf)

## fetch-url
Transfer URL content (like CURL)

```
usage: get_url.py [-h] [URL]

Transfer URL content

positional arguments:
  URL         URL to fetch

optional arguments:
  -h, --help  show this help message and exit
```

Example:
```bash
fetch-url https://jsonplaceholder.typicode.com/posts/1
```

# fetch-tweets
Stream or Search a set of Tweets with the Twitter API.

```
usage: get_raw_tweets.py [-h] --consumer_key CONSUMER_KEY --consumer_secret
                         CONSUMER_SECRET --access_token ACCESS_TOKEN
                         --access_token_secret ACCESS_TOKEN_SECRET
                         [--language LANGUAGE] [--latitude LATITUDE]
                         [--longitude LONGITUDE] [--count COUNT]
                         [--keywords KEYWORDS [KEYWORDS ...]]
                         [--enable-entities]

Search tweets with the Twitter API

optional arguments:
  -h, --help            show this help message and exit

  API Key Arguments

  --consumer_key CONSUMER_KEY
                        API Consumer Key
  --consumer_secret CONSUMER_SECRET
                        API Consumer Secret
  --access_token ACCESS_TOKEN
                        API Access Token
  --access_token_secret ACCESS_TOKEN_SECRET
                        API Token Secret

  Search Parameters

  --language LANGUAGE   Language of the Tweets
  --latitude LATITUDE   GEO: Latitude
  --longitude LONGITUDE
                        GEO: Longitude
  --count COUNT         Language of the Tweets
  --keywords KEYWORDS [KEYWORDS ...]
                        Keywords to search
  --enable-entities     Don't fetch the entities information
```
Example:
```bash

fetch-tweets

```

# proc-clean
Clean a text input with a variety of modes.

```bash
usage: proc-clean [-h] [--html] [--rules RULES_FILE]

Clean input text with regex rules

optional arguments:
  -h, --help          show this help message and exit
  --html              Remove html tags
  --rules RULES_FILE  Rules CSV file
```

Example:
```bash
fetch-url https://news.ycombinator.com/item?id=14336563 | proc-clean --html
```

# proc-lmtz
Lemmatize input (previously tokenized)

```bash
usage: proc-lmtz [-h] [--lang LANG]

Lemmatize input (previously tokenized)

optional arguments:
  -h, --help   show this help message and exit
  --lang LANG  Language (defalt: english): spanish, etc.
```

Example:
```bash
echo "books" | proc-lmtz
# book
```

# proc-stem
Apple the stemming process to the input data.

```bash
usage: proc-stem [-h] [--type TYPE] [--lang LANG]

Apply the stemming procees to the input (previously tokenized)

optional arguments:
  -h, --help   show this help message and exit
  --type TYPE  Stemming type: porter, lancaster, snowball
  --lang LANG  Language (defalt: english): spanish, etc.
```

Example:
```bash
echo "going" | proc-stem
# go
```

# proc-tkn
Tokenize input and results one token per line

```bash
usage: proc-tkn [-h] [--lang LANG]

Tokenize input and results one token per line

optional arguments:
  -h, --help   show this help message and exit
  --lang LANG  Language (defalt: english): spanish, etc.

```

Example:
```bash
echo "Hello world!" | proc-tkn
# Hello
# world
# !
```

# feat-tfidf
Calculate the basic text features: TF, IDF and TFIDF

```bash
usage: feat-tfidf [-h] [--type TYPE] [--sep SEP]

Calculate tfidf, tf and idf features from a list of words

optional arguments:
  -h, --help   show this help message and exit
  --type TYPE  Calculation type: tfidf, tf or idf (Default tfidf)
  --sep SEP    Document separator
```

Example:
```
echo "Roses are red. Violets are blue. Sugar is sweet. And so are you." \
  | proc-tkn \
  | prok-lmtz \
  | feat-tfidf --type idf --sep .

# Result
#
# and 4.0
# are 1.3333333333333333
# blue 4.0
# is 4.0
# red 4.0
# rose 4.0
# so 4.0
# sugar 4.0
# sweet 4.0
# violet 4.0
# you 4.0
```
