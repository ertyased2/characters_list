from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random
WIDTH = 1296
HEIGHT = 1032
Steps = 20
prompt = "Input your "
negative_prompt = " "


is_random = True
char_am = 2
picture_to_generate = 50

browser = webdriver.Edge()
browser.get("http://127.0.0.1:7860")
sleep(10)
elems = browser.find_elements(By.CLASS_NAME, "svelte-1cl284s")

browser.execute_script(f"arguments[0].value = ''", elems[2])
elems[2].send_keys(Steps)
browser.execute_script(f"arguments[0].value = ''", elems[30])
elems[30].send_keys(WIDTH)
browser.execute_script(f"arguments[0].value = ''", elems[34])
elems[34].send_keys(HEIGHT)
f = open('characters.txt','r')
chars = f.readlines()
elems = browser.find_elements(By.CLASS_NAME, "svelte-1f354aw")
browser.execute_script(f"arguments[0].value = ''", elems[3])
elems[3].send_keys(negative_prompt)
generate_button = browser.find_element(By.CLASS_NAME, "generate-box")
skip_buttons = browser.find_elements(By.CLASS_NAME, "generate-box-skip")
if not is_random:
    for char in chars:
        browser.execute_script(f"arguments[0].value = ''", elems[1])
        elems[1].send_keys(prompt + " " + char)
        sleep(5)
        generate_button.click()

        while skip_buttons[0].is_displayed():
            continue
else:
    for _ in range(picture_to_generate):
        char = ""
        for i in range(char_am):
            char += "(" + random.choice(chars)[:-1] + ")" + ","
        print(char)
        browser.execute_script(f"arguments[0].value = ''", elems[1])
        elems[1].send_keys(prompt + " " + char)
        sleep(8)
        generate_button.click()
        while skip_buttons[0].is_displayed():
            continue

sleep(20)
browser.stop_client()
