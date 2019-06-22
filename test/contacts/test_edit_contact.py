from model.contactproperties import ContactProperties

def test_edit_contact(app):
    # photo path
    # p= os.path.abspath('C:\Users\hh\Pictures\Git.jpeg')
    app.contact.edit_first_contact(ContactProperties(firstname="Lev",
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
                                                      address2="New Secondary Adress",
                                                      phone2=" New Secondary Home",
                                                      notes=" some new notes ver 2",
                                                      ayear="1999",amonth="February",aday ="5",
                                                      byear="2001",bmonth="June",bday="17"))



# дорабоать пустые поля для ввода дат
def test_edit_contact_firstname(app):
    # photo path
    # p= os.path.abspath('C:\Users\hh\Pictures\Git.jpeg')
    app.contact.edit_first_contact(ContactProperties(firstname="Brown",
                                                      ayear="1999",amonth="February",aday ="5",
                                                      byear="2001",bmonth="June",bday="17"))
