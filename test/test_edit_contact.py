from model.contactproperties import ContactProperties

def test_edit_contact(app):
    app.session.login( username="admin", password="secret")
    # photo path
    # p= os.path.abspath('C:\Users\hh\Pictures\Git.jpeg')
    app.contact.edit_frist_contact(ContactProperties(firstname="Lev", middlename="Radeon", lastname="Akatiev", nickname="kiriill",
                                                      photo= "",title="Title2",
                                                      company="Company2",address= "Adress2 Company2",home="89776000000",mobile="89776000001",
                                                      work="89776000002",fax="89776000003",email="lev1@tt.ru",email2="lev2@tt.ru",
                                                      email3="lev3@tt.ru",homepage="lev.tt.ru",address2="New Secondary Adress",
                                                      phone2=" New Secondary Home",notes=" some new notes ver 2",ayear="1999",amonth="February",aday ="5",
                                                      byear="1985",bmonth="June",bday="17"))
 #   app.return_to_home_page()
    app.session.logout()