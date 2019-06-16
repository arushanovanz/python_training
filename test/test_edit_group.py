from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Новая группа", header="ввввв", footer="футер"))
    app.session.logout()