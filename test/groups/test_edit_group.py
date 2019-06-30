from model.group import Group

def test_edit_group_name(app):
    if app.group.count() ==0:
        app.group.create(Group(name="test edit group"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="Новая модифицированная группа2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_group_header(app):
    if app.group.count() ==0:
        app.group.create(Group(header="test Header group"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="New edited Header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_group_footer(app):
    old_groups = app.group.get_group_list()
    if app.group.count() ==0:
        app.group.create(Group(footer="test Header footer"))
    app.group.edit_first_group(Group(footer="New edited footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)