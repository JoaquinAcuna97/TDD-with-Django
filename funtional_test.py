from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest


class HomePageTest(unittest.TestCase):
    def setUp(self):
        binary = r"C:\Users\Juaco\AppData\Local\Mozilla Firefox\firefox.exe"
        options = Options()
        options.headless = True
        options.binary = binary
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True  # optional
        self.driver = webdriver.Firefox(
            options=options,
            capabilities=cap,
            executable_path="C:\\Users\\Juaco\\.pyenv\\pyenv-win\\versions\\3.7.3\\Scripts\\geckodriver.exe",
        )

    def test_home_page(self):
        self.driver.get("http://127.0.0.1:8000/")
        assert "Django" in self.driver.title

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
