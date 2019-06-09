from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.select import Select
from contactproperties import ContactProperties
from fixture.session import SessionHelper

class Application:

      def __init__(self):
          self.wd = WebDriver()
          self.wd.implicitly_wait(60)
          self.session = SessionHelper(self)

      def is_alert_present(self):
          try:
              self.wd.switch_to.alert()
          except NoAlertPresentException as e:
              return False
          return True

      def open_home_page(self):
           wd = self.wd
           wd.get("http://localhost/addressbook/")

      def open_groups_page(self):
           wd = self.wd
           # open group page
           wd.find_element_by_link_text("groups").click()

      def create_new_contact(self, contactproperties):
          wd = self.wd
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
          wd.find_element_by_xpath("//form[@name='theform']//select [@name='bday']").click()
          wd.find_element_by_name("bmonth").click()
          Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contactproperties.bmonth)
          wd.find_element_by_xpath("//form[@name='theform']//select [@name='bmonth']").click()
          wd.find_element_by_name("byear").click()
          wd.find_element_by_name("byear").clear()
          wd.find_element_by_name("byear").send_keys(contactproperties.byear)
          wd.find_element_by_name("aday").click()
          Select(wd.find_element_by_name("aday")).select_by_visible_text(contactproperties.aday)
          wd.find_element_by_xpath("//form[@name='theform']//select [@name='aday']").click()
          wd.find_element_by_name("amonth").click()
          Select(wd.find_element_by_name("amonth")).select_by_visible_text(contactproperties.amonth)
          wd.find_element_by_xpath("//form[@name='theform']//select [@name='amonth']").click()
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
          wd.find_element_by_xpath("//form[@name='theform']//textarea[@name='notes']").click()
          wd.find_element_by_xpath("//form[@name='theform']//input[@name='submit']").click()

      def create_group(self, group):
           wd = self.wd
           self.open_groups_page()
           # init group creation
           wd.find_element_by_name("new").click()
           # fill group firm
           wd.find_element_by_name("group_name").click()
           wd.find_element_by_name("group_name").clear()
           wd.find_element_by_name("group_name").send_keys(group.name)
           wd.find_element_by_name("group_header").click()
           wd.find_element_by_name("group_header").clear()
           wd.find_element_by_name("group_header").send_keys(group.header)
           wd.find_element_by_name("group_footer").clear()
           wd.find_element_by_name("group_footer").send_keys(group.footer)
           # submit group creation
           wd.find_element_by_name("submit").click()

      def tearDown(self):
          self.wd.quit()


      def return_to_groups_page(self):
          wd = self.wd
          # return to group page
          wd.find_element_by_link_text("group page").click()

      def return_to_home_page(self):
          wd = self.wd
          # return to home page
          wd.find_element_by_link_text("home page").click()

      def setUp(self):
          wd = self.wd
          self.wd =WebDriver()
          self.wd.implicitly_wait(60)

      def destroy(self):
          self.wd.quit()