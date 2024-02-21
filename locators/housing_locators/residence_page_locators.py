from selenium.webdriver.common.by import By


class ResidencePageLocators:
    RESIDENTIALBUTTON = "//div[@class='toggle-label' and text()='Residential']"
    COMMERCIALBUTTON = "//div[@class='toggle-label'][text()='Commercial']"
    PROPERTY_LABEL = "//div[@class='property-type-label'] [text()='Office'] "
    RENT = "//div[@class='toggle-label' and text()='Rent']"
    COUNTRY_CODE = "//div[@class='country-code']/span[text()='+91']"
    ENTER_MOBILE1 = "//div[contains(@class, 'material-input dropdownContainer') " \
                    "and .//text()='Enter Phone Number']"
    ENTER_MOBILE = "//input[@type='tel']"
    ENTER_NAME = "//input[@type='text']"
    SELECT_CITY2 = "//div[@class='country-code']/span[text()='Pune']"
    SELECT_CITY = "//*[@id='app-root']/div/div/div/div[2]/div/div[2]/div/div[5]/div/div/div/input"
    SELECT_CITY1 = "//input[contains(@value, 'Pune')]"
    START_NOW = "//button[@class='new-btn secondary  login large' and text()='Start Now']"
    START_NOW2 = "//*[@id='app-root']/div/div/div/div[2]/div/div[2]/div/div[6]/button"
    START_NOW1 = "new-btn secondary  login large"
    SCROLL_BAR = (By.XPATH, "//span[@class='css-yhp13m']")
    APARTMENT = "//div[@class='property-type-label' and text()='Apartment']"

