from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage,name='index'),
    path('add',insert,name='add'),
    path('cancel/<int:id>',cancel_record, name="cancel_record"),
    path('alter/<int:id>',alter_record,name="alter_record")
]

