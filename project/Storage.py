from project.models import User

def storage(data):
    # User(username='hulei',password='123456')
    # User.save()
    # User.objects.create(username='hulei',password='123456')
    data =  User.objects.get(username='hulei')
    print(data)
    pass;