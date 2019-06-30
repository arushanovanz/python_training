from model.contactproperties import ContactProperties

def test_delete_contact(app):
    # photo path
    # p= os.path.abspath('C:\Users\hh\Pictures\Git.jpeg')
    if app.contact.count() == 0:
        app.contact.create(ContactProperties(firstname="delete check",
                                                      middlename="delete check",
                                                      lastname="delete check",
                                                      nickname="delete check",
                                                      photo= "",
                                                      title="delete check",
                                                      company="delete check",
                                                      address= "Adress2 Company2",
                                                      home="89776000000",mobile="89776000001",
                                                      work="89776000002",
                                                      fax="89776000003",
                                                      email="lev1@tt.ru",email2="lev2@tt.ru",
                                                      email3="lev3@tt.ru",
                                                      homepage="lev.tt.ru",
                                                      address2="New Secondary Adress",
                                                      phone2=" New Secondary Home",
                                                      notes=" some new notes ver 2",
                                                      ayear="1999",amonth="February",aday ="5",
                                                      byear="2001",bmonth="June",bday="17"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    #assert old_contacts == new_contacts

