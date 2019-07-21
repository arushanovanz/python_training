from model.contactproperties import ContactProperties
import random

def test_delete_contact(app,check_ui,db):
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
                                                      homephone="89776000000",mobilephone="89776000001",
                                                      workphone="89776000002",
                                                      fax="89776000003",
                                                      email="lev1@tt.ru",email2="lev2@tt.ru",
                                                      email3="lev3@tt.ru",
                                                      homepage="lev.tt.ru",
                                                      address2="New Secondary Adress",
                                                      secondaryphone=" New Secondary Home",
                                                      notes=" some new notes ver 2",
                                                      ayear="1999",amonth="February",aday ="5",
                                                      byear="2001",bmonth="June",bday="17"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=ContactProperties.id_or_max) == sorted(new_contacts,
                                                                               key=ContactProperties.id_or_max)

