from locators.base_page_locators import BasePageLocator


class HomePageLocator(BasePageLocator):

    HOW_IT_WORKS = "//button[.//div[contains(text(),'How it works')]]"
    FAQS = "//button[.//div[contains(text(),'FAQs')]]"
    TESTOMONIAL_DESCRIPTION = "//div[contains(@class, 'css-175lis2') and .//text()='I bought the premium plus " \
                              "package to sell my property. I got so many buyers that I could easily finalize the " \
                              "deal at high profit']"
    TESTOMONIAL_PERSON = "//div[@class='css-1q036e2' and text()='Shantanu J']"
    TESTIMOIAL_CITY = "//div[@class='css-18jjomt']/div[text()='Mumbai']"
    TESTOMONIAL_DESCRIPTIONNEXT = "//div[contains(@class, 'css-175lis2') and .//text()='Full value for money, " \
                              "easily saved atleast Rs.15000 by buying a package instead of paying brokerage " \
                              "to find a tenant ']"
    TESTOMONIAL_PERSONNEXT = "//div[contains(@class, 'css-1q036e2') and  .//text()='Prakash P']"
    TESTIMOIAL_CITYNEXT = "//div[contains(@class, 'css-18jjomt') and  .//text()='Bengaluru']"
