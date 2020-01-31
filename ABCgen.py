from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

import re

from utils import *

BASE_URL = 'https://atcoder.jp/contests'
ABC_URL = 'https://atcoder.jp/contests/archive?ratedType=1&category=0&keyword='
MIN_NUM = 41

# ブラウザーを起動
options = Options()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

MAX_NUM = get_content_max(ABC_URL)

contest_type = 'abc'
contest_num = 56
task = 'b'

validate = validate(contest_type, contest_num, task, MAX_NUM, MIN_NUM)

tasks_url = generate_tasks_url(contest_type, contest_num)


contest_type = shape_type(contest_type)
contest_num = shape_num(contest_num)
task = shape_task(task)

generate_dir(contest_type, contest_num, task)

print(tasks_url)