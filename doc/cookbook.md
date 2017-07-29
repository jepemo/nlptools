# CookBook

## Ten most common words in the Quixote

```bash
fetch-url https://www.gutenberg.org/files/996/old/1donq10.txt \
  | bin/proc-tkn \
  | sort \
  | uniq -c \
  | sort -nr \
  | head
```
