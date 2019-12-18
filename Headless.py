from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import threading
import time

def selenium_drivers():
    options = Options()
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    url = 'https://ampdemo.azureedge.net/azuremediaplayer.html?url=%2F%2Famssamples.streaming.mediaservices.windows.net%2F49b57c87-f5f3-48b3-ba22-c55cfdffa9cb%2FSintel.ism%2Fmanifest&muted=true&aes=true&wallClockDisplayEnabled=true&useLocalTimeZone=true'
    driver.get(url)
    
    time.sleep(300)
    driver.quit()

Nubmer = 19   # Number of browsers to be open
thread_list = list()

# Testing begins
for i in range(Nubmer):
    t = threading.Thread(name='Test {}'.format(i), target=selenium_drivers)
    t.start()
    time.sleep(1)
    print(t.name + ' started!')
    thread_list.append(t)

# Wait for all thre<ads to complete
for thread in thread_list:
    thread.join()

print('The test is already done')
