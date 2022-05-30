from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GigCreateForm
from .models import Gig
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, \
                                  PageNotAnInteger
from django.views.generic import (
    ListView,
    DetailView,
    RedirectView,
    UpdateView
)


def gig_view(request):
    "A view to display all the gigs"
    gigs = Gig.objects.all()
    context = {'gigs': gigs}
    return render(request, 'home.html', context)



class GigDetailView(DetailView):
    model = Gig
    template_name = "gigs/gig/detail.html"



@login_required
def create_gig(request):
    if request.method == 'POST':
        # form is sent
        form = GigCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            # prevents the data from being saved to the database yet
            new_item = form.save(commit=False) 

            # assign current user to the item
            new_item.user = request.user
            new_item.save() # now saves the gig object to the database
            messages.success(request, 'Gig added successfully')

            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by thr bookmarklet vial GET
        form = GigCreateForm(data=request.GET)

    return render(request,
                  'gigs/gig/create.html',
                  {'section': 'gigs',
                   'form': form})


# def gig_detail(request, id, slug):
#     gig = get_object_or_404(Gig, id=id, slug=slug)
#     return render(request,
#                   'gigs/gig/detail.html',
#                   {'section': 'gigs',
#                   'gig': gig})
