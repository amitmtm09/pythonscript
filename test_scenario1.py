from selenium import webdriver
import time


list1 = []
driver = webdriver.Chrome(executable_path="F:\chromedriver_win32\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

#SearchBox

driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
time.sleep(5)
driver.find_element_by_css_selector("button[type='submit']").click()
time.sleep(5)
#added all the item to cart
time.sleep(5)
products = driver.find_elements_by_xpath("//div/div/button[text()='ADD TO CART']") # add to cart
#//div/div/button[text()='ADD TO CART']/parent::div/parent::div/h4
for product in products:
    print(product.find_element_by_xpath("parent::div/parent::div/h4").text)
    time.sleep(5)
    list1.append(product.find_element_by_xpath("parent::div/parent::div/h4").text)
    product.click()
print(list1)
driver.close()