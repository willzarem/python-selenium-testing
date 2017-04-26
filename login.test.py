import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://doctors-dashboard.herokuapp.com')
        time.sleep(2)
        self.email = self.driver.find_element_by_name('loginFormEmail')
        self.pwrd = self.driver.find_element_by_name('loginFormPass')

    def test_load(self):
        self.assertEqual("Doctores", self.driver.title)

    def test_submit(self):
        self.email.clear()
        self.pwrd.clear()
        self.pwrd.send_keys(Keys.RETURN)
        time.sleep(2)
        assert len(self.driver.find_elements_by_css_selector('.swal2-modal')) == 0
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/button[1]').click()

    def test_error_modal_text(self):
        self.email.send_keys('doctor')
        self.pwrd.send_keys('test')
        self.pwrd.send_keys(Keys.RETURN)
        time.sleep(2)
        assert len(self.driver.find_elements_by_css_selector('.swal2-modal')) > 0

        content = self.driver.find_elements_by_css_selector('.swal2-modal .swal2-content p')
        if len(content) > 0:
            self.assertIn('son incorrectos', content[0].text)
        else:
            assert False

    def tearDown(self):
        self.driver.close()

# driver.quit()

if __name__ == "__main__":
    unittest.main()
