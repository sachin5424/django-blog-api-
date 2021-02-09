from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from myBlog import views

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('categories',views.Categories_View,basename='categories')
# router.register('BlogView',views.BlogView,basename='blog')
urlpatterns = [
  # path('',include(router.urls))
  path('categories/',views.Categories_ListCreateAPIView.as_view()),
  path('BlogView/',views.BlogView.as_view()),
  path('BlogView/create/',views.BlogView1.as_view()),
  path('Contact/',views.Contact_Create_View.as_view()),
  path('Contact/<int:pk>',views.Contact_RetrieveUpdateDestroyAPIView.as_view()),
  path('categories/<int:pk>',views.Categories_RetrieveUpdateDestroyAPIView.as_view())
]
