import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yesbroker.settings')
django.setup()
'''
def adddata():
    from main.models import Test
    Test(name='asd', age='18').save()
adddata()
'''