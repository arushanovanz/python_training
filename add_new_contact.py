# -*- coding: utf-8 -*-
from selenium import webdriver
import os
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import unittest
from selenium.webdriver.support.select import Select
from contactproperties import ContactProperties

class add_new_contact(unittest.TestCase):
    
    def create_new_contact(self, wd,contactproperties):
        # search form element
        wd.find_element_by_name("searchform").click()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact firm
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contactproperties.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contactproperties.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contactproperties.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contactproperties.nickname)
   #     wd.find_element_by_name("photo").click()
   #     wd.find_element_by_name("photo").clear()
   #    wd.find_element_by_name("photo").send_keys(contactproperties.photo)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contactproperties.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contactproperties.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contactproperties.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contactproperties.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contactproperties.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contactproperties.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contactproperties.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contactproperties.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contactproperties.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contactproperties.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contactproperties.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contactproperties.bday)
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[18]").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contactproperties.bmonth)
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[45]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contactproperties.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contactproperties.aday)
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[3]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contactproperties.amonth)
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[35]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contactproperties.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contactproperties.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contactproperties.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contactproperties.notes)
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()


    def setUp(self):
            self.wd = webdriver.Firefox()
            self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
            wd.get("http://localhost/addressbook/")

    def return_to_home_page(self, wd):
            # return to home page
            wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
            # logout
            wd.find_element_by_link_text("Logout").click()

    def login(self, wd, username, password):
            # login
            wd.find_element_by_name("user").click()
            wd.find_element_by_name("user").clear()
            wd.find_element_by_name("user").send_keys(username)
            wd.find_element_by_name("pass").click()
            wd.find_element_by_name("pass").clear()
            wd.find_element_by_name("pass").send_keys(password)
            wd.find_element_by_xpath("//input[@value='Login']").click()

    def is_element_present(self, how, what):
            try:
                self.wd.find_element(by=how, value=what)
            except NoSuchElementException as e:
                return False
            return True

    def is_alert_present(self):
            try:
                self.wd.switch_to.alert()
            except NoAlertPresentException as e:
                return False
            return True

    def tearDown(self):
        self.wd.quit()

    def test_add_new_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        # photo path
       # p= os.path.abspath('C:\Users\hh\Pictures\Git.jpeg')
        self.create_new_contact(wd, ContactProperties(firstname="Andrew", middlename="Ivanovich", lastname="Lobachev", nickname="green",
                                                          photo= "",title="Title1",
                                                          company="Company1",address= "Adress1 Company1",home="89779087650",mobile="89779087651",
                                                          work="89779087652",fax="89779087653",email="andrew1@tt.ru",email2="andrew2@tt.ru",
                                                          email3="andrew3@tt.ru",homepage="andrew.tt.ru",address2="Secondary Adress",
                                                          phone2="Secondary Home",notes="some new notes",ayear="1994",amonth="January",aday ="1",
                                                          byear="1995",bmonth="November",bday="16"))
        self.return_to_home_page(wd)
        self.logout(wd)



if __name__ == "__main__":
    unittest.main()
