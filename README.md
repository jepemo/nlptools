 # nlptools
*nlptools* are an Unix inspired utilities for Natural Language Processing.

- [Examples](#examples)
  - [Basic tokenization](#basic-tokenization)
  - [Lemmatization and Stemming](#lemmatization-and-stemming)
  - [Basic features](#basic-features)
  - [Data fetching](#data-fetching)
- [Documentation](#documentation)
  - [Commands](#commands)
  - [Cookbook](#cookbook)

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

### Lemmatization and Stemming

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
  | proc-lmtz \
  | feat-tfidf --type idf --sep .

# Result
#
# and 0.0 0.0 0.0 1.0
# are 0.4444444444444444 0.4444444444444444 0.0 0.3333333333333333
# blue 0.0 1.3333333333333333 0.0 0.0
# is 0.0 0.0 1.3333333333333333 0.0
# red 1.3333333333333333 0.0 0.0 0.0
# roses 1.3333333333333333 0.0 0.0 0.0
# so 0.0 0.0 0.0 1.0
# sugar 0.0 0.0 1.3333333333333333 0.0
# sweet 0.0 0.0 1.3333333333333333 0.0
# violets 0.0 1.3333333333333333 0.0 0.0
# you 0.0 0.0 0.0 1.0
```

### Data fetching
```bash
fetch-url https://www.gutenberg.org/files/996/old/1donq10.txt \
  | proc-tkn \
  | sort \
  | uniq -c

# Result
#
#   5312 ``
#      1 ~
#      1 <
#      1 =
#      1 >
#      1 _
#     40 -
#  36793 ,
#   6057 ;
#    370 :
#    677 !
#    970 ?
#      1 /
#   7723 .
#      1 ...
#    503 '
#      1 '-
#   5222 ''
#    209 (
#    209 )
#     20 [
#     20 ]
#    .....
```

## Documentation

### [Commands](doc/commands.md)
### [CookBook](doc/cookbook.md)
