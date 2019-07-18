# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.contactproperties import ContactProperties


def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_month():
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return random.choice(months)

def random_phones(prefix,maxlen):
    symbols =  string.digits + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata =[ ContactProperties (firstname=random_string("firstname",20),
                               middlename=random_string("middlename",20),
                               lastname=random_string("lastname",20),
                               nickname=random_string("nickname",10),
                               photo="",
                               title=random_string("title",30),
                               company=random_string("company",30),
                               address=random_string("address",30),
                               homephone=random_phones("",11),
                               mobilephone=random_phones("",11),
                               workphone=random_phones("",11),
                               fax=random_phones("",11),
                               email=random_string("email@",10),
                               email2=random_string("email@",10),
                               email3=random_string("email@",10),
                               homepage=random_string("http://",15),
                               address2=random_string("address2",30),
                               secondaryphone=random_phones("",11),
                               notes=random_string("Notes",40),
                               ayear= random.randint(1945,2019),
                               amonth= random_month(),
                               aday =random.randint(1,31),
                               byear= random.randint(1945,2019),
                               bmonth= random_month(),
                               bday=random.randint(1,31)
                               )
             for i in range(5)
            ]


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
