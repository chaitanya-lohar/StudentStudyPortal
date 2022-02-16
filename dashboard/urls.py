

from django.urls import path
from .import views


urlpatterns=[

    path('',views.home,name="home"),
    path('notes/',views.notes,name="notes"),
    path('delete_note/<int:pkey>',views.delete_note,name="delete-note"),
    path('notes_detail/<int:pkey>',views.NotesDetailView.as_view(),name="notes-detail"),
    path('homework/',views.homework,name="home-work"),
    path('update_homework/<int:pkey>',views.update_homework,name="update-homework"),
    path('delete_homework/<int:pkey>',views.delete_homework,name="delete-homework"),
    path('youtube/',views.youtube,name="youtube"),
    path('todo/',views.todo,name="todo"),
    path('delete_todo/<int:pkey>',views.delete_todo,name="delete-todo"),
    path('update_todo/<int:pkey>',views.update_todo,name="update-todo"),
    path('books',views.books,name="books"),
    path('dictionary',views.dictionary,name="dictionary"),
    path('wiki',views.wiki,name="wiki"),
    path('conversion',views.conversion,name="conversion"),
    
]