 nlptools
*nlptools* are an Unix inspired utilities for Natural Language Processing.

## Examples

### Basic tokenization

```bash
echo "Hello world!" | proc-tkn

# Result:
#
# Hello
# world
# !
```

### Lemmatization & Stemming

```bash
echo "dog dogs" | bin/proc-tkn | bin/proc-lmtz

# Result:
#
# dog
# dog
```

### Basic features

```bash
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

## Documentation

* [Commands](doc/commands.md)
