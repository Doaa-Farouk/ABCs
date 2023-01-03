
from core.models import *
# Create your tests here.
s = User.objects.get(pk=7)
s.delete()
s.save()