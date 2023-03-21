from django.shortcuts import render

# Create your views here.
def index(request):
  '''The home page for Learning Diary.'''
  return render(request, 'learning_diary/index.xhtml')