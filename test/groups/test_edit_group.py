from model.group import Group

def test_edit_group_name(app):
    app.group.edit_first_group(Group(name="Новая группа2"))

def test_edit_group_header(app):
    app.group.edit_first_group(Group(header="New Header"))
