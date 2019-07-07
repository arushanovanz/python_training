from model.group import Group
from random import randrange

def test_edit_group_name(app):
    if app.group.count() ==0:
        app.group.create(Group(name="test edit group"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Новая модифицированная группа2")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_edit_group_header(app):

    if app.group.count() ==0:
        app.group.create(Group(header="New edited Header"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(header="New edited Header")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index,group)
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert len(old_groups) == app.group.count()
 #   assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_edit_group_footer(app):
    group = Group(footer="New edited footer")
    if app.group.count() ==0:
        app.group.create(Group(footer="New edited footer"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index,group)
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert len(old_groups) == len(new_groups)
 #   assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)