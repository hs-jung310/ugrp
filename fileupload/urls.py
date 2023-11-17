from django.urls import path
from . import views

urlpatterns = [
	path('fileupload/', views.fileUpload, name="fileupload"),
	path('fileupload/generate/', views.generate, name="generate"),
	path('fileupload/loading/',views.loading, name="loading"),
	path('fileupload/result/', views.result, name="result")
]


