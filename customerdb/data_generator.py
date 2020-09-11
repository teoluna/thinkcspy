import names
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

x = 100000
driver = webdriver.Firefox()

for i in range(x):
    # navigate to a link

    driver.get("http://localhost:5000/")

    # fill in the forms on the page
    driver.find_element_by_name("username").send_keys(names.get_first_name())
    driver.find_element_by_name("favfood").send_keys(random.randrange(0, 100))

    # click continue button
    driver.find_element_by_xpath("//input[@type='submit']").click()

    assert "No results found." not in driver.page_source

driver.close()