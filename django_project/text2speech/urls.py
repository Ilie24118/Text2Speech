from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import home_page_view, history_page_view, account_page_view

urlpatterns = [
    path("", home_page_view, name="home"),
    path("history/", history_page_view, name="history"),
    path("account/", account_page_view, name="account"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)