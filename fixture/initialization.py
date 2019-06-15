
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Initialization:

    def __init__(self,session,group,contact):
        self.session = SessionHelper
        self.group = GroupHelper
        self.contact = ContactHelper
