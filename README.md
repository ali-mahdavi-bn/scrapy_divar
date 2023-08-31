
# first step
find tokens

```python
python find_tokens/find_divar_tokens
```
copy address of tokens.txt to scrapy/divar/spider/divar_spaider 

# second step
```bash
scrapy crawl divar -o houe_prising.csv -t csv
```