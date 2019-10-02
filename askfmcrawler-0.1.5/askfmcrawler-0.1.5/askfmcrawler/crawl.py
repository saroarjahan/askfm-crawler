import time
from askfmcrawler.entities import User, Article
from selenium.common.exceptions import NoSuchElementException


class Crawler:

    def __init__(self, driver):
        self.driver = driver

    def crawl_user_questions(self, name, limit=1000):
        username = name

        url = f"https://ask.fm/{username}"
        self.driver.get(url)

        for _ in range(limit):
            previous_h = self.driver.execute_script("var h = window.pageYOffset; return h")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            after_h = self.driver.execute_script("var h = window.pageYOffset; return h")
            if previous_h == after_h:
                break

        user_id = self.driver.find_elements_by_css_selector('.userName')[0].text
        user_name = self.driver.find_elements_by_css_selector('.userName')[1].text

        user = User(user_id, user_name)

        articles = []

        for article in self.driver.find_elements_by_tag_name('article'):
            article_id = article.find_element_by_css_selector('.streamItem_meta').get_attribute('href').split('/')[-1]
            question = article.find_element_by_tag_name('h2').text
            try:
                answer = article.find_element_by_css_selector('.streamItem_content').text
            except NoSuchElementException:
                # Image only
                answer = ''

            articles.append(Article(article_id, user, question, answer))

        return articles

    def crawl_random_users(self):
        url = "https://ask.fm/"
        self.driver.get(url)
        faces = self.driver.find_element_by_css_selector('.faces')
        users = [face.text for face in faces.find_elements_by_tag_name('a')]
        return users
