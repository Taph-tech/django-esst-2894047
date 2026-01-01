from django.urls import path

from . import views


urlpatterns = [
     path('notes/', views.NoteListView.as_view(), name="notes.list"), # Map the /notes URL to the notes list view
     path('notes/<int:pk>/', views.NotesDetailView.as_view(), name= "notes.detail"), # Map the /notes/<pk>/ URL to the note detail view
     path('notes/<int:pk>/edit/', views.NotesUpdateView.as_view(), name= "notes.update"), # Map the /notes/<pk>/edit/ URL to the note update view
     path('notes/<int:pk>/delete/', views.NotesDeleteView.as_view(), name= "notes.delete"), # Map the /notes/<pk>/delete/ URL to the note delete view
     path('popular/', views.PopularNotesListView.as_view(), name='popular_name'), # Map the /popular URL to the popular notes view
     path('notes/new/', views.NotesCreateView.as_view(), name='notes.new'), # Map the /notes/new/ URL to the note creation view
     path('notes/<int:pk>/add_like', views.add_like_view, name='notes.add_like'), # Map the /notes/<pk>/add_like/ URL to the add like view
     path('notes/<int:pk>/change_visibility', views.change_visibility_view, name='notes.change_visibility'), # Map the /notes/<pk>/change_visibility/ URL to the change visibility view
     path('notes/<int:pk>/share', views.NotesPublicDetailView.as_view(), name= "notes.share"), # Map the /notes/public/<pk>/ URL to the public note detail view    
]


