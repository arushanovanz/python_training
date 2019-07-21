from model.contactproperties import ContactProperties
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts ", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n= 1
f= "data/contacts.json"

for o, a in opts:
    if o =="-n":
        n =int (a)
    elif o == "-f":
        f=a



def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_month():
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return random.choice(months)

def random_phones(prefix,maxlen):
    symbols =  string.digits
    # + string.punctuation
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
            for i in range(n)
            ]



file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",f)

with open(file,"w") as out:
     jsonpickle.set_encoder_options ("json",indent =2)
     out.write(jsonpickle.encode(testdata))




file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",f)

with open(file,"w") as out:
     jsonpickle.set_encoder_options ("json",indent =2)
     out.write(jsonpickle.encode(testdata))