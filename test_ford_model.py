import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import ford_models as f_m

class TestFordCLK:
    driver = ''
    search_model = f_m
    menu_pth = './/div[@class="flyout-container flyout-mbl-only presentation-only-lg"]//button[@id="brand-nav-vm-seg2-btn"]'

    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.ford.com/")
    #
    @pytest.mark.parametrize('srch_path1, srch_url1', [
        (f_m.f150_path, f_m.f150_url),
        (f_m.maverick_path, f_m.maverick_url),
    ])
    def test_click_model(self, srch_path1, srch_url1):
        # First press
        menu = self.driver.find_element(By.XPATH, self.menu_pth)
        self.driver.execute_script("arguments[0].click();", menu)
        # Second press
        clk1 = self.driver.find_element(By.XPATH, srch_path1)
        self.driver.execute_script("arguments[0].click();", clk1)
        # Comparing url
        act_link = self.driver.current_url
        expected_link = str(srch_url1)


        # Asserts
        assert str(act_link) == str(
            expected_link), f"Expected to see: [{expected_link}] link, but actual link: [{act_link}]"
        #
            # str(act_txt) == str(
            # expected_text), f"Expected to see {expected_text} link, but actual links: '{act_txt}'"

    def teardown_method(self):
        self.driver.quit()
