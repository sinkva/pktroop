from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r"^admin/", include(admin.site.urls)),
#     url(r"^account/signup/$", SignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),
    url(r"^profiles/", include("profiles.urls")),
    url(r"^patrols/", include("patrols.urls")),
    url(r"^events/", include("events.urls")),
]

# django-debug-toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "PKTroop - Admin Area"