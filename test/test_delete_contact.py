
def test_delete_contact(app):
    app.session.login( username="admin", password="secret")
    # photo path
    # p= os.path.abspath('C:\Users\hh\Pictures\Git.jpeg')
    app.contact.delete_first_contact()
    app.session.logout()