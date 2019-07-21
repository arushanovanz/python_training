from model.group import Group

class GroupHelper:

    def __init__(self,app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        # open group page
        if not (len(wd.find_elements_by_name("new"))>0 and wd.current_url.endswith("/group.php")):
           wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        # init group creation
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cash = None

    def fill_group_form(self,group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_groups_page(self):
        wd = self.app.wd
        # return to group page
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.group_cash = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_first_group(self):
        self.edit_group_by_index(0)

    def edit_group_by_index(self,index,new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        #open edit form
        wd.find_element_by_xpath("//form//input[@name='edit']").click()
        #fill group form
        self.fill_group_form(new_group_data)
        #submit edit changes
        wd.find_element_by_xpath("// form // input[ @ name = 'update']").click()
        self.return_to_groups_page()
        self.group_cash = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len (wd.find_elements_by_name("selected[]"))

    group_cash = None

    def get_group_list(self):
        if self.group_cash is None:
           wd = self.app.wd
           self.open_groups_page()
           self.group_cash = []
           for element in wd.find_elements_by_css_selector("span.group"):
               text = element.text
               id = element.find_element_by_name("selected[]").get_attribute ("value")
               self.group_cash.append (Group(name=text, id=id))
        return list(self.group_cash)

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cash = None

    def select_group_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']"%id).click()

    def edit_group_by_id(self,id,new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # open edit form
        wd.find_element_by_xpath("//form//input[@name='edit']").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit edit changes
        wd.find_element_by_xpath("// form // input[ @ name = 'update']").click()
        self.return_to_groups_page()
        self.group_cash = None