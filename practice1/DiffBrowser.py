from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from practice1.PyAutoIt import uploadfile

# Firefox browser

firefox_options = webdriver.FirefoxOptions()
#firefox_options.add_argument('-headless')
firefox_options.set_preference("browser.download.folderList", 2)
firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
firefox_options.set_preference("browser.download.dir", "E:\Export")
firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel,image/jpeg")

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)

# Chrome browesr
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("prefs", {"download.default_directory": "E:\Export"})

#chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-notifications')

#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

# Internet Explorer browser
#driver = webdriver.Ie(executable_path=IEDriverManager().install())

#driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

#driver.get("http://demo.guru99.com/test/autoit.html")

driver.get("http://www.demoqa.com/upload-download")

#driver.implicitly_wait(3)
driver.maximize_window()

downloadbtn = driver.find_element_by_xpath("//a[text()='Download']")

wait = WebDriverWait(driver, 20)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='Download']")))

action = ActionChains(driver)

action.move_to_element(downloadbtn).click().perform()

sleep(4)

#driver.switch_to.frame("JotFormIFrame-72320244964454")

#wait = WebDriverWait(driver, 20)
#wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='input_5' and @class='form-upload validate[required]']")))

#uploadbtn = driver.find_element_by_xpath("//input[@id='input_5' and @class='form-upload validate[required]']")

#driver.execute_script("arguments[0].scrollIntoView(false);", uploadbtn)

#driver.execute_script("arguments[0].click();", uploadbtn)

#uploadbtn.click()

#action = ActionChains(driver)

#action.move_to_element(uploadbtn).click().perform()

#uploadfile("E:\CodeWorkspace\SeleniumWithPythonPractice\SeleniumWithPythonPractice\practice1\Test.xlsx")



#print("Title is "+driver.title)
#print("Current Url is "+driver.current_url)

#sleep(3)

#print(driver.get_cookies())

#driver.add_cookie({"name": "python", "domain": "reddit.com", "value": "python"})

#cookies = driver.get_cookies()
#for cookie in cookies:
#    print(cookie)

#driver.delete_all_cookies()

#print(driver.get_cookies())

#RadioButtons = driver.find_elements_by_css_selector("input.radioButton")

#for radiobutton in RadioButtons:
#    if radiobutton.get_attribute("value") == "radio2":
#        radiobutton.click()
#        print("Radio Button is Selected ", radiobutton.is_selected())
#        break


#AutoSuggest = driver.find_element_by_id("autocomplete")
#AutoSuggest.clear()
#AutoSuggest.send_keys("Gabon")
#wait = WebDriverWait(driver, 5)
#wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//ul[contains(@class,'ui-menu')]/li/div[text()='Gabon']")))
#Value = driver.find_element_by_xpath("//ul[contains(@class,'ui-menu')]/li/div")
#TextValue = Value.text
#print("Value is "+TextValue)
#AutoSuggestValue = driver.find_element_by_xpath("//ul[contains(@class,'ui-menu')]/li/div[text()='"+TextValue+"']")
#AutoSuggestValue.click()

#select = Select(driver.find_element_by_name("dropdown-class-example"))

#print("Is Multiple ", select.is_multiple)

#AllOptions = select.options

#for i in AllOptions:
#    print(i.text)

#select.select_by_value("option3")

#CheckBoxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

#for checkbox in CheckBoxes:
#    checkbox.click()
#    print("is Enabled ", checkbox.is_enabled(), end="")
#    print(checkbox.text)

#AlertInputBox = driver.find_element_by_css_selector("#name")

#AlertInputBox.clear()
#AlertInputBox.send_keys("Nagesh")

#AlertBtn = driver.find_element_by_css_selector("#alertbtn")

#AlertBtn.click()

#Alerts = driver.switch_to.alert

#print(Alerts.text)

#Alerts.accept()

#DisplayedElement = driver.find_element_by_xpath("//input[@class='inputs displayed-class']")

#print("CSS Value ", DisplayedElement.value_of_css_property("font-size"))

#HideBtn = driver.find_element_by_id("hide-textbox")

#HideBtn.click()

#print("Clicked on Hide Button ", DisplayedElement.is_displayed())

#ShowBtn = driver.find_element_by_id("show-textbox")

#ShowBtn.click()

#print("Clicked on Show Button ", DisplayedElement.is_displayed())

#TableElement = driver.find_element_by_xpath("//table[@id='product']//tr")

#TableHeader = TableElement.find_elements_by_xpath("th")

#for i in TableHeader:
#    print("Table header "+i.text)


#TableRow = driver.find_elements(By.XPATH, "//table[@id='product']//tr/td")

#for j in TableRow:
#    print("Table Row data "+j.text)

#parentwindowhanlde = driver.current_window_handle
#openwindowbutton = driver.find_element_by_xpath("//button[text()='Open Window']")
#driver.execute_script("arguments[0].click();", openwindowbutton)
#windowhandles = set(driver.window_handles)

#for windowhandle in windowhandles:
#    driver.switch_to.window(windowhandle)
#    if driver.title == "QA Click Academy | Selenium,Jmeter,SoapUI,Appium,Database testing,QA Training Academy":
#        print("Switched to Child Window")
#        driver.close()
#        break


#driver.switch_to.window(parentwindowhanlde)
#print("Switched back to Parent Window")

#driver.switch_to.frame("courses-iframe")

#homelink = driver.find_element_by_xpath("//a[text()='Home']")

#driver.execute_script("arguments[0].scrollIntoView(false);", homelink)

#driver.switch_to.parent_frame()

#action = ActionChains(driver)

#mousehoverelement = driver.find_element_by_xpath("//button[text()='Mouse Hover']")

#action.move_to_element(mousehoverelement).click_and_hold(mousehoverelement).perform()

#wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='mouse-hover-content']/a")))

#tooltiptexts = driver.find_elements_by_xpath("//div[@class='mouse-hover-content']/a")

#for tooltipelement in tooltiptexts:
#    print("Tooltip Text ", tooltipelement.text)


#driver.save_screenshot("abc.png")
#driver.quit()

#driver.get("https://www.rahulshettyacademy.com/#/index")

#driver.minimize_window()

#print("Title is "+driver.title)

#driver.back()

#print("Title is "+driver.title)

#driver.forward()

#print("Title is "+driver.title)
#driver.refresh()
#driver.get(driver.current_url)
#print(driver.page_source)
#driver.close()
driver.quit()
