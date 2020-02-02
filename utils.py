from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import os
import sys

BASE_URL = 'https://atcoder.jp/contests'
ABC_URL = 'https://atcoder.jp/contests/archive?ratedType=1&category=0&keyword='

options = Options()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

def validate_type(contest_type):
  if type(contest_type) is not str:
    return False
  contest_type = contest_type.upper()
  if contest_type != 'ABC':
    return False
  else: 
    return True
  
def validate_num(contest_num, MAX_NUM, MIN_NUM):
  if type(contest_num) is not int:
    contest_num = int(contest_num)
  if contest_num < MIN_NUM or MAX_NUM < contest_num:
    return False
  else:
    return True
  
def validate_task(task):
  if type(task) is not str:
    return False

  if type(task) is str and len(task) == 1:
    return True
  return False

def validate(contest_type, contest_num, task, MAX_NUM, MIN_NUM):
  is_all_element_true = False
  validate_result = []
  validate_result.append(validate_type(contest_type))
  validate_result.append(validate_num(contest_num, MAX_NUM, MIN_NUM))
  validate_result.append(validate_task(task))

  if (validate_result[0] == True) and (validate_result[1] == True) and (validate_result[2] == True):
    is_all_element_true = True

  if len(validate_result) == 3 and is_all_element_true:
    return True
  
  return False

def check_task(contest_num, task):
  task_41to125 = ['a', 'b', 'c', 'd']
  task_126tolatest = task_41to125 + ['e', 'f']

  if contest_num > 125:
    if task in task_126tolatest:
      return True
  else:
    if task in task_41to125:
      return True
      
  return False

def shape_type(contest_type):
  return contest_type.upper()

def shape_num(num):
  num = int(num)
  if 10 < num < 100:
    num = '0' + str(num)
  elif 0 < num < 10:
    num = '00' + str(number)
  return num

def shape_task(task):
  return task.upper()

def shape_val(contest_type, contest_num, task):
  shaped_val = []
  shaped_type = shape_type(contest_type)
  shaped_num = shape_num(contest_num)
  shaped_task = shape_task(task)
  shaped_val.append(shaped_type)
  shaped_val.append(shaped_num)
  shaped_val.append(shaped_task)
  return shaped_val

def generate_dir(contest_type, contest_num, task):
  shaped_val = shape_val(contest_type, contest_num, task)

  path = f'./{shaped_val[0]}/{shaped_val[1]}/{shaped_val[2]}'
  os.makedirs(path, exist_ok=True)

def generate_python_file(title, contest_type, contest_num, task):
  shaped_val = shape_val(contest_type, contest_num, task)

  target_dir = f'./{shaped_val[0]}/{shaped_val[1]}/{shaped_val[2]}'
  text = f'import os\nimport sys\nf = open("{title}_1.txt", "r")\nsys.stdin = f\n\n#この下にコードを記述\n'
  with open(f'{target_dir}/{title}.py', 'w') as f:
    f.write(text)

def generate_input_file(input_content, title, index, contest_type, contest_num, task):
  shaped_val = shape_val(contest_type, contest_num, task)

  target_dir = f'./{shaped_val[0]}/{shaped_val[1]}/{shaped_val[2]}'
  with open(f'{target_dir}/{title}_{index}.txt', 'w') as f:
    f.write(input_content)

#最新のABCのナンバーを取得する
def get_content_max(ABC_URL):
  driver.get(ABC_URL)
  ABC_max_element = driver.find_elements_by_css_selector('#main-container > div.row > div.col-lg-9.col-md-8 > div.panel.panel-default > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')
  ABC_max = ABC_max_element[0].text.split(' ')[3]
  return int(ABC_max)

def generate_task_url(contest_type, contest_num, task):
  lowered_type = contest_type.lower()
  shaped_contest_num = shape_num(contest_num)
  lowered_task = task.lower()
  return f'{BASE_URL}/{lowered_type}{shaped_contest_num}/tasks/{lowered_type}{shaped_contest_num}_{task}'