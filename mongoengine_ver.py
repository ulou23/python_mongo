from mongoengine import *
import datetime

connect('baza', host='localhost', port=27017)



class User(Document):
    name=StringField(required=True,max_length=20)
    number=IntField(required=True)

class Note(Document):
    title=StringField(required=True,max_length=20)
    published=DateTimeField(default=datetime.datetime.now)
    user= ReferenceField('User',reverse_delete_rule=CASCADE)

user_1=User(
    name='Love',
    number=23
)

user_1.save()
print(user_1.name)


note_1=Note(
    title='one',
    user=user_1 ,
)

note_1.save()


print(Note.objects.first().user.name )