# askfmcrawler
[![PyPI Version](https://img.shields.io/pypi/v/askfmcrawler.svg)](https://pypi.python.org/pypi/askfmcrawler)
Python askfm crawler.


## Install
```
pipenv install askfmcrawler
```

## Requirements
- Python 3.6 or higher
- selenium

## Usage
```python
from selenium import webdriver

from askfmcrawler import Crawler

driver = webdriver.Chrome('./chromedriver')

crawler = Crawler(driver)

# Crawl user questions
for article in crawler.crawl_user_questions('uehara1414test', limit=20):
    print(article.question, " => ", article.answer)

# 好きなデザートは？ => ガトーショコラ
# 赤信号なのに道路を渡ることはある？ => ある
# ...

# Get random users and crawl questions of them
for user in crawler.crawl_random_users():
    for article in crawler.crawl_user_questions(user):
        print(user, article.question, " => ", article.answer)

driver.quit()
```

## Test
### Setup
- Install requiremnts with `pipenv install --dev`
- Place chromedriver to project root

### Run tests
```sh
pipenv run nosetests
```
