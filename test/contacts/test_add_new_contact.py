# -*- coding: utf-8 -*-

from model.contactproperties import ContactProperties




def test_add_new_contact(app,json_contacts,check_ui,db):
    # photo path
    # # p= os.path.abspath('C:\Users\hh\Pictures\Git.jpeg')
        contact=json_contacts
        old_contacts = db.get_contact_list()
        app.contact.create(contact)
        new_contacts = db.get_contact_list()
        assert len(old_contacts) + 1 == app.contact.count()
        old_contacts.append(contact)
        if check_ui:
           assert sorted(old_contacts, key=ContactProperties.id_or_max) == sorted(new_contacts, key=ContactProperties.id_or_max)
