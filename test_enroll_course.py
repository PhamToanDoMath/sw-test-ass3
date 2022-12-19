import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.LoginUtils import LoginUtils
from utils.Utils import Utils
from utils.EnrollCourseUtils import EnrollCourseUtils

url = "http://localhost"
username = "user"
password = "bitnami"

class CreateUserTest(unittest.TestCase):
    courseId = 1
    sessionId = 1
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        Utils.setConfig(self.driver, url)
        LoginUtils.login(username, password)
        
    def tearDown(self) -> None:
        self.driver.implicitly_wait(1)
        self.driver.close()
        
    def test_1(self) -> None:
        res = EnrollCourseUtils.enrollCourse(["user1@gmail.com"], '2')
        self.assertEqual(res, True)
        
    def test_2(self):
        res = EnrollCourseUtils.enrollCourse(["user2@gmail.com"], '2')
        self.assertEqual(res, True)

    def test_3(self):
        res = EnrollCourseUtils.enrollCourse(["user3@gmail.com", "user4@gmail.com"], '2')
        self.assertEqual(res, True)

    def test_4(self):
        res = EnrollCourseUtils.enrollCourse([], '2')
        self.assertEqual(res, True)

if __name__=="__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    unittest.main(warnings='ignore')