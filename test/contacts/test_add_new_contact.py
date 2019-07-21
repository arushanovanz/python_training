# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.contactproperties import ContactProperties


@pytest.mark.parametrize("contact",testdata, ids=[repr (x)for x in testdata])
def test_add_new_contact(app,contact):
    # photo path
    # # p= os.path.abspath('C:\Users\hh\Pictures\Git.jpeg')
        old_contacts = app.contact.get_contact_list()
        app.contact.create(contact)
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) + 1 == app.contact.count()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=ContactProperties.id_or_max) == sorted(new_contacts, key=ContactProperties.id_or_max)
