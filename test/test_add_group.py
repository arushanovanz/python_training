# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from fixture.application import Application

# initialize fixture
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):

    app.initialization.session.login( username = "admin",password="secret")
    app.initialization.group.create(Group(name="yfpdfybt uhes",header="header",footer="yjdfz uhef 1"))
    app.initialization.session.logout()

def test_add_empty_group(app):
    app.initialization.session.login(username="admin",password="secret")
    app.initialization.group.create(Group(name=" ",header=" ",footer=" "))
    app.initialization.session.logout()


