from django.urls import path, include
from django.contrib import admin
from . import views
urlpatterns=[
    path('admin/',admin.site.urls),
    path('',views.index,name='index'),
    
    #show all topics
    path('topics/',views.topics,name='topics'),
    #detail page for single topic
    path('topics/?<topic_id>',views.topic,name='topic'),
    #page for adding new topic
    path('new_topic/',views.new_topic,name='new_topic'),
    #page for adding new entry
    path('new_entry/?<topic_id>',views.new_entry,name='new_entry'),
    #edit entry
    path('edit_entry/?<entry_id>',views.edit_entry,name='edit_entry')
]

    
