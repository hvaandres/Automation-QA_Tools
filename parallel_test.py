import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions() 
 
class ChromeSearch(unittest.TestCase):
 
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=chrome_options)
        self.driver.maximize_window()
    
    # We will need to verify that our browser is working
    def test_search_lambdatest_chrome(self):
        driver_chrome = self.driver
        driver_chrome.get('http://www.google.com')
        time.sleep(10)
 
        search_criteria = driver_chrome.find_element_by_name("q") # Search Bar
        search_criteria.clear()
        search_criteria.send_keys("Test") # Will type Test on the Search Bar
 
        # Check if the search returns any result
        assert "No results found." not in driver_chrome.page_source
 
        search_criteria.submit()
        print("Browser is working at 100%") #Confirm that the browser is working right
        time.sleep(10)

        

        driver_chrome.get("https://ampdemo.azureedge.net/azuremediaplayer.html?url=%2F%2Famssamples.streaming.mediaservices.windows.net%2F49b57c87-f5f3-48b3-ba22-c55cfdffa9cb%2FSintel.ism%2Fmanifest&muted=true&aes=true")
        print("Initial Page Title is : %s" %driver_chrome.title)
        windows_before  = driver_chrome.current_window_handle
        print("First Window Handle is : %s" %windows_before)
        driver_chrome.execute_script("window.open('https://ampdemo.azureedge.net/azuremediaplayer.html?url=%2F%2Famssamples.streaming.mediaservices.windows.net%2F49b57c87-f5f3-48b3-ba22-c55cfdffa9cb%2FSintel.ism%2Fmanifest&muted=true&aes=true')")
        WebDriverWait(driver_chrome, 10).until(EC.number_of_windows_to_be(2))
        driver_chrome.execute_script("window.open('https://ampdemo.azureedge.net/azuremediaplayer.html?url=%2F%2Famssamples.streaming.mediaservices.windows.net%2F49b57c87-f5f3-48b3-ba22-c55cfdffa9cb%2FSintel.ism%2Fmanifest&muted=true&aes=true')")
        WebDriverWait(driver_chrome, 10).until(EC.number_of_windows_to_be(3))
        driver_chrome.execute_script("window.open('https://ampdemo.azureedge.net/azuremediaplayer.html?url=%2F%2Famssamples.streaming.mediaservices.windows.net%2F49b57c87-f5f3-48b3-ba22-c55cfdffa9cb%2FSintel.ism%2Fmanifest&muted=true&aes=true')")
        WebDriverWait(driver_chrome, 10).until(EC.number_of_windows_to_be(4))
        driver_chrome.execute_script("window.open('https://ampdemo.azureedge.net/azuremediaplayer.html?url=%2F%2Famssamples.streaming.mediaservices.windows.net%2F49b57c87-f5f3-48b3-ba22-c55cfdffa9cb%2FSintel.ism%2Fmanifest&muted=true&aes=true')")
        WebDriverWait(driver_chrome, 10).until(EC.number_of_windows_to_be(5))
        driver_chrome.execute_script("window.open('https://ampdemo.azureedge.net/azuremediaplayer.html?url=%2F%2Famssamples.streaming.mediaservices.windows.net%2F49b57c87-f5f3-48b3-ba22-c55cfdffa9cb%2FSintel.ism%2Fmanifest&muted=true&aes=true')")
        WebDriverWait(driver_chrome, 10).until(EC.number_of_windows_to_be(6))
        driver_chrome.execute_script("window.open('https://ampdemo.azureedge.net/azuremediaplayer.html?url=%2F%2Famssamples.streaming.mediaservices.windows.net%2F49b57c87-f5f3-48b3-ba22-c55cfdffa9cb%2FSintel.ism%2Fmanifest&muted=true&aes=true')")
        WebDriverWait(driver_chrome, 10).until(EC.number_of_windows_to_be(7))
        driver_chrome.execute_script("window.open('https://ampdemo.azureedge.net/azuremediaplayer.html?url=%2F%2Famssamples.streaming.mediaservices.windows.net%2F49b57c87-f5f3-48b3-ba22-c55cfdffa9cb%2FSintel.ism%2Fmanifest&muted=true&aes=true')")
        WebDriverWait(driver_chrome, 10).until(EC.number_of_windows_to_be(8))
        driver_chrome.execute_script("window.open('https://ampdemo.azureedge.net/azuremediaplayer.html?url=%2F%2Famssamples.streaming.mediaservices.windows.net%2F49b57c87-f5f3-48b3-ba22-c55cfdffa9cb%2FSintel.ism%2Fmanifest&muted=true&aes=true')")
        WebDriverWait(driver_chrome, 10).until(EC.number_of_windows_to_be(9))
        driver_chrome.execute_script("window.open('https://ampdemo.azureedge.net/azuremediaplayer.html?url=%2F%2Famssamples.streaming.mediaservices.windows.net%2F49b57c87-f5f3-48b3-ba22-c55cfdffa9cb%2FSintel.ism%2Fmanifest&muted=true&aes=true')")
        WebDriverWait(driver_chrome, 10).until(EC.number_of_windows_to_be(10))
        windows_after = driver_chrome.window_handles
        new_window = [x for x in windows_after if x != windows_before][0]
        driver_chrome.switch_to_window(new_window)
        print("Page Title after Tab Switching is : %s" %driver_chrome.title)
        print("Second Window Handle is : %s" %new_window)

        time.sleep(200)

   # Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        # Close the browser. 
        self.driver.close()
 
if __name__ == "__main__":
    unittest.main() 



''' 
class FirefoxSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
        self.driver.maximize_window()
    
    # As per unittest module, individual test should start with test_
    def test_search_lambdatest_firefox(self):
        driver_firefox = self.driver
        driver_firefox.get('http://www.google.com')
        time.sleep(10)
 
        search_criteria = driver_firefox.find_element_by_name("q")
        search_criteria.clear()
        search_criteria.send_keys("Lambda Test")
 
        # Check if the search returns any result
        assert "No results found." not in driver_firefox.page_source
 
        search_criteria.submit()
        time.sleep(10)

        driver_firefox.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
        driver_firefox.get("https://ampdemo.azureedge.net/azuremediaplayer.html?url=%2F%2Famssamples.streaming.mediaservices.windows.net%2F49b57c87-f5f3-48b3-ba22-c55cfdffa9cb%2FSintel.ism%2Fmanifest&muted=true&aes=true")
        time.sleep(20)

 
    # Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        # Close the browser. 
        self.driver.close()
 
if __name__ == "__main__":
    unittest.main() 
'''