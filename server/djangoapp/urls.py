from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view

    # path for contact us view

    # path for registration

    # path for login

    # path for logout

    path(route='', view=views.get_dealerships, name='index'),
    path(route='register', view=views.registration_request, name='register'),
    path(route='dealerdetails', view=views.get_dealer_details, name='dealerdetails'),
    path(route='about', view=views.about, name='aboutt'),
    path(route='contact', view=views.contact, name='contact'),

    path(route = 'login/', view = views.login_request, name='login'),
    path(route = 'logout/', view = views.logout_request, name='logout'),
    # path(route = 'registering/', view = views.registration_request, name='registerfill'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)