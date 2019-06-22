
def test_delete_contact(app):
    # photo path
    # p= os.path.abspath('C:\Users\hh\Pictures\Git.jpeg')
    app.contact.delete_first_contact()
