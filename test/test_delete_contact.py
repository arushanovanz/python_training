from model.contactproperties import ContactProperties

def test_delete_contact(app):
    app.session.login( username="admin", password="secret")
    # photo path
    # p= os.path.abspath('C:\Users\hh\Pictures\Git.jpeg')
    app.contact.delete_first_contact()
    # (ContactProperties(firstname="Andrew", middlename="Ivanovich", lastname="Lobachev", nickname="green",
    #                                                   photo= "",title="Title1",
    #                                                   company="Company1",address= "Adress1 Company1",home="89779087650",mobile="89779087651",
    #                                                   work="89779087652",fax="89779087653",email="andrew1@tt.ru",email2="andrew2@tt.ru",
    #                                                   email3="andrew3@tt.ru",homepage="andrew.tt.ru",address2="Secondary Adress",
    #                                                   phone2="Secondary Home",notes="some new notes",ayear="1994",amonth="January",aday ="1",
    #                                                   byear="1995",bmonth="November",bday="16"))

    app.session.logout()