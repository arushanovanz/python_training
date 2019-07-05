from selenium.webdriver.support.select import Select
from model.contactproperties import ContactProperties

class ContactHelper:

    def __init__(self,app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contactproperties):
        wd = self.app.wd
        # search form element
        wd.find_element_by_name("searchform").click()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contactproperties)
        wd.find_element_by_xpath("//form[@name='theform']//input[@name='submit']").click()
        self.contact_cash = None

    def fill_contact_form(self, contactproperties):
        wd = self.app.wd
        self.change_field_value("firstname",contactproperties.firstname)
        self.change_field_value("middlename", contactproperties.middlename)
        self.change_field_value("lastname", contactproperties.lastname)
        self.change_field_value("nickname", contactproperties.nickname)
        self.change_field_value("title", contactproperties.title)
        self.change_field_value("company", contactproperties.company)
        self.change_field_value("address", contactproperties.address)
        self.change_field_value("home", contactproperties.home)
        self.change_field_value("mobile", contactproperties.mobile)
        self.change_field_value("work", contactproperties.work)
        self.change_field_value("fax", contactproperties.fax)
        self.change_field_value("email", contactproperties.email)
        self.change_field_value("email2", contactproperties.email2)
        self.change_field_value("email3", contactproperties.email3)
        self.change_field_value("homepage", contactproperties.homepage)
        self.change_field_value("address2", contactproperties.address2)
        self.change_field_value("notes", contactproperties.notes)
        #    wd.find_element_by_name("photo").click()
        #    wd.find_element_by_name("photo").clear()
        #    wd.find_element_by_name("photo").send_keys(contactproperties.photo)

        # edit birthday
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contactproperties.bday)

        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contactproperties.bmonth)

        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys(contactproperties.byear)

        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contactproperties.aday)

        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contactproperties.amonth)

        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys(contactproperties.ayear)

    def delete_first_contact(self):
        wd = self.app.wd
        wd.delete_contact_by_index(0)
        # self.return_to_home_page()
        # wd.find_element_by_name("selected[]").click()
        # # submit deletion
        # wd.find_element_by_xpath("//div[contains(@class,'left')]//input[contains(@onclick, 'DeleteSel()')]").click()
        # wd.switch_to_alert().accept()
        # wd.find_element_by_css_selector("div.msgbox")
        # self.return_to_home_page()
        # self.contact_cash = None

    def select_contact_by_index(self,index):
        wd =self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[contains(@class,'left')]//input[contains(@onclick, 'DeleteSel()')]").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.return_to_home_page()
        self.contact_cash = None

    def edit_first_contact(self,new_contactproperties_data):
        wd = self.app.wd
        self.return_to_home_page()
        self.edit_contact_by_index(0)
        # # find edit button
        # wd.find_element_by_xpath("//a/img[contains(@title[1],'Edit')]").click()
        # # edit contact firm
        # self.fill_contact_form(new_contactproperties_data)
        # # submit edit contact
        # wd.find_element_by_xpath("//form//input[@name='update']").click()
        # self.contact_cash = None

    def edit_contact_by_index(self,new_contactproperties_data,index):
        wd = self.app.wd
        self.return_to_home_page()
        # find edit button
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//a/img[contains(@title[1],'Edit')]").click()
        # edit contact firm
        self.fill_contact_form(new_contactproperties_data)
        # submit edit contact
        wd.find_element_by_xpath("//form//input[@name='update']").click()
        self.contact_cash = None


    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") or wd.current_url.endswith("/addressbook/index.php")
                or wd.find_elements_by_xpath("//div//input[contains(@title, 'Search for any text')]")):
           wd.get("http://localhost/addressbook/")

    contact_cash = None

    def get_contact_list(self):
       if  self.contact_cash is None:
           wd = self.app.wd
           self.return_to_home_page()
           self.contact_cash = []
           for wd.element in wd.find_elements_by_xpath("//tr[@name='entry']"):
               container = wd.element.find_elements_by_tag_name('td')
               lastname = container[1].text
               firstname = container[2].text
               id = container[0].find_element_by_name("selected[]").get_attribute("value")
               self.contact_cash.append (ContactProperties(lastname=lastname, firstname=firstname, id=id))
       return list(self.contact_cash)