import random
from selenium import webdriver
from torch import randint

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("--headless")
option.add_argument("disable-gpu")
browser = webdriver.Edge()

browser.get("https://forms.gle/XcyVfoJ7r4NxuJRd6")

# Use the following snippets to get elements by their class names
#textboxes = browser.find_elements_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]')
radiobuttons = browser.find_elements_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[3]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]')
#checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
#submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

# Use the following snippets to get elements by their XPath
#otherboxes = browser.find_element_by_xpath("<Paste the XPath here>")

#textboxes[0].send_keys("Value education is the process by which people give moral values to each other.")

radiobuttons[random.randint(1,5)].click()

#checkboxes[1].click()
#checkboxes[3].click()

#submitbutton[0].click()
