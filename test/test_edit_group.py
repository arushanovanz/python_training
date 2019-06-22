from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group_name(Group(name="Новая группа"))
    app.session.logout()

# def test_edit_group_header(app):
#     app.session.login(username="admin", password="secret")
#     app.group.edit_first_group_name(Group(header="New Header"))
#     app.session.logout()