from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import threading
import time


# Option 1 - with ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox') 
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=chrome_options)
  
#Functionality
time.sleep(2)
driver.get('https://ampdemo.azureedge.net/azuremediaplayer.html?url=%2F%2Famssamples.streaming.mediaservices.windows.net%2F49b57c87-f5f3-48b3-ba22-c55cfdffa9cb%2FSintel.ism%2Fmanifest&muted=true&aes=true&wallClockDisplayEnabled=true&useLocalTimeZone=true') 
print(driver.title)

time.sleep(2)

Number = 50
thread_list = list()

# Testing begins
for i in range(Number):
    t = threading.Thread(name='Test {}'.format(i))
    t.start()
    time.sleep(1)
    print(t.name + ' started!')
    thread_list.append(t)

# Wait for all thre<ads to complete
for thread in thread_list:
    thread.join()

print('Testing is ready and done')




