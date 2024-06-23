import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SchedulerEvents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_add_events_to_scheduler(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.get("https://stephenchou1017.github.io/scheduler")
        driver.find_element(By.XPATH, "//span[contains(text(), 'Infinite scroll')]").click()
        driver.find_element(By.XPATH, "//span[contains(text(), 'Month')]").click()
        for tr in range(3, 6):
            for retry in range(0, 10):
                try:
                    driver.find_element(By.XPATH, f"//table[(@class='scheduler-content-table')]/tbody/tr[{tr}]/td[1]").click()
                    break
                except StaleElementReferenceException:
                    driver.refresh()  # recommended step to deal with stale elements
                    driver.find_element(By.XPATH, "//span[contains(text(), 'Month')]").click()
            driver.switch_to.alert.accept()
            wait.until(
                EC.presence_of_element_located((By.XPATH, f"//table[(@class='scheduler-content-table')]/tbody/tr[{tr}]/td[1]/div/a[@class='timeline-event']"))
            )
        current_month_headers = list(map(lambda el: el.accessible_name, driver.find_elements(By.XPATH, "//table[(@class='scheduler-bg-table')]/thead/tr/th")))
        driver.find_element(By.XPATH, "//i[(@class='anticon anticon-right icon-nav')]").click()
        wait.until_not(
            EC.text_to_be_present_in_element((By.XPATH, "//table[(@class='scheduler-bg-table')]/thead/tr/th"), current_month_headers[0])
        )
        for tr in range(3, 6):
            try:
                driver.find_element(By.XPATH, f"//table[(@class='scheduler-content-table')]/tbody/tr[{tr}]/td/div/a[@class='timeline-event']")
                raise Exception("Test failed, newly created events also appear in following month")
            except NoSuchElementException:
                pass
        driver.find_element(By.XPATH, "//i[(@class='anticon anticon-left icon-nav')]").click()
        wait.until(
            EC.text_to_be_present_in_element((By.XPATH, "//table[(@class='scheduler-bg-table')]/thead/tr/th"), current_month_headers[0])
        )
        for tr in range(3, 6):
            try:
                driver.find_element(By.XPATH, f"//table[(@class='scheduler-content-table')]/tbody/tr[{tr}]/td/div/a[@class='timeline-event']")
            except NoSuchElementException:
                raise Exception("Test failed, newly created events are missing")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
