from model.contactproperties import ContactProperties
import  random


def test_edit_contact(app,check_ui,db):
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
    old_contacts =db.get_contact_list()
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

    contact_to_edit = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact_to_edit.id,contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=ContactProperties.id_or_max) == sorted(new_contacts,
                                                                               key=ContactProperties.id_or_max)


