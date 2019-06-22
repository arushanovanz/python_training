from model.group import Group

def test_edit_group_name(app):
    if app.group.count() ==0:
        app.group.create(Group(name="test edit group"))
    app.group.edit_first_group(Group(name="Новая модифицированная группа2"))

def test_edit_group_header(app):
    if app.group.count() ==0:
        app.group.create(Group(header="test Header group"))
    app.group.edit_first_group(Group(header="New edited Header"))

def test_edit_group_footer(app):
    if app.group.count() ==0:
        app.group.create(Group(footer="test Header footer"))
    app.group.edit_first_group(Group(footer="New edited footer"))