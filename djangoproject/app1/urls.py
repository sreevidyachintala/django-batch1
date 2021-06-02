from django.urls import path

from app1 import views

urlpatterns = [
	path('dynamic/',views.dynamic),
	path('register/',views.register,name='register'),
	path('display/',views.display,name='display'),
	path('update/<int:id>',views.update,name='update'),
	path('delete/<int:id>',views.delete,name='delete'),
]


