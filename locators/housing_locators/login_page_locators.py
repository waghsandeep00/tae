from locators.base_page_locators import BasePageLocator


class LoginPageLocator(BasePageLocator):

       STUCK_IN_FORM_ALERT = "//*[@id='portal-modal-root']/div/div/div/div/div/div[1]/i"
       COLLECT_ROLE = "toggle-label" #classname
       SELECT_ROLE = "//div[@class='toggle-label' and text()='Flatmate']"
       SUBMIT_ROLE = "//*[@id='app-root']/div/div/div/div[2]/div/div[2]/div/div[2]/button"
       GO_BACK = "//a[contains(text(), 'Go back')]"
       USERNAME = "//input[@type='tel']"
       CONTINUE = "//button[@class='new-btn secondary  login large']"
       PASSWORD = "//input[@type='password']"
       SUBMIT = "//button[@class='new-btn secondary  login large']"
       NAME = "//div[contains(string(), 'Sandeep wagh')]" \
              "[@class='profile-card--details--name inspectlet-sensitive']"
       MOBILENUMBER = "//div[contains(string(), '9552312095')]" \
                      "[@class='profile-card--details--contact contact-phone inspectlet-sensitive']"
       EMAILADDRESS = "//div[contains(string(), 'sandeep.wagh2012@rediffmail.com')]" \
                      "[@class='profile-card--details--contact inspectlet-sensitive']"

       LOGINHERE = "//span[@class='link' and text()='Login here']"

