import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.LoginUtils import LoginUtils
from utils.Utils import Utils
from utils.UserUtils import UserUtils

url = "http://localhost"
username = "user"
password = "bitnami"

class CreateUserTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        Utils.setConfig(self.driver, url)
        LoginUtils.login(username, password)
        
    def tearDown(self) -> None:
        self.driver.implicitly_wait(1)
        self.driver.close()
        
    def test_1(self) -> None:
        res = UserUtils.createUser(
            "user1",
            "Password123-",
            "user",
            "1",
            "user1@gmail.com"
        )
        self.assertTrue(res)
        
    def test_2(self):
        res = UserUtils.createUser(
            "user2",
            "Password123-",
            "user",
            "2",
            "user2@gmail.com"
        )
        self.assertTrue(res)

    def test_3(self):
        res = UserUtils.createUser(
            "user3",
            "Password123-",
            "user",
            "3",
            "user3@gmail.com"
        )
        self.assertTrue(res)

    def test_4(self):
        res = UserUtils.createUser(
            "user4",
            "Password123-",
            "user",
            "4",
            "user4@gmail.com"
        )
        self.assertTrue(res)

    def test_5(self):
        res = UserUtils.createUser(
            "user5",
            "Password123-",
            "user",
            "5",
            "user5@gmail.com"
        )
        self.assertTrue(res)
        
if __name__=="__main__":
    unittest.main()