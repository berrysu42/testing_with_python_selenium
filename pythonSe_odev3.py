from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

class  testCase:
    def username_passwordControls(self):
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(3)
        loginButton=driver.find_element(By.ID,"login-button")
        sleep(3)
        loginButton.click()
        sleep(3)
        returnMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3") 
        testResult=returnMessage.text=="Epic sadface: Username is required"
        

    def passwordControls(self):
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(3)
        userNameInput = driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("standard_user")
        userNameInput.click()
        sleep(3)
        passwordInput=driver.find_element(By.ID,"password")
        passwordInput.send_keys("")
        loginButton=driver.find_element(By.ID,"login-button")
        sleep(3)
        loginButton.click()
        returnMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3") 
        testResult=returnMessage.text=="Epic sadface: Password is required"
    
    def nightmare_noun(self):
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(3)
        userNameInput = driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("locked_out_user")
        userNameInput.click()
        sleep(3)
        passwordInput=driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        loginButton=driver.find_element(By.ID,"login-button")
        sleep(3)
        loginButton.click()
        returnMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3") 
        testResult=returnMessage.text== "Epic sadface: Sorry, this user has been locked out."
        sleep(10)
    
    def page_assignment (self):
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(3)
        userNameInput = driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("standard_user")
        userNameInput.click()
        sleep(3)
        passwordInput=driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        loginButton=driver.find_element(By.ID,"login-button")
        sleep(3)
        loginButton.click()
        sleep(1000)
        redirected_page="https://www.saucedemo.com/inventory.html"
        print(f"{redirected_page} sayfasına giriş yapılıyor.")

    def number_of_products(self):
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(3)
        userNameInput = driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("standard_user")
        userNameInput.click()
        sleep(3)
        passwordInput=driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        loginButton=driver.find_element(By.ID,"login-button")
        sleep(3)
        loginButton.click()
        sleep(30)
        redirected_page="https://www.saucedemo.com/inventory.html"

        inventory_page=driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"{redirected_page} sitesinde şu anda {len(inventory_page)} adet ürün var.")

    def icon_x(self):
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(3)
        loginButton=driver.find_element(By.ID,"login-button")
        sleep(3)
        loginButton.click()
        sleep(5)
        username_icon= driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
        password_icon=driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        sleep(30)
       
        
       




testClass=testCase()
#testClass.username_passwordControls()
#testClass.passwordControls()
#testClass.nightmare_noun()
#testClass.page_assignment()
#testClass.number_of_products()
testClass.icon_x()