# Commands

- [fetch-url](#fetch-url)
- [fetch-tweets](#fetch-tweets)
- [proc-clean](#proc-clean)

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
usage: cleaner.py [-h] [--html] [--rules RULES_FILE]

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
