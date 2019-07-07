from model.contactproperties import ContactProperties
from random import randrange

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactProperties(firstname="edit check",
                                                      middlename="edit check",
                                                      lastname="edit check",
                                                      nickname="edit check",
                                                      photo= "",
                                                      title="edit check",
                                                      company="edit check",
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
    old_contacts = app.contact.get_contact_list()
    contact = ContactProperties(firstname="Lev",
                                                      middlename="Radeon",
                                                      lastname="Akatiev",
                                                      nickname="kiriill",
                                                      photo= "",
                                                      title="Title2",
                                                      company="Company2",
                                                      address= "Adress2 Company2",
                                                      homephone="89776000000",mobilephone="89776000001",
                                                      workphone="89776000002",
                                                      fax="89776000003",
                                                      email="lev1@tt.ru",email2="lev2@tt.ru",
                                                      email3="lev3@tt.ru",
                                                      homepage="lev.tt.ru",
                                                      address2="edit",
                                                      secondaryphone=" edit Secondary Home",
                                                      notes=" some new notes ver 2",
                                                      ayear="2002",amonth="February",aday ="8",
                                                      byear="2004",bmonth="June",bday="16")
    contact.id = old_contacts[0].id
    index = randrange(len(old_contacts))
    app.contact.edit_contact_by_index(contact,index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
   # assert sorted(old_contacts, key=ContactProperties.id_or_max) == sorted(new_contacts,key=ContactProperties.id_or_max)


# дорабоать пустые поля для ввода дат
def test_edit_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    contact= ContactProperties(firstname="Brown",lastname="Brown New",
                      ayear="1999", amonth="February", aday="5",
                      byear="2001", bmonth="June", bday="17")
    contact.id = old_contacts[0].id
    index = randrange(len(old_contacts))
    app.contact.edit_contact_by_index(contact,index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
  #  assert sorted(old_contacts, key=ContactProperties.id_or_max) == sorted(new_contacts, key=ContactProperties.id_or_max)


def test_edit_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = ContactProperties(firstname="Brown", lastname="Brown New",
                                ayear="1999", amonth="February", aday="5",
                                byear="2001", bmonth="June", bday="17")
    contact.id = old_contacts[0].id
    index = randrange(len(old_contacts))
    app.contact.edit_contact_by_index(contact, 0)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
   # assert sorted(old_contacts, key=ContactProperties.id_or_max) == sorted(new_contacts,
   #                                                                     key=ContactProperties.id_or_max)