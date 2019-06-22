
class GroupHelper:

    def __init__(self,app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        # open group page
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def fill_group_form(self, group):
        wd = self.app.wd

        if group.name is not None:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)

        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def return_to_groups_page(self):
        wd = self.app.wd
        # return to group page
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #submit deletion
        wd.find_element_by_name("delete").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    # self.return_to_groups_page()

    def edit_first_group(self,new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #open edit form
        wd.find_element_by_xpath("//form//input[@name='edit']").click()
        #fill group form
        self.fill_group_form(new_group_data)
        #submit edit changes
        wd.find_element_by_xpath("// form // input[ @ name = 'update']").click()
        self.return_to_groups_page()
