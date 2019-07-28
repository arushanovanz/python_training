import re


def test_all_information_on_home_page(app):
    contact_from_home_page =app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == clear(contact_from_edit_page.address)
    assert contact_from_home_page.all_emails == merge_contact_info_emails(contact_from_edit_page)


def test_compare_information_home_page_db(app,db):
    contacts_from_home_page = app.contact.get_contact_list()
    for contact in contacts_from_home_page:
            assert contact.firstname == db.get_contact_by_id(contact.id).firstname
            assert contact.lastname == db.get_contact_by_id(contact.id).lastname
            assert clear(contact.address) == clear(db.get_contact_by_id(contact.id).address)
            assert contact.all_emails == merge_contact_info_emails(db.get_contact_by_id(contact.id))


def clear(s):
    return re.sub("[() -]","",s)

def merge_contact_info_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email,contact.email2,contact.email3]))))




