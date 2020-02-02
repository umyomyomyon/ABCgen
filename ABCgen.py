from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

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
contest_num = 54
task = 'b'

#引数が正しいか検証する
validate_result = validate(contest_type, contest_num, task, MAX_NUM, MIN_NUM)
if validate_result == False:
  print('failed.')
  sys.exit()

#contest_numとtaskの組み合わせが正しいか確認する
if check_task(contest_num, task) == False:
  print('task is not correct.')
  sys.exit()

#対象のディレクトリを生成する
generate_dir(contest_type, contest_num, task)
#問題が記載されているページのURLを生成する
task_url = generate_task_url(contest_type, contest_num, task)
print(task_url)
driver.get(task_url)

#copyボタンの数から入出力例の数を決定する
copy_btn_element = driver.find_elements_by_class_name('div-btn-copy')
sample_qty = len(copy_btn_element) // 4

#入力例をリストに加える
input_list = []
for i in range(0, sample_qty * 2, 2):
  target = driver.find_element_by_id(f'pre-sample{i}').get_attribute('textContent')
  input_list.append(target)
  print(target)

driver.quit()