# -*- coding: utf-8 -*-
from group import Group
import pytest
from application import Application


# initialize fixture
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login( username = "admin",password="secret")
    app.create_group(Group(name="yfpdfybt uhes",header="header",footer="yjdfz uhef 1"))
    app.logout()

def test_add_empty_group(app):
    app.login( username="admin",password="secret")
    app.create_group( Group(name=" ",header=" ",footer=" "))
    app.logout()


