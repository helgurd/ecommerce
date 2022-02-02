from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from payments.views import CancelledView

# views.CancelledView.as_view()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include("users.urls")),
    path('shop/', include("shop.urls")),
    path('paymentscancelled/', CancelledView.as_view()),
    path('payments/', include("payments.urls")),
    path('', include("shop.urls")),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
