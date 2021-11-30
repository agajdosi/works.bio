from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import HttpResponseRedirect

from .forms import Artwork

# Create your views here.
def index(request):
  return TemplateResponse(request, 'portfolio.html', {})


def addArtwork(request):
  if request.method == 'POST':
    form = Artwork(request.POST)
    if form.is_valid():
      return HttpResponseRedirect('/thanks/')

  else:
    form = Artwork()

  return TemplateResponse(request, 'artwork.html', {'form': form})
  