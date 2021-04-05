from locators.base_page_locators import BasePageLocator

class LoginPageLocator(BasePageLocator):

       SINGINBUTTON = "//a[contains(text(),'Sign in')]"
       USERNAME = "email"
       PASSWORD= "passwd"
       SUBMITLOGINBUTTON = "SubmitLogin"
       EMAILADDRESS = "email_create"
       SUBMITCREATE = "SubmitCreate"

