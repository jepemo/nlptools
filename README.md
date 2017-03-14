# nlptools
*nlptools* are an Unix inspired utilities for Natural Language Processing.

## Example

```bash
echo "Hello world!" | proc-tkn
```

Result:

```
Hello
world
!
```

## Commands

- [fetch-url](#fetch-url)
- [fetch-tweets](#fetch-tweets)

### fetch-url
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
```
fetch-url https://jsonplaceholder.typicode.com/posts/1
```

## fetch-tweets
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
```
```
