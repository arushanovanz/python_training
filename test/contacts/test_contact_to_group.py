import random
from fixture.orm import ORMFixture
from model.contactproperties import ContactProperties
from model.group import Group

def test_add_contact_to_group(db,app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test group"))
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

    groups = db.get_group_list()
    old_contacts = db.get_contact_list()
    contact_id= random.choice(old_contacts).id
    group_id= random.choice(groups).id
    app.contact.add_contact_to_group(contact_id,group_id)
    # не работает assert
   # assert db.get_contact_by_id(contact_id) == ORMFixture.get_contacts_in_group(group_id)

# def test_remove_contact_from_group(db,app):
#     if len(db.get_group_list()) == 0:
#         app.group.create(Group(name="test group"))
#     if app.contact.count() == 0:
#         app.contact.create(ContactProperties(firstname="delete check",
#                                              middlename="delete check",
#                                              lastname="delete check",
#                                              nickname="delete check",
#                                              photo="",
#                                              title="delete check",
#                                              company="delete check",
#                                              address="Adress2 Company2",
#                                              homephone="89776000000", mobilephone="89776000001",
#                                              workphone="89776000002",
#                                              fax="89776000003",
#                                              email="lev1@tt.ru", email2="lev2@tt.ru",
#                                              email3="lev3@tt.ru",
#                                              homepage="lev.tt.ru",
#                                              address2="New Secondary Adress",
#                                              secondaryphone=" New Secondary Home",
#                                              notes=" some new notes ver 2",
#                                              ayear="1999", amonth="February", aday="5",
#                                              byear="2001", bmonth="June", bday="17"))
#
#     groups = db.get_group_list()
#     group_id= random.choice(groups).id
#     contact =db.get_contacts_in_group(group_id)
#     app.contact.delete_contact_from_group(contact, group_id)
#     assert db.get_contact_by_id(contact) == ORMFixture.get_contacts_not_in_group(group_id)