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
                    level=logging.INFO, stream=sys.stdout)


class TestSuite_Empirix(unittest.TestCase):
    def setUp(self):
        logging.info("(Chrome)## -- Entering 'setUp()' method -- ##")
        try:
            self.driver = Chrome(executable_path=r'E:\Pawan\Selenium\WebAppTests_Empirix\drivers\chromedriver.exe')
            self.driver.implicitly_wait(30)
            self.driver.maximize_window()
            self.driver.get("https://services.empirix.com/")
        except Exception as e:
            logging.exception("(Chrome)Issue in func setUp() - " + str(e))
            logging.exception(traceback.format_exc())


    def waitByName(self, name):
        try:
            WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.NAME, name)))
        except TimeoutError:
            logging.exception("(Chrome)Issue in func waitByName()")
            logging.exception(traceback.format_exc())


    def waitByClass(self, classname):
        try:
            WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.CLASS_NAME, classname)))
        except TimeoutError:
            logging.exception("(Chrome)Issue in func waitByName()")
            logging.exception(traceback.format_exc())


    def waitByXpath(self, xpath):
        try:
            WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutError:
            logging.exception("(Chrome)Issue in func waitByXpath()")
            logging.exception(traceback.format_exc())


    def slow_typing(self, element, text):
        try:
            for character in text:
                element.send_keys(character)
                time.sleep(0.3)
        except Exception as e:
            logging.exception("(Chrome)Issue in func slow_typing() - " + str(e))
            logging.exception(traceback.format_exc())


    def check_exists(self):
        try:
            self.driver.find_element_by_class_name('product')
        except NoSuchElementException:
            return False
        return True


    def Empirix_Login(self):
        logging.info("(Chrome)## -- Entering 'Empirix_Login()' method -- ##")
        try:
            time.sleep(1)

            logging.info("(Chrome)#--Located the 'username' textbox and going to slow-type username in it--")
            self.waitByName('callback_0')
            username = self.driver.find_element_by_name('callback_0')
            self.slow_typing(username, 'QA_traininguser25')
            time.sleep(1)

            logging.info("(Chrome)#--Located the 'password' textbox and going to enter password into it via a file saved in system--")
            self.waitByName('callback_1')
            password = self.driver.find_element_by_name('callback_1')

            try:
                with open('password.txt', 'r') as myfile:
                    Password = myfile.read().replace('\n', '')
            except:
                Password = "Empirix!"

            self.slow_typing(password, Password)
            time.sleep(2)

            logging.info("(Chrome)#--Located and going to click on the 'Sign-in' button--")
            self.waitByName('callback_2')
            signin = self.driver.find_element_by_name('callback_2')
            signin.click()

            time.sleep(30)

            logging.info("(Chrome)#--Located a Cookies popup on Window and going to press 'OK'--")
            try:
                cookies = self.driver.find_element_by_class_name('cc-compliance')
                cookies.click()
                logging.info("(Chrome)Cookies popup clicked successfully..")
                time.sleep(2)
            except:
                logging.exception("(Chrome)Cookies popup not clicked..")

            logging.info("(Chrome)Login Successful in 'Empirix' Website..")
            time.sleep(30)

        except Exception as e:
            logging.exception("(Chrome)Issue in func Empirix_Login() - " + str(e))
            logging.info("(Chrome)TestCase:: Logged into the 'Empirix' Website Successfully : FAIL")
            logging.exception(traceback.format_exc())
            sys.exit()


    #@unittest.skip("demonstrating skipping")
    def test_Empirix_Login(self):
        logging.info("(Chrome)## -- Entering TestCase method 'test_Empirix_Login()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            try:
                logging.info("(Chrome)#--Trying locating first page after Sign-in operation--")
                res = self.check_exists()
                if res:
                    logging.info("(Chrome)TestCase:: Logged into the 'Empirix' Website Successfully : PASS")
            except:
                logging.exception("(Chrome)#--Trying locating 'Sign-in' button on the page even after login operation--")
                signin = self.driver.find_element_by_name('callback_2')
                if signin:
                    logging.exception("(Chrome)TestCase:: Failed to login in 'Empirix' Website(Username / Password mismatch or some other issue) : FAIL")

        except Exception as e:
            logging.exception("(Chrome)Issue in func test_Empirix_Login() - " + str(e))
            logging.info("(Chrome)TestCase:: Logged into the 'Empirix' Website Successfully : FAIL")
            logging.exception(traceback.format_exc())


    def switch_language_toEnglish(self):
        logging.info("(Chrome)## -- Entering 'switch_language_toEnglish()' method -- ##")
        try:
            logging.info("(Chrome)#--Going to click on Profile dropdown--")
            profile_dropdown = self.driver.find_element_by_link_text('QA_traininguser25(Empirix_QA_Training)')
            profile_dropdown.click()
            time.sleep(3)

            logging.info("(Chrome)#--Located and going to click on the 'English' button from dropdown--")
            English = self.driver.find_element_by_xpath("//a[text()='English']")
            English.click()
            logging.info("(Chrome)Clicked English button..")
            time.sleep(5)

            logging.info("(Chrome)#--Switched to popup alert message to accept it--")
            obj = self.driver.switch_to.alert
            logging.info("(Chrome)Before clicking Alert")
            time.sleep(2)
            obj.accept()
            logging.info("(Chrome)After clicking Alert")
            time.sleep(30)
        except Exception as e:
            logging.exception("(Chrome)Issue in func switch_language_toEnglish() - " + str(e))
            logging.exception("(Chrome)TestCase:: Successfully switched to 'English' language(inside except) : FAIL")
            logging.exception(traceback.format_exc())
            sys.exit()


    def switch_language_toJapanese(self):
        logging.info("(Chrome)## -- Entering 'switch_language_toJapanese()' method -- ##")
        try:
            logging.info("(Chrome)#--Going to click on Profile dropdown--")
            profile_dropdown = self.driver.find_element_by_link_text('QA_traininguser25(Empirix_QA_Training)')
            profile_dropdown.click()
            time.sleep(3)

            logging.info("(Chrome)#--Located and going to click on the 'Japanese' button from dropdown--")
            Japan = self.driver.find_element_by_xpath("//a[text()='Japanese']")
            Japan.click()
            logging.info("(Chrome)Clicked Japanese..")
            time.sleep(5)

            logging.info("(Chrome)#--Switched to popup alert message to accept it--")
            obj = self.driver.switch_to.alert
            logging.info("(Chrome)Before clicking Alert")
            time.sleep(2)
            obj.accept()
            logging.info("(Chrome)After clicking Alert")
            time.sleep(30)
        except Exception as e:
            logging.exception("(Chrome)TestCase:: Successfully switched to 'Japanese' language(inside except) : FAIL")
            logging.exception("(Chrome)Issue in func switch_language_toEnglish() - " + str(e))
            logging.exception(traceback.format_exc())
            sys.exit()


    @unittest.skip("Skipping English")
    def test_switch_language_toEnglish(self):
        logging.info("(Chrome)## -- Entering TestCase method 'test_switch_language_toEnglish()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            try:
                logging.info("(Chrome)#--Trying locating English 'Dashboard' tab on the page--")
                dashboard_eng = self.driver.find_element_by_xpath("//a[text()='Dashboard']")
                if dashboard_eng:
                    logging.info("(Chrome)TestCase:: Successfully switched to 'English' language : PASS")
            except:
                logging.exception("(Chrome)#--Trying locating Japanese 'Dashboard' tab on the page(inside except)--")
                dashboard_jap = self.driver.find_element_by_xpath("//a[text()='ダッシュボード']")
                if dashboard_jap:
                    logging.exception("(Chrome)Found Japanese, updating language to English")
                    self.switch_language_toEnglish()
                    try:
                        logging.exception("(Chrome)#-- Again trying locating English 'Dashboard' tab on the page--")
                        dashboard_eng = self.driver.find_element_by_xpath("//a[text()='Dashboard']")
                        if dashboard_eng:
                            logging.exception("(Chrome)TestCase:: Successfully switched to 'English' language : PASS")
                    except:
                        logging.exception("(Chrome)TestCase:: Successfully switched to 'English' language(language not changed or Page load issue) : FAIL")

        except Exception as e:
            logging.exception("(Chrome)TestCase:: Successfully switched to 'English' language(inside except) : FAIL")
            logging.exception("(Chrome)Issue in func switch_language() - " + str(e))
            logging.exception(traceback.format_exc())


    @unittest.skip("Skipping English")
    def test_switch_language_toJapanese(self):
        logging.info("(Chrome)## -- Entering TestCase method 'test_switch_language_toJapanese()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            try:
                logging.info("(Chrome)#--Trying locating Japanese 'Dashboard' tab on the page--")
                dashboard_jap = self.driver.find_element_by_xpath("//a[text()='ダッシュボード']")
                if dashboard_jap:
                    logging.info("(Chrome)TestCase:: Successfully switched to 'Japanese' language : PASS")
            except:
                logging.exception("(Chrome)#--Trying locating English 'Dashboard' tab on the page(inside except)--")
                dashboard_eng = self.driver.find_element_by_xpath("//a[text()='Dashboard']")
                if dashboard_eng:
                    logging.exception("(Chrome)Found English, updating language to Japanese")
                    self.switch_language_toJapanese()
                    try:
                        logging.exception("(Chrome)#-- Again trying locating Japanese 'Dashboard' tab on the page--")
                        dashboard_jap = self.driver.find_element_by_xpath("//a[text()='ダッシュボード']")
                        if dashboard_jap:
                            logging.exception("(Chrome)TestCase:: Successfully switched to 'Japanese' language : PASS")
                    except:
                        logging.exception("(Chrome)TestCase:: Successfully switched to 'Japanese' language(language not changed or Page load issue) : FAIL")

        except Exception as e:
            logging.exception("(Chrome)TestCase:: Successfully switched to 'Japanese' language(inside except) : FAIL")
            logging.exception("(Chrome)Issue in func switch_language() - " + str(e))
            logging.exception(traceback.format_exc())

if __name__ == "__main__":
    unittest.main()