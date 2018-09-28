from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from users.views import (SignupView, SigninView, AccountSettingsView,
ForgotPasswordView)
from notes.views import NoteListView
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # user relates urls
    url('admin/', admin.site.urls),

    url(r'^signup/', SignupView.as_view(), name='signup'),
    url(r'^signin/', SigninView.as_view(), name='signin'),
    url(r'^account/', login_required(AccountSettingsView.as_view()),
        name='account_settings'),
    url(r'^forgot-password/', ForgotPasswordView.as_view(),
        name='forgot_password'),
    url(r'^signout/$', logout,
        {'next_page': '/'}, name='signout'),

    # notes
    url(r'^notes/', include('notes.urls')),
    # pads
    url(r'^pads/', include('pads.urls')),

    url(r'^$', login_required(NoteListView.as_view()), name='home'),
]
