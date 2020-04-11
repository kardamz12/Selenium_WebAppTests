import unittest, time, traceback, os, urllib3
from selenium.webdriver import Chrome, ActionChains, Firefox, Edge
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import logging, sys, xmlrunner, pytest


logging.basicConfig(format='%(asctime)s %(message)s ',
                    datefmt='%m/%d/%Y %I:%M:%S %p ',
                    level=logging.INFO, filename='out_chrome.log', filemode='w+')
#stream=sys.stdout


class TestSuite_Empirix(unittest.TestCase):
    def setUp(self):
        logging.info("## -- Entering 'setUp()' method -- ##")
        try:
            self.driver = Chrome(os.path.join(os.getcwd(), "drivers", "chromedriver.exe"))
            self.driver.implicitly_wait(30)
            self.driver.maximize_window()
            self.driver.get("https://services.empirix.com/")
        except Exception as e:
            logging.exception("Issue in func setUp() - " + str(e))
            logging.exception(traceback.format_exc())


    def waitByName(self, name):
        try:
            WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.NAME, name)))
        except TimeoutError:
            logging.exception("Issue in func waitByName()")
            logging.exception(traceback.format_exc())


    def waitByClass(self, classname):
        try:
            WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.CLASS_NAME, classname)))
        except TimeoutError:
            logging.exception("Issue in func waitByName()")
            logging.exception(traceback.format_exc())


    def waitByXpath(self, xpath):
        try:
            WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutError:
            logging.exception("Issue in func waitByXpath()")
            logging.exception(traceback.format_exc())


    def slow_typing(self, element, text):
        try:
            for character in text:
                element.send_keys(character)
                time.sleep(0.3)
        except Exception as e:
            logging.exception("Issue in func slow_typing() - " + str(e))
            logging.exception(traceback.format_exc())


    def check_exists(self):
        try:
            self.driver.find_element_by_class_name('product')
        except NoSuchElementException:
            return False
        return True


    def Empirix_Login(self):
        logging.info("## -- Entering 'Empirix_Login()' method -- ##")
        try:
            time.sleep(1)

            logging.info("#--Located the 'username' textbox and going to slow-type username in it--")
            self.waitByName('callback_0')
            username = self.driver.find_element_by_name('callback_0')
            self.slow_typing(username, 'QA_traininguser25')
            time.sleep(1)

            logging.info("#--Located the 'password' textbox and going to enter password into it via a file saved in system--")
            self.waitByName('callback_1')
            password = self.driver.find_element_by_name('callback_1')

            try:
                with open('password.txt', 'r') as myfile:
                    Password = myfile.read().replace('\n', '')
            except:
                Password = "Empirix!"

            self.slow_typing(password, Password)
            time.sleep(2)

            logging.info("#--Located and going to click on the 'Sign-in' button--")
            self.waitByName('callback_2')
            signin = self.driver.find_element_by_name('callback_2')
            signin.click()

            time.sleep(30)

            logging.info("#--Located a Cookies popup on Window and going to press 'OK'--")
            try:
                cookies = self.driver.find_element_by_class_name('cc-compliance')
                cookies.click()
                logging.info("Cookies popup clicked successfully..")
                time.sleep(2)
            except:
                logging.exception("Cookies popup not clicked..")

            logging.info("Login Successful in 'Empirix' Website..")
            time.sleep(30)

        except Exception as e:
            logging.exception("Issue in func Empirix_Login() - " + str(e))
            logging.exception(traceback.format_exc())


    #@unittest.skip("demonstrating skipping")
    def test_Empirix_Login(self):
        logging.info("## -- Entering TestCase method 'test_Empirix_Login()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            try:
                logging.info("#--Trying locating first page after Sign-in operation--")
                res = self.check_exists()
                if res:
                    logging.info("TestCase:: Logged into the 'Empirix' Website Successfully : PASS")
            except:
                logging.exception("#--Trying locating 'Sign-in' button on the page even after login operation--")
                signin = self.driver.find_element_by_name('callback_2')
                if signin:
                    logging.exception("TestCase:: Failed to login in 'Empirix' Website(Username / Password mismatch or some other issue) : FAIL")

        except Exception as e:
            logging.exception("Issue in func test_Empirix_Login() - " + str(e))
            logging.exception(traceback.format_exc())


    def tearDown(self):
        logging.info("## -- Entering tearDown() method -- ##")
        try:
            self.driver.quit()
        except Exception as e:
            logging.exception("Issue in func tearDown() - " + str(e))
            logging.exception(traceback.format_exc())


if __name__ == "__main__":
    unittest.main()


