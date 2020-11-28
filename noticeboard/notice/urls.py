from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('post_notice/',views.post_notice,name='post_notice'),
    path('post_success/',views.post_success,name='post_success'),
    path('view_notice/',views.view_notice,name='view_notice'),
    path('view/<int:notice_id>/',views.view,name='view'),
    path('post_notice1/',views.post_notice1,name='post_notice1'),
    path('contact/',views.contact,name='contact'),
    path('faq/',views.FAQ,name='FAQ'),
   # path('home/',views.home,name='home')
]