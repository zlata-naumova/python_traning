# from model.contact import Contact
# from random import randrange
#
# def test_delete_some_contact(app):
#     if app.contact.count()==0:
#         app.contact.create(Contact(firstname="test"))
#     #old_contacts = app.contact.get_contacts_list()
#     #index = randrange(len(old_contacts))
#     app.contact.delete_contact_by_index(0)#index)
#     #new_contacts = app.contact.get_contacts_list()
#     #assert len(old_contacts) - 1 == len(new_contacts)
#     #old_contacts[index:index+1]=[]
#     #assert old_contacts == new_contacts