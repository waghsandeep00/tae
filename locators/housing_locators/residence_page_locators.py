from selenium.webdriver.common.by import By


class ResidencePageLocators:
    RESIDENTIALBUTTON = "//div[@class='toggle-label' and text()='Residential']"
    COMMERCIALBUTTON = "//div[@class='toggle-label'][text()='Commercial']"
    PROPERTY_LABEL = "//div[@class='property-type-label'] [text()='Office'] "
    RENT = "//div[@class='toggle-label' and text()='Rent']"
    SELL = "//div[@class='toggle-label' and text()='Sell']"
    COUNTRY_CODE = "//div[@class='country-code']/span[text()='+91']"
    ENTER_MOBILE1 = "//div[contains(@class, 'material-input dropdownContainer') " \
                    "and .//text()='Enter Phone Number']"
    ENTER_MOBILE = "//input[@type='tel']"
    ENTER_NAME = "//input[@type='text']"
    SELECT_CITY2 = "//div[@class='country-code']/span[text()='Pune']"
    SELECT_CITY = "//*[@id='app-root']/div/div/div/div[2]/div/div[2]/div/div[5]/div/div/div/input"
    SELECT_CITY1 = "//input[contains(@value, 'Pune')]"
    START_NOW = "//button[@class='new-btn secondary  login large' and text()='Next, add address & price']"
    START_NOW2 = "//*[@id='app-root']/div/div/div/div[2]/div/div[2]/div/div[6]/button"
    START_NOW1 = "new-btn secondary  login large"
    SCROLL_BAR = (By.XPATH, "//span[@class='css-yhp13m']")
    APARTMENT = "//div[@class='property-type-label' and text()='Apartment']"
    BUILDING = "//input[@type='text']"
    MOVETOBUILDING = "//ul[@class='result-cont']/li"
    LOCALITY = "//*[@id='app-root']/div/div/section/div[2]/div[2]/div/div/div[1]/div[3]/div/div[1]/input"
    MOVETOLOCALITY = "//*[@id='app-root']/div/div/section/div[2]/div[2]/div/div/div[1]/div[3]/div/div[1]/ul/li[1]"
    BHK = "//div[@class= 'apartment-type' and text()='2 BHK']"
    BUILDUP = "//*[@id='app-root']/div/div/section/div[2]/div[2]/div/div/div[1]/div[5]/div/input"
    FURNISHTYPE = "//span[text()='Unfurnished']"
    CHECKBOX = "//i[@class='icon-checkbox']"
    NEXTBUTTON = "//button[@class='selfupload-cta-button css-1olr0sc']"
    PROPERTYCOMPLETED = "//div[@class = 'pill-state css-1uhdbu5' and text()='Completed']"
    MONTHLYRENT = "//*[@id='app-root']/div/div/section/div[2]/div[2]/div/div/div[1]/div[1]/div/input"
    AVAILABLEFROM= "//*[@id='app-root']/div/div/section/div[2]/div[2]/div/div/div[1]/div[2]/div/div/input"
    DATE = "//div[@class='pmu-saturday pmu-button' and text()='9']"
    SECURITYDEPOSIT = "//div[@class='toggle-label' and text()='1 month']"

