from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Notes
from .forms import NotesForm
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin

def add_like_view(request, pk):
    if request.method == 'POST':
       note = get_object_or_404(Notes, pk=pk)
       note.likes += 1
       note.save()
       return HttpResponseRedirect(reverse("notes.detail", args=(pk,)))
    raise Http404

def change_visibility_view(request, pk):
    if request.method == 'POST':
       note = get_object_or_404(Notes, pk=pk)
       note.is_public  = not note.is_public
       note.save()
       return HttpResponseRedirect(reverse("notes.detail", args=(pk,)))
    raise Http404
    
class NotesDeleteView(DeleteView):
    model = Notes
    template_name = 'notes/notes_delete.html'
    success_url = '/smart/notes'
    
    def get_success_url(self):
        return reverse_lazy('notes.list')

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = '/admin/'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        

class NoteListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/admin/'
    
    def get_queryset(self):
        return self.request.user.notes.all()
    

class NotesDetailView(LoginRequiredMixin,DetailView):
    model = Notes
    context_object_name = 'note'
    
class NotesPublicDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    queryset = Notes.objects.filter(is_public=True)

class PopularNotesListView(ListView):
    model = Notes
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'

def get_queryset(self):
    return super().get_queryset(
    likes_count = Count('likes')).filter(likes_count__gte=1)
    
def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'notes/notes_detail.html', {'note': note})
    