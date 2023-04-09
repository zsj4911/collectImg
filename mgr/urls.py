from django.urls import path
from . import task
from . import sign_in_out
from . import person


urlpatterns = [
    path('hello', task.helloworld),
    path('task', task.dispatcher),
    path('add_person', person.add_person),
    path('list_person', person.list_person),
    path('del_person', person.delete_person),

    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),
]
