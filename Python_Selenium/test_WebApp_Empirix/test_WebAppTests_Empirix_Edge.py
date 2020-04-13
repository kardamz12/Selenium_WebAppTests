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
#stream=sys.stdout


class TestSuite_Empirix(unittest.TestCase):
    def setUp(self):
        logging.info("(Edge)## -- Entering 'setUp()' method -- ##")
        try:
            #self.driver = Edge(executable_path=os.path.join(os.getcwd(), "drivers", "msedgedriver.exe"))
            self.driver = Edge(executable_path=r'E:\Pawan\Selenium\WebAppTests_Empirix\drivers\msedgedriver.exe')
            self.driver.implicitly_wait(30)
            self.driver.maximize_window()
            self.driver.get("https://services.empirix.com/")
        except Exception as e:
            logging.exception("(Edge)Issue in func setUp() - " + str(e))
            logging.exception(traceback.format_exc())


    def waitByName(self, name):
        try:
            WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.NAME, name)))
        except TimeoutError:
            logging.exception("(Edge)Issue in func waitByName()")
            logging.exception(traceback.format_exc())


    def waitByClass(self, classname):
        try:
            WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.CLASS_NAME, classname)))
        except TimeoutError:
            logging.exception("(Edge)Issue in func waitByName()")
            logging.exception(traceback.format_exc())


    def waitByXpath(self, xpath):
        try:
            WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutError:
            logging.exception("(Edge)Issue in func waitByXpath()")
            logging.exception(traceback.format_exc())


    def slow_typing(self, element, text):
        try:
            for character in text:
                element.send_keys(character)
                time.sleep(0.3)
        except Exception as e:
            logging.exception("(Edge)Issue in func slow_typing() - " + str(e))
            logging.exception(traceback.format_exc())


    def check_exists(self):
        try:
            self.driver.find_element_by_class_name('product')
        except NoSuchElementException:
            return False
        return True


    def Empirix_Login(self):
        logging.info("(Edge)## -- Entering 'Empirix_Login()' method -- ##")
        try:
            time.sleep(1)

            logging.info("(Edge)#--Located the 'username' textbox and going to slow-type username in it--")
            self.waitByName('callback_0')
            username = self.driver.find_element_by_name('callback_0')
            self.slow_typing(username, 'QA_traininguser25')
            time.sleep(1)

            logging.info("(Edge)#--Located the 'password' textbox and going to enter password into it via a file saved in system--")
            self.waitByName('callback_1')
            password = self.driver.find_element_by_name('callback_1')

            try:
                with open('password.txt', 'r') as myfile:
                    Password = myfile.read().replace('\n', '')
            except:
                Password = "Empirix!"

            self.slow_typing(password, Password)
            time.sleep(2)

            logging.info("(Edge)#--Located and going to click on the 'Sign-in' button--")
            self.waitByName('callback_2')
            signin = self.driver.find_element_by_name('callback_2')
            signin.click()

            time.sleep(30)

            logging.info("(Edge)#--Located a Cookies popup on Window and going to press 'OK'--")
            try:
                cookies = self.driver.find_element_by_class_name('cc-compliance')
                cookies.click()
                logging.info("(Edge)Cookies popup clicked successfully..")
                time.sleep(2)
            except:
                logging.exception("(Edge)Cookies popup not clicked..")

            logging.info("(Edge)Login Successful in 'Empirix' Website..")
            time.sleep(30)

        except Exception as e:
            logging.exception("(Edge)Issue in func Empirix_Login() - " + str(e))
            logging.info("(Edge)TestCase:: Logged into the 'Empirix' Website Successfully : FAIL")
            logging.exception(traceback.format_exc())
            sys.exit()


    #@unittest.skip("demonstrating skipping")
    def test_Empirix_Login(self):
        logging.info("(Edge)## -- Entering TestCase method 'test_Empirix_Login()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            try:
                logging.info("(Edge)#--Trying locating first page after Sign-in operation--")
                res = self.check_exists()
                if res:
                    logging.info("(Edge)TestCase:: Logged into the 'Empirix' Website Successfully : PASS")
            except:
                logging.exception("(Edge)#--Trying locating 'Sign-in' button on the page even after login operation--")
                signin = self.driver.find_element_by_name('callback_2')
                if signin:
                    logging.exception("(Edge)TestCase:: Failed to login in 'Empirix' Website(Username / Password mismatch or some other issue) : FAIL")

        except Exception as e:
            logging.exception("(Edge)Issue in func test_Empirix_Login() - " + str(e))
            logging.info("(Edge)TestCase:: Logged into the 'Empirix' Website Successfully : FAIL")
            logging.exception(traceback.format_exc())


    def switch_language_toEnglish(self):
        logging.info("(Edge)## -- Entering 'switch_language_toEnglish()' method -- ##")
        try:
            logging.info("(Edge)#--Going to click on Profile dropdown--")
            profile_dropdown = self.driver.find_element_by_link_text('QA_traininguser25(Empirix_QA_Training)')
            profile_dropdown.click()
            time.sleep(3)

            logging.info("(Edge)#--Located and going to click on the 'English' button from dropdown--")
            English = self.driver.find_element_by_xpath("//a[text()='English']")
            English.click()
            logging.info("(Edge)Clicked English button..")
            time.sleep(5)

            logging.info("(Edge)#--Switched to popup alert message to accept it--")
            obj = self.driver.switch_to.alert
            logging.info("(Edge)Before clicking Alert")
            time.sleep(2)
            obj.accept()
            logging.info("(Edge)After clicking Alert")
            time.sleep(30)
        except Exception as e:
            logging.exception("(Edge)Issue in func switch_language_toEnglish() - " + str(e))
            logging.exception("(Edge)TestCase:: Successfully switched to 'English' language(inside except) : FAIL")
            logging.exception(traceback.format_exc())
            sys.exit()


    def switch_language_toJapanese(self):
        logging.info("(Edge)## -- Entering 'switch_language_toJapanese()' method -- ##")
        try:
            logging.info("(Edge)#--Going to click on Profile dropdown--")
            profile_dropdown = self.driver.find_element_by_link_text('QA_traininguser25(Empirix_QA_Training)')
            profile_dropdown.click()
            time.sleep(3)

            logging.info("(Edge)#--Located and going to click on the 'Japanese' button from dropdown--")
            Japan = self.driver.find_element_by_xpath("//a[text()='Japanese']")
            Japan.click()
            logging.info("(Edge)Clicked Japanese..")
            time.sleep(5)

            logging.info("(Edge)#--Switched to popup alert message to accept it--")
            obj = self.driver.switch_to.alert
            logging.info("(Edge)Before clicking Alert")
            time.sleep(2)
            obj.accept()
            logging.info("(Edge)After clicking Alert")
            time.sleep(30)
        except Exception as e:
            logging.exception("(Edge)TestCase:: Successfully switched to 'Japanese' language(inside except) : FAIL")
            logging.exception("(Edge)Issue in func switch_language_toEnglish() - " + str(e))
            logging.exception(traceback.format_exc())
            sys.exit()


    #@unittest.skip("Skipping English")
    def test_switch_language_toEnglish(self):
        logging.info("(Edge)## -- Entering TestCase method 'test_switch_language_toEnglish()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            try:
                logging.info("(Edge)#--Trying locating English 'Dashboard' tab on the page--")
                dashboard_eng = self.driver.find_element_by_xpath("//a[text()='Dashboard']")
                if dashboard_eng:
                    logging.info("(Edge)TestCase:: Successfully switched to 'English' language : PASS")
            except:
                logging.exception("(Edge)#--Trying locating Japanese 'Dashboard' tab on the page(inside except)--")
                dashboard_jap = self.driver.find_element_by_xpath("//a[text()=r'ダッシュボード']")
                if dashboard_jap:
                    logging.exception("(Edge)Found Japanese, updating language to English")
                    self.switch_language_toEnglish()
                    try:
                        logging.exception("(Edge)#-- Again trying locating English 'Dashboard' tab on the page--")
                        dashboard_eng = self.driver.find_element_by_xpath("//a[text()='Dashboard']")
                        if dashboard_eng:
                            logging.exception("(Edge)TestCase:: Successfully switched to 'English' language : PASS")
                    except:
                        logging.exception("(Edge)TestCase:: Successfully switched to 'English' language(language not changed or Page load issue) : FAIL")

        except Exception as e:
            logging.exception("(Edge)TestCase:: Successfully switched to 'English' language(inside except) : FAIL")
            logging.exception("(Edge)Issue in func switch_language() - " + str(e))
            logging.exception(traceback.format_exc())


    #@unittest.skip("Skipping English")
    def test_switch_language_toJapanese(self):
        logging.info("(Edge)## -- Entering TestCase method 'test_switch_language_toJapanese()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            try:
                logging.info("(Edge)#--Trying locating Japanese 'Dashboard' tab on the page--")
                dashboard_jap = self.driver.find_element_by_xpath("//a[text()=r'ダッシュボード']")
                if dashboard_jap:
                    logging.info("(Edge)TestCase:: Successfully switched to 'Japanese' language : PASS")
            except:
                logging.exception("(Edge)#--Trying locating English 'Dashboard' tab on the page(inside except)--")
                dashboard_eng = self.driver.find_element_by_xpath("//a[text()='Dashboard']")
                if dashboard_eng:
                    logging.exception("(Edge)Found English, updating language to Japanese")
                    self.switch_language_toJapanese()
                    try:
                        logging.exception("(Edge)#-- Again trying locating Japanese 'Dashboard' tab on the page--")
                        dashboard_jap = self.driver.find_element_by_xpath("//a[text()=r'ダッシュボード']")
                        if dashboard_jap:
                            logging.exception("(Edge)TestCase:: Successfully switched to 'Japanese' language : PASS")
                    except:
                        logging.exception("(Edge)TestCase:: Successfully switched to 'Japanese' language(language not changed or Page load issue) : FAIL")

        except Exception as e:
            logging.exception("(Edge)TestCase:: Successfully switched to 'Japanese' language(inside except) : FAIL")
            logging.exception("(Edge)Issue in func switch_language() - " + str(e))
            logging.exception(traceback.format_exc())

    def viewTabs_English(self):
        logging.info("(Edge)## -- Entering 'viewTabs_English()' method -- ##")
        try:
            logging.info("(Edge)#--Accessing English Dashboard Tab--")

            logging.info("(Edge)# --Located and going to click on the Dashboard tab--")
            self.waitByXpath("//a[text()='Dashboard']")
            dashboard = self.driver.find_element_by_xpath("//a[text()='Dashboard']")
            dashboard.click()
            time.sleep(10)

            logging.info("(Edge)# --Locating a heading 'Overall Performance' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//div[@class='col-md-3']"):
                self.driver.save_screenshot(os.path.join(os.getcwd(), "Images", "dashboard_english_edge.png"))
                #self.driver.save_screenshot("dashboard_eng.png")
                logging.info("(Edge)English Dashboard accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Edge)Issue in func test_viewTabs_English(), inside Dashboard Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Edge)# --Accessing English Alerts Tab--")

            logging.info("(Edge)# --Located and going to click on the Alerts tab--")
            time.sleep(3)
            self.waitByXpath("//a[text()='Alerts']")
            alerts = self.driver.find_element_by_xpath("//a[text()='Alerts']")
            alerts.click()
            time.sleep(10)

            logging.info("(Edge)# --Locating a heading 'Alert Status' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//th[text()='Alert Status']"):
                self.driver.save_screenshot(os.path.join(os.getcwd(), "Images", "alerts_english_edge.png"))
                #self.driver.save_screenshot("alerts_eng.png")
                logging.info("(Edge)English Alerts accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Edge)Issue in func test_viewTabs_English(), inside Alerts Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Edge)# --Accessing English Tests Tab--")

            logging.info("(Edge)# --Located and going to click on the Tests tab--")
            time.sleep(3)
            self.waitByXpath("//a[text()='Tests']")
            tests = self.driver.find_element_by_xpath("//a[text()='Tests']")
            tests.click()
            time.sleep(10)

            logging.info("(Edge)# --Locating a heading 'Please select a test' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//span[text()='Please select a test']"):
                self.driver.save_screenshot(os.path.join(os.getcwd(), "Images", "tests_english_edge.png"))
                #self.driver.save_screenshot("tests_eng.png")
                logging.info("(Edge)English Tests accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Edge)Issue in func test_viewTabs_English(), inside Tests Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Edge)# --Accessing English Variables Tab--")

            logging.info("(Edge)# --Located and going to click on the Variables tab--")
            time.sleep(3)
            self.waitByXpath("//a[text()='Variables']")
            tests = self.driver.find_element_by_xpath("//a[text()='Variables']")
            tests.click()
            time.sleep(10)

            logging.info("(Edge)# --Locating a heading 'Please select a variable, or the following:' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//div[text()=' Please select a variable, or the following:']"):
                self.driver.save_screenshot(os.path.join(os.getcwd(), "Images", "variables_english_edge.png"))
                #self.driver.save_screenshot("variables_eng.png")
                logging.info("(Edge)English Variables accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Edge)Issue in func test_viewTabs_English(), inside Variables Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Edge)# --Accessing English Notifications Tab--")

            logging.info("(Edge)# --Located and going to click on the Notifications tab--")
            time.sleep(3)
            self.waitByXpath("//a[text()='Notifications']")
            notifications = self.driver.find_element_by_xpath("//a[text()='Notifications']")
            notifications.click()
            time.sleep(10)

            logging.info("(Edge)# --Locating a heading 'Please select a notification' and clicked on 'test' before taking screenshot--")
            if self.driver.find_element_by_xpath("//span[text()='Please select a notification']"):
                test = self.driver.find_element_by_class_name("nav.nav-sidebar.tests.ng-binding.ng-scope")
                if test:
                    test.click()
                    time.sleep(10)
                    self.driver.save_screenshot(os.path.join(os.getcwd(), "Images", "notifications_english_edge.png"))
                    #self.driver.save_screenshot("notifications_eng.png")
                    logging.info("(Edge)English Notifications accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Edge)Issue in func test_viewTabs_English(), inside Notifications Tab - " + str(e))
            logging.exception(traceback.format_exc())


    def viewTabs_Japanese(self):
        logging.info("(Edge)## -- Entering viewTabs_Japanese() method -- ##")
        try:
            logging.info("(Edge)# --Accessing Japanese Dashboard Tab--")

            logging.info("(Edge)# --Located and going to click on the Dashboard tab--")
            self.waitByXpath("//a[text()=r'ダッシュボード']")
            dashboard = self.driver.find_element_by_xpath("//a[text()=r'ダッシュボード']")
            dashboard.click()
            time.sleep(10)

            logging.info("(Edge)# --Locating a heading 'Overall Performance' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//div[@class='col-md-3']"):
                self.driver.save_screenshot(os.path.join(os.getcwd(), "Images", "dashboard_japanese_edge.png"))
                #self.driver.save_screenshot("dashboard_jap.png")
                logging.info("(Edge)Japanese Dashboard accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Edge)Issue in func test_viewTabs_Japanese(), inside Dashboard Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Edge)# --Accessing Japanese Alerts Tab--")

            logging.info("(Edge)# --Located and going to click on the Alerts tab--")
            time.sleep(3)
            self.waitByXpath("//a[text()=r'アラート']")
            alerts = self.driver.find_element_by_xpath("//a[text()=r'アラート']")
            alerts.click()
            time.sleep(10)

            logging.info("(Edge)# --Locating a heading 'Alert Status' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//th[text()=r'アラートステータス']"):
                self.driver.save_screenshot(os.path.join(os.getcwd(), "Images", "alerts_japanese_edge.png"))
                #self.driver.save_screenshot("alerts_jap.png")
                logging.info("(Edge)Japanese Alerts accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Edge)Issue in func test_viewTabs_Japanese(), inside Alerts Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Edge)# --Accessing Japanese Tests Tab--")

            logging.info("(Edge)# --Located and going to click on the Tests tab--")
            time.sleep(3)
            self.waitByXpath("//a[text()=r'テスト']")
            tests = self.driver.find_element_by_xpath("//a[text()=r'テスト']")
            tests.click()
            time.sleep(10)

            logging.info("(Edge)# --Locating a heading 'Please select a test' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//span[text()=r'テストを選択してください。']"):
                self.driver.save_screenshot(os.path.join(os.getcwd(), "Images", "tests_japanese_edge.png"))
                #self.driver.save_screenshot("tests_jap.png")
                logging.info("(Edge)Japanese Tests accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Edge)Issue in func test_viewTabs_Japanese(), inside Tests Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Edge)# --Accessing Japanese Variables Tab--")

            logging.info("(Edge)# --Located and going to click on the Variables tab--")
            time.sleep(3)
            self.waitByXpath("//a[text()=r'変数']")
            tests = self.driver.find_element_by_xpath("//a[text()=r'変数']")
            tests.click()
            time.sleep(10)

            logging.info("(Edge)# --Locating a heading 'Please select a variable, or the following:' on the page before taking screenshot--")
            if self.driver.find_element_by_xpath("//div[text()=r'変数を選択してください。または、以下のように操作してください。']"):
                self.driver.save_screenshot(os.path.join(os.getcwd(), "Images", "variables_japanese_edge.png"))
                #self.driver.save_screenshot("variables_jap.png")
                logging.info("(Edge)Japanese Variables accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Edge)Issue in func test_viewTabs_Japanese(), inside Variables Tab - " + str(e))
            logging.exception(traceback.format_exc())

        try:
            logging.info("(Edge)# --Accessing Japanese Notifications Tab--")

            logging.info("(Edge)# --Located and going to click on the Notifications tab--")
            time.sleep(3)
            self.waitByXpath("//a[text()=r'通知']")
            notifications = self.driver.find_element_by_xpath("//a[text()=r'通知']")
            notifications.click()
            time.sleep(10)

            logging.info("(Edge)# --Locating a heading 'Please select a notification' and clicked on 'test' before taking screenshot--")
            if self.driver.find_element_by_xpath("//span[text()=r'通知を選択してください。']"):
                test = self.driver.find_element_by_class_name("nav.nav-sidebar.tests.ng-binding.ng-scope")
                if test:
                    test.click()
                    time.sleep(10)
                    self.driver.save_screenshot(os.path.join(os.getcwd(), "Images", "notifications_japanese_edge.png"))
                    #self.driver.save_screenshot("notifications_jap.png")
                    logging.info("(Edge)Japanese Notifications accessed and captured an Image of it..")

        except Exception as e:
            logging.exception("(Edge)Issue in func test_viewTabs_Japanese(), inside Notifications Tab - " + str(e))
            logging.exception(traceback.format_exc())


    #@unittest.skip("Skipping English")
    def test_viewTabs_English(self):
        logging.info("(Edge)## -- Entering TestCase method 'test_viewTabs_English()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            try:
                logging.info("(Edge)#--Trying to locate English 'Dashboard' tab on the page")
                dashboard_eng = self.driver.find_element_by_xpath("//a[text()='Dashboard']")
                if dashboard_eng:
                    self.viewTabs_English()
            except:
                logging.exception("(Edge)#--Trying to locate Japanese 'Dashboard' tab on the page(inside except)")
                dashboard_jap = self.driver.find_element_by_xpath("//a[text()=r'ダッシュボード']")
                if dashboard_jap:
                    logging.exception("(Edge)#--Found Japanese, updating language to English")
                    self.switch_language_toEnglish()
                    self.viewTabs_English()

        except Exception as e:
            logging.exception("(Edge)Issue in func test_viewTabs_English() - " + str(e))
            logging.exception(traceback.format_exc())


    #@unittest.skip("Skipping japanese")
    def test_viewTabs_Japanese(self):
        logging.info("(Edge)## -- Entering TestCase method 'test_viewTabs_Japanese()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            try:
                logging.info("(Edge)#--Trying to locate Japanese 'Dashboard' tab on the page")
                dashboard_jap = self.driver.find_element_by_xpath("//a[text()=r'ダッシュボード']")
                if dashboard_jap:
                    self.viewTabs_Japanese()
            except:
                logging.exception("(Edge)#--Trying to locate English 'Dashboard' tab on the page(inside except)")
                dashboard_eng = self.driver.find_element_by_xpath("//a[text()='Dashboard']")
                if dashboard_eng:
                    logging.exception("(Edge)#--Found English, updating language to Japanese")
                    self.switch_language_toJapanese()
                    self.viewTabs_Japanese()

        except Exception as e:
            logging.exception("(Edge)Issue in func viewTabs_Japanese() - " + str(e))
            logging.exception(traceback.format_exc())


    #@unittest.skip("Skipping English")
    def test_clientInfo_check_english(self):
        logging.info("(Edge)## -- Entering TestCase method 'test_clientInfo_check_english()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            logging.info("(Edge)# --Going to click on Profile dropdown--")
            profile_dropdown = self.driver.find_element_by_link_text('QA_traininguser25(Empirix_QA_Training)')
            profile_dropdown.click()
            time.sleep(5)

            try:
                logging.info("(Edge)# --Going to click on English 'Client' from the dropdown menu--")
                client_eng = self.driver.find_element_by_xpath("//span[text()='Client']")
                if client_eng:
                    client_eng.click()
                    time.sleep(10)
                    logging.info("(Edge)# --Locating a heading 'Client Details' in English on the page before taking screenshot--")
                    if self.driver.find_element_by_class_name('panel-title'):
                        self.driver.save_screenshot(os.path.join(os.getcwd(), "Images", "client_details_english_edge.png"))
                        #self.driver.save_screenshot("client_details_eng.png")
                        logging.info("(Edge)Client Details accessed in English and captured an Image of it..")
                        logging.info("(Edge)TestCase:: Client Details accessed in 'English' Successfully : PASS")
            except:
                logging.exception("(Edge)# --Checking for a Japanese 'Client' from the dropdown menu(inside except)--")
                client_jap = self.driver.find_element_by_xpath("//span[text()=r'クライアント']")
                if client_jap:
                    profile_dropdown.click()
                    time.sleep(5)
                    logging.exception("(Edge)#--Found Japanese, updating language to English")
                    self.switch_language_toEnglish()
                    try:
                        profile_dropdown = self.driver.find_element_by_link_text('QA_traininguser25(Empirix_QA_Training)')
                        if profile_dropdown:
                            profile_dropdown.click()
                            time.sleep(3)
                            logging.exception("(Edge)# --Going to click on English 'Client' from the dropdown menu once language is changed--")
                            client_eng = self.driver.find_element_by_xpath("//span[text()='Client']")
                            if client_eng:
                                client_eng.click()
                                time.sleep(10)
                                logging.exception("(Edge)# --Locating a heading 'Client Details' in English on the page before taking screenshot--")
                                if self.driver.find_element_by_class_name('panel-title'):
                                    self.driver.save_screenshot(os.path.join(os.getcwd(), "Images", "client_details_english_edge.png"))
                                    #self.driver.save_screenshot("client_details_eng.png")
                                    logging.exception("(Edge)Client Details accessed in English and captured an Image of it..")
                                    logging.exception("(Edge)TestCase:: Client Details accessed in 'English' Successfully : PASS")
                    except:
                        logging.exception("(Edge)TestCase:: Client Details accessed in 'English' Successfully(language not changed or Page load issue) : FAIL")

        except Exception as e:
            logging.exception("(Edge)TestCase:: Client Details accessed in 'English' Successfully(inside except) : FAIL")
            logging.exception("(Edge)Issue in func test_clientInfo_check_english() - " + str(e))
            logging.exception(traceback.format_exc())


    #@unittest.skip("Skipping japanese")
    def test_clientInfo_check_japanese(self):
        logging.info("(Edge)## -- Entering TestCase method 'test_clientInfo_check_japanese()' -- ##")
        try:
            self.Empirix_Login()
            time.sleep(2)

            logging.info("(Edge)# --Going to click on Profile dropdown--")
            profile_dropdown = self.driver.find_element_by_link_text('QA_traininguser25(Empirix_QA_Training)')
            profile_dropdown.click()
            time.sleep(3)

            try:
                logging.info("(Edge)# --Going to click on Japanese 'Client' from the dropdown menu--")
                client_jap = self.driver.find_element_by_xpath("//span[text()=r'クライアント']")
                if client_jap:
                    client_jap.click()
                    time.sleep(10)
                    logging.info("(Edge)# --Locating a heading 'Client Details' in Japanese on the page before taking screenshot--")
                    if self.driver.find_element_by_class_name('panel-title'):
                        self.driver.save_screenshot(os.path.join(os.getcwd(), "Images", "client_details_japanese_edge.png"))
                        #self.driver.save_screenshot("client_details_jap.png")
                        logging.info("(Edge)Client Details accessed in Japanese and captured an Image of it..")
                        logging.info("(Edge)TestCase:: Client Details accessed in 'Japanese' Successfully : PASS")
            except:
                logging.exception("(Edge)# --Checking for a English 'Client' from the dropdown menu(inside except)--")
                client_eng = self.driver.find_element_by_xpath("//span[text()='Client']")
                if client_eng:
                    profile_dropdown.click()
                    time.sleep(3)
                    logging.exception("(Edge)#--Found English, updating language to Japanese")
                    self.switch_language_toJapanese()
                    try:
                        profile_dropdown = self.driver.find_element_by_link_text('QA_traininguser25(Empirix_QA_Training)')
                        if profile_dropdown:
                            profile_dropdown.click()
                            time.sleep(3)
                            logging.exception("(Edge)# --Going to click on Japanese 'Client' from the dropdown menu once language is changed--")
                            client_jap = self.driver.find_element_by_xpath("//span[text()=r'クライアント']")
                            if client_jap:
                                client_jap.click()
                                time.sleep(10)
                                logging.exception("(Edge)# --Locating a heading 'Client Details' in Japanese on the page before taking screenshot--")
                                if self.driver.find_element_by_class_name('panel-title'):
                                    self.driver.save_screenshot(os.path.join(os.getcwd(), "Images", "client_details_japanese_edge.png"))
                                    #self.driver.save_screenshot("client_details_jap.png")
                                    logging.exception("(Edge)Client Details accessed in Japanese and captured an Image of it..")
                                    logging.exception("(Edge)TestCase:: Client Details accessed in 'Japanese' Successfully : PASS")
                    except:
                        logging.exception("(Edge)TestCase:: Client Details accessed in 'Japanese' Successfully(language not changed or Page load issue) : FAIL")

        except Exception as e:
            logging.exception("(Edge)TestCase:: Client Details accessed in 'Japanese' Successfully(inside except) : FAIL")
            logging.exception("(Edge)Issue in func test_clientInfo_check_japanese() - " + str(e))
            logging.exception(traceback.format_exc())

    def tearDown(self):
        logging.info("(Edge)## -- Entering tearDown() method -- ##")
        try:
            self.driver.quit()
        except Exception as e:
            logging.exception("(Edge)Issue in func tearDown() - " + str(e))
            logging.exception(traceback.format_exc())


if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test_reports'))


