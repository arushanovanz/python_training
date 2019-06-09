from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.initialization import Initialization

class Application:

      def __init__(self):
          self.wd = WebDriver()
          self.wd.implicitly_wait(60)

      def tearDown(self):
          self.wd.quit()

      def return_to_home_page(self):
          wd = self.wd
          # return to home page
          wd.find_element_by_link_text("home page").click()

      def init (self):
          self.session = Initialization
          self.group= Initialization
          self.contact= Initialization

      def open_home_page(self):
           wd = self.wd
           wd.get("http://localhost/addressbook/")

      def destroy(self):
          self.wd.quit()