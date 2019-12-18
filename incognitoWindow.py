from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import threading
import time

def test_logic():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--no-sandbox') 
    browser = webdriver.Chrome(executable_path= "C:\\Program files (x86)\\ChromeDriver\\chromedriver.exe", chrome_options=options)
    browser.get('https://ampdemo.azureedge.net/azuremediaplayer.html?url=%2F%2Famssamples.streaming.mediaservices.windows.net%2F49b57c87-f5f3-48b3-ba22-c55cfdffa9cb%2FSintel.ism%2Fmanifest&muted=true&aes=true&wallClockDisplayEnabled=true&useLocalTimeZone=true')
    
    time.sleep(200)
    browser.quit()

Number = 20   # Number of browsers to be open
thread_list = list()

# Testing begins
for i in range(Number):
    t = threading.Thread(name='Test {}'.format(i), target=test_logic)
    t.start()
    time.sleep(1)
    print(t.name + ' started!')
    thread_list.append(t)

# Wait for all thre<ads to complete
for thread in thread_list:
    thread.join()

print('Testing is ready and done')



