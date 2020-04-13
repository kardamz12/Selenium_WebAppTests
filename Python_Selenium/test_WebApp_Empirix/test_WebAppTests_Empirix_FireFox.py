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


image_path = "E:\\Pawan\\Selenium\\WebAppTests_Empirix\\Images\\"


class TestSuite_Empirix(unittest.TestCase):
    def setUp(self):
        logging.info("(Firefox)## -- Entering 'setUp()' method -- ##")
        try:
            self.driver = Firefox(executable_path=r'E:\Pawan\Selenium\WebAppTests_Empirix\drivers\geckodriver.exe')
            self.driver.implicitly_wait(30)
            self.driver.maximize_window()
            self.driver.get("https://services.empirix.com/")
        except Exception as e:
            logging.exception("(Firefox)Issue in func setUp() - " + str(e))
            logging.exception(traceback.format_exc())


    def waitByName(self, name):
        try:
            WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.NAME, name)))
        except TimeoutError:
            logging.exception("(Firefox)Issue in func waitByName()")
            logging.exception(traceback.format_exc())


    def waitByClass(self, classname):
        try:
            WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.CLASS_NAME, classname)))
        except TimeoutError:
            logging.exception("(Firefox)Issue in func waitByName()")
            logging.exception(traceback.format_exc())


    def waitByXpath(self, xpath):
        try:
            WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutError:
            logging.exception("(Firefox)Issue in func waitByXpath()")
            logging.exception(traceback.format_exc())


    def slow_typing(self, element, text):
        try:
            for character in text:
                element.send_keys(character)
                time.sleep(0.3)
        except Exception as e:
            logging.exception("(Firefox)Issue in func slow_typing() - " + str(e))
            logging.exception(traceback.format_exc())


    def check_exists(self):
        try:
            self.driver.find_element_by_class_name('product')
        except NoSuchElementException:
            return False
        return True


    def Empirix_Login(self):
        logging.info("(Firefox)## -- Entering 'Empirix_Login()' method -- ##")
        try:
            time.sleep(1)

            logging.info("(Firefox)#--Located the 'username' textbox and going to slow-type username in it--")
            self.waitByName('callback_0')
            username = self.driver.find_element_by_name('callback_0')
            self.slow_typing(username, 'QA_traininguser25')
            time.sleep(1)

            logging.info("(Firefox)#--Located the 'password' textbox and going to enter password into it via a file saved in system--")
            self.waitByName('callback_1')
            password = self.driver.find_element_by_name('callback_1')

            try:
                with open('password.txt', 'r') as myfile:
                    Password = myfile.read().replace('\n', '')
            except:
                Password = "Empirix!"

            self.slow_typing(password, Password)
            time.sleep(2)

            logging.info("(Firefox)#--Located and going to click on the 'Sign-in' button--")
            self.waitByName('callback_2')
            signin = self.driver.find_element_by_name('callback_2')
            signin.click()

            time.sleep(30)

            logging.info("(Firefox)#--Located a Cookies popup on Window and going to press 'OK'--")
            try:
                cookies = self.driver.find_element_by_class_name('cc-compliance')
                cookies.click()
                logging.info("(Firefox)Cookies popup clicked successfully..")
                time.sleep(2)
            except:
                logging.exception("(Firefox)Cookies popup not clicked..")

            logging.info("(Firefox)Login Successful in 'Empirix' Website..")
            time.sleep(30)

        except Exception as e:
            logging.exception("(Firefox)Issue in func Empirix_Login() - " + str(e))
            logging.info("(Firefox)TestCase:: Logged into the 'Empirix' Website Successfully : FAIL")
            logging.exception(traceback.format_exc())


    #@unittest.skip("demonstrating skipping")
    def test_Empirix_Login(self):
        logging.info("(Firefox)## -- Entering TestCase method 'test_Empirix_Login()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            try:
                logging.info("(Firefox)#--Trying locating first page after Sign-in operation--")
                res = self.check_exists()
                if res:
                    logging.info("(Firefox)TestCase:: Logged into the 'Empirix' Website Successfully : PASS")
            except:
                logging.exception("(Firefox)#--Trying locating 'Sign-in' button on the page even after login operation--")
                signin = self.driver.find_element_by_name('callback_2')
                if signin:
                    logging.exception("(Firefox)TestCase:: Failed to login in 'Empirix' Website(Username / Password mismatch or some other issue) : FAIL")

        except Exception as e:
            logging.exception("(Firefox)Issue in func test_Empirix_Login() - " + str(e))
            logging.info("(Firefox)TestCase:: Logged into the 'Empirix' Website Successfully : FAIL")
            logging.exception(traceback.format_exc())


    def switch_language_toEnglish(self):
        logging.info("(Firefox)## -- Entering 'switch_language_toEnglish()' method -- ##")
        try:
            logging.info("(Firefox)#--Going to click on Profile dropdown--")
            profile_dropdown = self.driver.find_element_by_link_text('QA_traininguser25(Empirix_QA_Training)')
            profile_dropdown.click()
            time.sleep(3)

            logging.info("(Firefox)#--Located and going to click on the 'English' button from dropdown--")
            English = self.driver.find_element_by_xpath("//a[text()='English']")
            English.click()
            logging.info("(Firefox)Clicked English button..")
            time.sleep(5)

            logging.info("(Firefox)#--Switched to popup alert message to accept it--")
            obj = self.driver.switch_to.alert
            logging.info("(Firefox)Before clicking Alert")
            time.sleep(2)
            obj.accept()
            logging.info("(Firefox)After clicking Alert")
            time.sleep(30)
        except Exception as e:
            logging.exception("(Firefox)Issue in func switch_language_toEnglish() - " + str(e))
            logging.exception("(Firefox)TestCase:: Successfully switched to 'English' language(inside except) : FAIL")
            logging.exception(traceback.format_exc())


    def switch_language_toJapanese(self):
        logging.info("(Firefox)## -- Entering 'switch_language_toJapanese()' method -- ##")
        try:
            logging.info("(Firefox)#--Going to click on Profile dropdown--")
            profile_dropdown = self.driver.find_element_by_link_text('QA_traininguser25(Empirix_QA_Training)')
            profile_dropdown.click()
            time.sleep(3)

            logging.info("(Firefox)#--Located and going to click on the 'Japanese' button from dropdown--")
            Japan = self.driver.find_element_by_xpath("//a[text()='Japanese']")
            Japan.click()
            logging.info("(Firefox)Clicked Japanese..")
            time.sleep(5)

            logging.info("(Firefox)#--Switched to popup alert message to accept it--")
            obj = self.driver.switch_to.alert
            logging.info("(Firefox)Before clicking Alert")
            time.sleep(2)
            obj.accept()
            logging.info("(Firefox)After clicking Alert")
            time.sleep(30)
        except Exception as e:
            logging.exception("(Firefox)TestCase:: Successfully switched to 'Japanese' language(inside except) : FAIL")
            logging.exception("(Firefox)Issue in func switch_language_toEnglish() - " + str(e))
            logging.exception(traceback.format_exc())


    #@unittest.skip("Skipping English")
    def test_switch_language_toEnglish(self):
        logging.info("(Firefox)## -- Entering TestCase method 'test_switch_language_toEnglish()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            try:
                logging.info("(Firefox)#--Trying locating English 'Dashboard' tab on the page--")
                dashboard_eng = self.driver.find_element_by_xpath("//a[text()='Dashboard']")
                if dashboard_eng:
                    logging.info("(Firefox)TestCase:: Successfully switched to 'English' language : PASS")
            except:
                # var = 'ダッシュボード'
                # var = ascii(var)
                # var = '\u30c0\u30c3\u30b7\u30e5\u30dc\u30fc\u30c9'
                logging.exception("(Firefox)#--Trying locating Japanese 'Dashboard' tab on the page(inside except)--")
                dashboard_jap = self.driver.find_element_by_xpath("//a[text()='\u30c0\u30c3\u30b7\u30e5\u30dc\u30fc\u30c9']")
                if dashboard_jap:
                    logging.exception("(Firefox)Found Japanese, updating language to English")
                    self.switch_language_toEnglish()
                    try:
                        logging.exception("(Firefox)#-- Again trying locating English 'Dashboard' tab on the page--")
                        dashboard_eng = self.driver.find_element_by_xpath("//a[text()='Dashboard']")
                        if dashboard_eng:
                            logging.exception("(Firefox)TestCase:: Successfully switched to 'English' language : PASS")
                    except:
                        logging.exception("(Firefox)TestCase:: Successfully switched to 'English' language(language not changed or Page load issue) : FAIL")

        except Exception as e:
            logging.exception("(Firefox)TestCase:: Successfully switched to 'English' language(inside except) : FAIL")
            logging.exception("(Firefox)Issue in func switch_language() - " + str(e))
            logging.exception(traceback.format_exc())


    #@unittest.skip("Skipping English")
    def test_switch_language_toJapanese(self):
        logging.info("(Firefox)## -- Entering TestCase method 'test_switch_language_toJapanese()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            try:
                # var = 'ダッシュボード'
                # var = ascii(var)
                # var = '\u30c0\u30c3\u30b7\u30e5\u30dc\u30fc\u30c9'
                logging.info("(Firefox)#--Trying locating Japanese 'Dashboard' tab on the page--")
                dashboard_jap = self.driver.find_element_by_xpath("//a[text()='\u30c0\u30c3\u30b7\u30e5\u30dc\u30fc\u30c9']")
                if dashboard_jap:
                    logging.info("(Firefox)TestCase:: Successfully switched to 'Japanese' language : PASS")
            except:
                logging.exception("(Firefox)#--Trying locating English 'Dashboard' tab on the page(inside except)--")
                dashboard_eng = self.driver.find_element_by_xpath("//a[text()='Dashboard']")
                if dashboard_eng:
                    logging.exception("(Firefox)Found English, updating language to Japanese")
                    self.switch_language_toJapanese()
                    try:
                        # var = 'ダッシュボード'
                        # var = ascii(var)
                        # var = '\u30c0\u30c3\u30b7\u30e5\u30dc\u30fc\u30c9'
                        logging.exception("(Firefox)#-- Again trying locating Japanese 'Dashboard' tab on the page--")
                        dashboard_jap = self.driver.find_element_by_xpath("//a[text()='\u30c0\u30c3\u30b7\u30e5\u30dc\u30fc\u30c9']")
                        if dashboard_jap:
                            logging.exception("(Firefox)TestCase:: Successfully switched to 'Japanese' language : PASS")
                    except:
                        logging.exception("(Firefox)TestCase:: Successfully switched to 'Japanese' language(language not changed or Page load issue) : FAIL")

        except Exception as e:
            logging.exception("(Firefox)TestCase:: Successfully switched to 'Japanese' language(inside except) : FAIL")
            logging.exception("(Firefox)Issue in func switch_language() - " + str(e))
            logging.exception(traceback.format_exc())

    def viewTabs_English(self):
        logging.info("(Firefox)## -- Entering 'viewTabs_English()' method -- ##")
        try:
            logging.info("(Firefox)#--Accessing English Dashboard Tab--")

            logging.info("(Firefox)# --Located and going to click on the Dashboard tab--")
            self.waitByXpath("//a[text()='Dashboard']")
            dashboard = self.driver.find_element_by_xpath("//a[text()='Dashboard']")
            dashboard.click()
            time.sleep(10)

            logging.info("(Firefox)# --Locating a heading 'Overall Performance' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//div[@class='col-md-3']"):
                self.driver.save_screenshot(image_path + "Dashboard_english_firefox.png")
                logging.info("(Firefox)English Dashboard accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Firefox)Issue in func test_viewTabs_English(), inside Dashboard Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Firefox)# --Accessing English Alerts Tab--")

            logging.info("(Firefox)# --Located and going to click on the Alerts tab--")
            time.sleep(3)
            self.waitByXpath("//a[text()='Alerts']")
            alerts = self.driver.find_element_by_xpath("//a[text()='Alerts']")
            alerts.click()
            time.sleep(10)

            logging.info("(Firefox)# --Locating a heading 'Alert Status' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//th[text()='Alert Status']"):
                self.driver.save_screenshot(image_path + "Alerts_english_firefox.png")
                logging.info("(Firefox)English Alerts accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Firefox)Issue in func test_viewTabs_English(), inside Alerts Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Firefox)# --Accessing English Tests Tab--")

            logging.info("(Firefox)# --Located and going to click on the Tests tab--")
            time.sleep(3)
            self.waitByXpath("//a[text()='Tests']")
            tests = self.driver.find_element_by_xpath("//a[text()='Tests']")
            tests.click()
            time.sleep(10)

            logging.info("(Firefox)# --Locating a heading 'Please select a test' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//span[text()='Please select a test']"):
                self.driver.save_screenshot(image_path + "Tests_english_firefox.png")
                logging.info("(Firefox)English Tests accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Firefox)Issue in func test_viewTabs_English(), inside Tests Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Firefox)# --Accessing English Variables Tab--")

            logging.info("(Firefox)# --Located and going to click on the Variables tab--")
            time.sleep(3)
            self.waitByXpath("//a[text()='Variables']")
            tests = self.driver.find_element_by_xpath("//a[text()='Variables']")
            tests.click()
            time.sleep(10)

            logging.info("(Firefox)# --Locating a heading 'Please select a variable, or the following:' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//div[text()=' Please select a variable, or the following:']"):
                self.driver.save_screenshot(image_path + "Variables_english_firefox.png")
                logging.info("(Firefox)English Variables accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Firefox)Issue in func test_viewTabs_English(), inside Variables Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Firefox)# --Accessing English Notifications Tab--")

            logging.info("(Firefox)# --Located and going to click on the Notifications tab--")
            time.sleep(3)
            self.waitByXpath("//a[text()='Notifications']")
            notifications = self.driver.find_element_by_xpath("//a[text()='Notifications']")
            notifications.click()
            time.sleep(10)

            logging.info("(Firefox)# --Locating a heading 'Please select a notification' and clicked on 'test' before taking screenshot--")
            if self.driver.find_element_by_xpath("//span[text()='Please select a notification']"):
                test = self.driver.find_element_by_class_name("nav.nav-sidebar.tests.ng-binding.ng-scope")
                if test:
                    test.click()
                    time.sleep(10)
                    self.driver.save_screenshot(image_path + "Notifications_english_firefox.png")
                    logging.info("(Firefox)English Notifications accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Firefox)Issue in func test_viewTabs_English(), inside Notifications Tab - " + str(e))
            logging.exception(traceback.format_exc())


    def viewTabs_Japanese(self):
        logging.info("(Firefox)## -- Entering viewTabs_Japanese() method -- ##")
        try:
            logging.info("(Firefox)# --Accessing Japanese Dashboard Tab--")

            # var = 'ダッシュボード'
            # var = ascii(var)
            # var = '\u30c0\u30c3\u30b7\u30e5\u30dc\u30fc\u30c9'
            logging.info("(Firefox)# --Located and going to click on the Dashboard tab--")
            self.waitByXpath("//a[text()='\u30c0\u30c3\u30b7\u30e5\u30dc\u30fc\u30c9']")
            dashboard = self.driver.find_element_by_xpath("//a[text()='\u30c0\u30c3\u30b7\u30e5\u30dc\u30fc\u30c9']")
            dashboard.click()
            time.sleep(10)

            logging.info("(Firefox)# --Locating a heading 'Overall Performance' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//div[@class='col-md-3']"):
                self.driver.save_screenshot(image_path + "Dashboard_japanese_firefox.png")
                logging.info("(Firefox)Japanese Dashboard accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Firefox)Issue in func test_viewTabs_Japanese(), inside Dashboard Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Firefox)# --Accessing Japanese Alerts Tab--")

            # var = 'アラート'
            # var = ascii(var)
            # var = '\u30a2\u30e9\u30fc\u30c8'
            logging.info("(Firefox)# --Located and going to click on the Alerts tab--")
            time.sleep(3)
            self.waitByXpath("//a[text()='\u30a2\u30e9\u30fc\u30c8']")
            alerts = self.driver.find_element_by_xpath("//a[text()='\u30a2\u30e9\u30fc\u30c8']")
            alerts.click()
            time.sleep(10)

            # var = 'アラートステータス'
            # var = ascii(var)
            # var = '\u30a2\u30e9\u30fc\u30c8\u30b9\u30c6\u30fc\u30bf\u30b9'
            logging.info("(Firefox)# --Locating a heading 'Alert Status' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//th[text()='\u30a2\u30e9\u30fc\u30c8\u30b9\u30c6\u30fc\u30bf\u30b9']"):
                self.driver.save_screenshot(image_path + "Alerts_japanese_firefox.png")
                logging.info("(Firefox)Japanese Alerts accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Firefox)Issue in func test_viewTabs_Japanese(), inside Alerts Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Firefox)# --Accessing Japanese Tests Tab--")

            logging.info("(Firefox)# --Located and going to click on the Tests tab--")
            time.sleep(3)
            # var = 'テスト'
            # var = ascii(var)
            # var = '\u30c6\u30b9\u30c8'
            self.waitByXpath("//a[text()='\u30c6\u30b9\u30c8']")
            tests = self.driver.find_element_by_xpath("//a[text()='\u30c6\u30b9\u30c8']")
            tests.click()
            time.sleep(10)

            # var = 'テストを選択してください。'
            # var = ascii(var)
            # var = '\u30c6\u30b9\u30c8\u3092\u9078\u629e\u3057\u3066\u304f\u3060\u3055\u3044\u3002'
            logging.info("(Firefox)# --Locating a heading 'Please select a test' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//span[text()='\u30c6\u30b9\u30c8\u3092\u9078\u629e\u3057\u3066\u304f\u3060\u3055\u3044\u3002']"):
                self.driver.save_screenshot(image_path + "Tests_japanese_firefox.png")
                logging.info("(Firefox)Japanese Tests accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Firefox)Issue in func test_viewTabs_Japanese(), inside Tests Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Firefox)# --Accessing Japanese Variables Tab--")

            # var = '変数'
            # var = ascii(var)
            # var = '\u5909\u6570'
            logging.info("(Firefox)# --Located and going to click on the Variables tab--")
            time.sleep(3)
            self.waitByXpath("//a[text()='\u5909\u6570']")
            tests = self.driver.find_element_by_xpath("//a[text()='\u5909\u6570']")
            tests.click()
            time.sleep(10)

            # var = '変数を選択してください。または、以下のように操作してください。'
            # var = ascii(var)
            # var = '\u5909\u6570\u3092\u9078\u629e\u3057\u3066\u304f\u3060\u3055\u3044\u3002\u307e\u305f\u306f\u3001\u4ee5\u4e0b\u306e\u3088\u3046\u306b\u64cd\u4f5c\u3057\u3066\u304f\u3060\u3055\u3044\u3002'
            logging.info("(Firefox)# --Locating a heading 'Please select a variable, or the following:' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//div[text()='\u5909\u6570\u3092\u9078\u629e\u3057\u3066\u304f\u3060\u3055\u3044\u3002\u307e\u305f\u306f\u3001\u4ee5\u4e0b\u306e\u3088\u3046\u306b\u64cd\u4f5c\u3057\u3066\u304f\u3060\u3055\u3044\u3002']"):
                self.driver.save_screenshot(image_path + "Variables_japanese_firefox.png")
                logging.info("(Firefox)Japanese Variables accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Firefox)Issue in func test_viewTabs_Japanese(), inside Variables Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Firefox)# --Accessing Japanese Notifications Tab--")

            # var = '通知'
            # var = ascii(var)
            # var = '\u901a\u77e5'
            logging.info("(Firefox)# --Located and going to click on the Notifications tab--")
            time.sleep(3)
            self.waitByXpath("//a[text()='\u901a\u77e5']")
            notifications = self.driver.find_element_by_xpath("//a[text()='\u901a\u77e5']")
            notifications.click()
            time.sleep(10)

            # var = '通知を選択してください。'
            # var = ascii(var)
            # var = '\u901a\u77e5\u3092\u9078\u629e\u3057\u3066\u304f\u3060\u3055\u3044\u3002'
            logging.info("(Firefox)# --Locating a heading 'Please select a notification' and clicked on 'test' before taking screenshot--")
            if self.driver.find_element_by_xpath("//span[text()='\u901a\u77e5\u3092\u9078\u629e\u3057\u3066\u304f\u3060\u3055\u3044\u3002']"):
                test = self.driver.find_element_by_class_name("nav.nav-sidebar.tests.ng-binding.ng-scope")
                if test:
                    test.click()
                    time.sleep(10)
                    self.driver.save_screenshot(image_path + "Notifications_japanese_firefox.png")
                    logging.info("(Firefox)Japanese Notifications accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Firefox)Issue in func test_viewTabs_Japanese(), inside Notifications Tab - " + str(e))
            logging.exception(traceback.format_exc())


    #@unittest.skip("Skipping English")
    def test_viewTabs_English(self):
        logging.info("(Firefox)## -- Entering TestCase method 'test_viewTabs_English()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            try:
                logging.info("(Firefox)#--Trying to locate English 'Dashboard' tab on the page")
                dashboard_eng = self.driver.find_element_by_xpath("//a[text()='Dashboard']")
                if dashboard_eng:
                    self.viewTabs_English()
            except:
                # var = 'ダッシュボード'
                # var = ascii(var)
                # var = '\u30c0\u30c3\u30b7\u30e5\u30dc\u30fc\u30c9'
                logging.exception("(Firefox)#--Trying to locate Japanese 'Dashboard' tab on the page(inside except)")
                dashboard_jap = self.driver.find_element_by_xpath("//a[text()='\u30c0\u30c3\u30b7\u30e5\u30dc\u30fc\u30c9']")
                if dashboard_jap:
                    logging.exception("(Firefox)#--Found Japanese, updating language to English")
                    self.switch_language_toEnglish()
                    self.viewTabs_English()

        except Exception as e:
            logging.exception("(Firefox)Issue in func test_viewTabs_English() - " + str(e))
            logging.exception(traceback.format_exc())


    #@unittest.skip("Skipping japanese")
    def test_viewTabs_Japanese(self):
        logging.info("(Firefox)## -- Entering TestCase method 'test_viewTabs_Japanese()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            try:
                # var = 'ダッシュボード'
                # var = ascii(var)
                # var = '\u30c0\u30c3\u30b7\u30e5\u30dc\u30fc\u30c9'
                logging.info("(Firefox)#--Trying to locate Japanese 'Dashboard' tab on the page")
                dashboard_jap = self.driver.find_element_by_xpath("//a[text()='\u30c0\u30c3\u30b7\u30e5\u30dc\u30fc\u30c9']")
                if dashboard_jap:
                    self.viewTabs_Japanese()
            except:
                logging.exception("(Firefox)#--Trying to locate English 'Dashboard' tab on the page(inside except)")
                dashboard_eng = self.driver.find_element_by_xpath("//a[text()='Dashboard']")
                if dashboard_eng:
                    logging.exception("(Firefox)#--Found English, updating language to Japanese")
                    self.switch_language_toJapanese()
                    self.viewTabs_Japanese()

        except Exception as e:
            logging.exception("(Firefox)Issue in func viewTabs_Japanese() - " + str(e))
            logging.exception(traceback.format_exc())


    #@unittest.skip("Skipping English")
    def test_clientInfo_check_english(self):
        logging.info("(Firefox)## -- Entering TestCase method 'test_clientInfo_check_english()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            logging.info("(Firefox)# --Going to click on Profile dropdown--")
            profile_dropdown = self.driver.find_element_by_link_text('QA_traininguser25(Empirix_QA_Training)')
            profile_dropdown.click()
            time.sleep(5)

            try:
                logging.info("(Firefox)# --Going to click on English 'Client' from the dropdown menu--")
                client_eng = self.driver.find_element_by_xpath("//span[text()='Client']")
                if client_eng:
                    client_eng.click()
                    time.sleep(10)
                    logging.info("(Firefox)# --Locating a heading 'Client Details' in English on the page before taking screenshot--")
                    if self.driver.find_element_by_class_name('panel-title'):
                        self.driver.save_screenshot(image_path + "ClientDetails_english_firefox.png")
                        logging.info("(Firefox)Client Details accessed in English and captured an Image of it..")
                        logging.info("(Firefox)TestCase:: Client Details accessed in 'English' Successfully : PASS")
            except:
                # var = 'クライアント'
                # var = ascii(var)
                # var = '\u30af\u30e9\u30a4\u30a2\u30f3\u30c8'
                logging.exception("(Firefox)# --Checking for a Japanese 'Client' from the dropdown menu(inside except)--")
                client_jap = self.driver.find_element_by_xpath("//span[text()='\u30af\u30e9\u30a4\u30a2\u30f3\u30c8']")
                if client_jap:
                    profile_dropdown.click()
                    time.sleep(5)
                    logging.exception("(Firefox)#--Found Japanese, updating language to English")
                    self.switch_language_toEnglish()
                    try:
                        profile_dropdown = self.driver.find_element_by_link_text('QA_traininguser25(Empirix_QA_Training)')
                        if profile_dropdown:
                            profile_dropdown.click()
                            time.sleep(3)
                            logging.exception("(Firefox)# --Going to click on English 'Client' from the dropdown menu once language is changed--")
                            client_eng = self.driver.find_element_by_xpath("//span[text()='Client']")
                            if client_eng:
                                client_eng.click()
                                time.sleep(10)
                                logging.exception("(Firefox)# --Locating a heading 'Client Details' in English on the page before taking screenshot--")
                                if self.driver.find_element_by_class_name('panel-title'):
                                    self.driver.save_screenshot(image_path + "ClientDetails_english_firefox.png")
                                    logging.exception("(Firefox)Client Details accessed in English and captured an Image of it..")
                                    logging.exception("(Firefox)TestCase:: Client Details accessed in 'English' Successfully : PASS")
                    except:
                        logging.exception("(Firefox)TestCase:: Client Details accessed in 'English' Successfully(language not changed or Page load issue) : FAIL")

        except Exception as e:
            logging.exception("(Firefox)TestCase:: Client Details accessed in 'English' Successfully(inside except) : FAIL")
            logging.exception("(Firefox)Issue in func test_clientInfo_check_english() - " + str(e))
            logging.exception(traceback.format_exc())


    #@unittest.skip("Skipping japanese")
    def test_clientInfo_check_japanese(self):
        logging.info("(Firefox)## -- Entering TestCase method 'test_clientInfo_check_japanese()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            logging.info("(Firefox)# --Going to click on Profile dropdown--")
            profile_dropdown = self.driver.find_element_by_link_text('QA_traininguser25(Empirix_QA_Training)')
            profile_dropdown.click()
            time.sleep(3)

            try:
                # var = 'クライアント'
                # var = ascii(var)
                # var = '\u30af\u30e9\u30a4\u30a2\u30f3\u30c8'
                logging.info("(Firefox)# --Going to click on Japanese 'Client' from the dropdown menu--")
                client_jap = self.driver.find_element_by_xpath("//span[text()='\u30af\u30e9\u30a4\u30a2\u30f3\u30c8']")
                if client_jap:
                    client_jap.click()
                    time.sleep(10)
                    logging.info("(Firefox)# --Locating a heading 'Client Details' in Japanese on the page before taking screenshot--")
                    if self.driver.find_element_by_class_name('panel-title'):
                        self.driver.save_screenshot(image_path + "ClientDetails_japanese_firefox.png")
                        logging.info("(Firefox)Client Details accessed in Japanese and captured an Image of it..")
                        logging.info("(Firefox)TestCase:: Client Details accessed in 'Japanese' Successfully : PASS")
            except:
                logging.exception("(Firefox)# --Checking for a English 'Client' from the dropdown menu(inside except)--")
                client_eng = self.driver.find_element_by_xpath("//span[text()='Client']")
                if client_eng:
                    profile_dropdown.click()
                    time.sleep(3)
                    logging.exception("(Firefox)#--Found English, updating language to Japanese")
                    self.switch_language_toJapanese()
                    try:
                        profile_dropdown = self.driver.find_element_by_link_text('QA_traininguser25(Empirix_QA_Training)')
                        if profile_dropdown:
                            profile_dropdown.click()
                            time.sleep(3)
                            logging.exception("(Firefox)# --Going to click on Japanese 'Client' from the dropdown menu once language is changed--")
                            client_jap = self.driver.find_element_by_xpath("//span[text()='\u30af\u30e9\u30a4\u30a2\u30f3\u30c8']")
                            if client_jap:
                                client_jap.click()
                                time.sleep(10)
                                logging.exception("(Firefox)# --Locating a heading 'Client Details' in Japanese on the page before taking screenshot--")
                                if self.driver.find_element_by_class_name('panel-title'):
                                    self.driver.save_screenshot(image_path + "ClientDetails_japanese_firefox.png")
                                    logging.exception("(Firefox)Client Details accessed in Japanese and captured an Image of it..")
                                    logging.exception("(Firefox)TestCase:: Client Details accessed in 'Japanese' Successfully : PASS")
                    except:
                        logging.exception("(Firefox)TestCase:: Client Details accessed in 'Japanese' Successfully(language not changed or Page load issue) : FAIL")

        except Exception as e:
            logging.exception("(Firefox)TestCase:: Client Details accessed in 'Japanese' Successfully(inside except) : FAIL")
            logging.exception("(Firefox)Issue in func test_clientInfo_check_japanese() - " + str(e))
            logging.exception(traceback.format_exc())


    def tearDown(self):
        logging.info("(Firefox)## -- Entering tearDown() method -- ##")
        try:
            self.driver.quit()
        except Exception as e:
            logging.exception("(Firefox)Issue in func tearDown() - " + str(e))
            logging.exception(traceback.format_exc())


if __name__ == "__main__":
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()

