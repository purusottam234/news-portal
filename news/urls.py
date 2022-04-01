from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [
    path('',views.home,name='home' ),
    path('<int:id>/detail/',views.detail,name="detail"),
    path('results/', views.search, name='search'),
    path('logout',views.signout,name='signout'),
    path('login/',views.signin,name='signin'),
    path('signup/',views.signup,name ='signup'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    # path('',views.index,name="index"),
    path('registration/',views.registration,name='registration'),
    # path('login/',views.login,name='login'),
    path('cards/',views.cards,name='cards'),
    # path('registrationPage.html/homePage.html',views.homePage),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)