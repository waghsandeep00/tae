from locators.base_page_locators import BasePageLocator


class LoginPageLocator(BasePageLocator):

       SINGINBUTTON = "//button[.//div[contains(text(),'How it works')]]"
       USERNAME = "email"
       PASSWORD= "passwd"
       SUBMITLOGINBUTTON = "SubmitLogin"
       EMAILADDRESS = "email_create"
       SUBMITCREATE = "SubmitCreate"

