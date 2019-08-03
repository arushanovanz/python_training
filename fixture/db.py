import mysql.connector
from model.contactproperties import ContactProperties
from model.group import Group

class Dbfixture:

    def __init__(self,host,name,user,password):
        self.host=host
        self.name=name
        self.user=user
        self.password=password
        self.connection = mysql.connector.connect(host=host,database=name,user=user,password=password,autocommit=True)

    def get_group_list(self):
        list=[]
        cursor= self.connection.cursor()
        try:
            cursor.execute("select group_id,group_name,group_header,group_footer from group_list")
            for row in cursor:
                (id,name,header,footer) =row
                list.append(Group(id=str(id),name=name,header=header,footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_in_group(self,id_group):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                                   select id,firstname,lastname,middlename,nickname,title,company,address,
                                   home,mobile,work,fax,email,email2,email3,homepage,bday,bmonth,byear,
                                   aday,amonth,ayear,address2,phone2,notes
                                   from addressbook where deprecated='0000-00-00 00:00:00' and group_id='%s' """%id_group)
            for row in cursor:
                (id, firstname, lastname, middlename, nickname, title, company, address,
                 homephone, mobilephone, workphone, fax, email, email2, email3, homepage, bday, bmonth, byear,
                 aday, amonth, ayear, address2, secondaryphone, notes) = row
                list.append(ContactProperties(id=str(id), firstname=firstname, lastname=lastname,
                                              middlename=middlename, nickname=nickname, title=title, company=company,
                                              address=address,
                                              homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                                              fax=fax,
                                              email=email, email2=email2, email3=email3, homepage=homepage, bday=bday,
                                              bmonth=bmonth, byear=byear,
                                              aday=aday, amonth=amonth, ayear=ayear, address2=address2,
                                              secondaryphone=secondaryphone, notes=notes
                                              ))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list=[]
        cursor= self.connection.cursor()
        try:
            cursor.execute("""
                           select id,firstname,lastname,middlename,nickname,title,company,address,
                           home,mobile,work,fax,email,email2,email3,homepage,bday,bmonth,byear,
                           aday,amonth,ayear,address2,phone2,notes
                           from addressbook where deprecated='0000-00-00 00:00:00'
                           """)
            for row in cursor:
                (id,firstname,lastname,middlename,nickname,title,company,address,
                           homephone,mobilephone,workphone,fax,email,email2,email3,homepage,bday,bmonth,byear,
                           aday,amonth,ayear,address2,secondaryphone,notes) =row
                list.append(ContactProperties(id=str(id),firstname=firstname,lastname=lastname,
                               middlename=middlename, nickname=nickname, title=title, company=company, address=address,
                               homephone=homephone, mobilephone=mobilephone, workphone=workphone, fax=fax,
                               email=email,email2=email2,email3=email3,homepage=homepage, bday=bday, bmonth=bmonth,byear= byear,
                               aday=aday, amonth=amonth, ayear=ayear, address2=address2, secondaryphone=secondaryphone, notes=notes
                ))
        finally:
            cursor.close()
        return list


    def get_groups_with_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select DISTINCT group_id from address_in_groups")
            for row in cursor:
                (id)=row
                list.append(Group(id=str(id)))
        finally:
         cursor.close()
        return list

    def get_contact_by_id(self,id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""select id,firstname,lastname,middlename,nickname,title,company,address,
                                  home,mobile,work,fax,email,email2,email3,homepage,bday,bmonth,byear,
                                  aday,amonth,ayear,address2,phone2,notes
                                  from addressbook where deprecated='0000-00-00 00:00:00' and id='%s' """ %id)
            (id, firstname, lastname, middlename, nickname, title, company, address,
                 homephone, mobilephone, workphone, fax, email, email2, email3, homepage, bday, bmonth, byear,
                 aday, amonth, ayear, address2, secondaryphone, notes) = cursor.fetchone()

            contact = (ContactProperties(id=str(id), firstname=firstname, lastname=lastname,
                                              middlename=middlename, nickname=nickname, title=title, company=company,
                                              address=address,
                                              homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                                              fax=fax,
                                              email=email, email2=email2, email3=email3, homepage=homepage, bday=bday,
                                              bmonth=bmonth, byear=byear,
                                              aday=aday, amonth=amonth, ayear=ayear, address2=address2,
                                              secondaryphone=secondaryphone, notes=notes
                                              ))
        finally:
            cursor.close()
        return contact

    def destroy(self):
         self.connection.close()