from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

      def __init__(self):
          self.wd = WebDriver()
          self.wd.implicitly_wait(60)
          self.session = SessionHelper (self)
          self.group = GroupHelper (self)
          self.contact = ContactHelper(self)

      def is_valid(self):
          try:
              self.wd.current_url
              return True
          except:
              return False

      def tearDown(self):
          self.wd.quit()

      def return_to_home_page(self):
          wd = self.wd
          # return to home page
          wd.find_element_by_link_text("home page").click()

      def open_home_page(self):
           wd = self.wd
           wd.get("http://localhost/addressbook/")

      def destroy(self):
          self.wd.quit()


