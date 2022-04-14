from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Rating
from django.db.models import Avg

# create a generic list view of the model
class HomeView(ListView):
    model = Rating
    ordering = ['-ratingnum']

class RatingView(DetailView):
    model = Rating
    template_name = 'rating/bookrating_detail.html'
    ordering = ['-ratingnum']
    paginate_by = 25


class CreateRatingView(CreateView):
    model = Rating
    template_name = 'BookRating.html'
    fields = ['ISBN', 'username', 'ratingnum', 'comment']
    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)




def home_view(request):
    return render(request, 'BookRating.html')


def rating_list(request):
    ratings = Rating.objects.all().order_by('-ratingnum')
    return render(request, 'rating_list.html', {'ratings': ratings})

def avrating_list(request):
    avgrating = Rating.objects.values('ISBN').annotate(avgrate=Avg('ratingnum')).order_by('-avgrate')
    return render(request, 'averageratinglist.html', {'avgrating': avgrating})

