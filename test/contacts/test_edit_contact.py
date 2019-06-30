from model.contactproperties import ContactProperties

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
    contact = ContactProperties(firstname="Lev",
                                                      middlename="Radeon",
                                                      lastname="Akatiev",
                                                      nickname="kiriill",
                                                      photo= "",
                                                      title="Title2",
                                                      company="Company2",
                                                      address= "Adress2 Company2",
                                                      home="89776000000",mobile="89776000001",
                                                      work="89776000002",
                                                      fax="89776000003",
                                                      email="lev1@tt.ru",email2="lev2@tt.ru",
                                                      email3="lev3@tt.ru",
                                                      homepage="lev.tt.ru",
                                                      address2="edit",
                                                      phone2=" edit Secondary Home",
                                                      notes=" some new notes ver 2",
                                                      ayear="2002",amonth="February",aday ="8",
                                                      byear="2004",bmonth="June",bday="16")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    #assert sorted(old_contacts, key=ContactProperties.id_or_max) == sorted(new_contacts,key=ContactProperties.id_or_max)


# дорабоать пустые поля для ввода дат
def test_edit_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    contact= ContactProperties(firstname="Brown",
                      ayear="1999", amonth="February", aday="5",
                      byear="2001", bmonth="June", bday="17")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    #assert sorted(old_contacts, key=ContactProperties.id_or_max) == sorted(new_contacts, key=ContactProperties.id_or_max)
