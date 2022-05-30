from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GigCreateForm
from .models import Gig
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, \
                                  PageNotAnInteger
from django.views.generic import (
    ListView,
    DetailView,
    RedirectView,
    UpdateView
)

# class GigListView(ListView):
#     model = Gig
#     template_name = "home.html"

def gig_view(request):
    gigs = Gig.objects.all()
    context = {'gigs':gigs}
    return render(request, 'gig/home.html', context)

# def gig_view(request):
#     """Gig view for all context"""
#     gigs = Gig.objects.all()
#     paginator = Paginator(gigs, 8)
#     page = request.GET.get('page')
#     try:
#         gigs = paginator.page(page)
#     except pageNotAnInteger:
#         # If page is not an integer deliver the first page
#         gigs = paginator.page(1)
#     except EmptyPage:
#         if request.is_ajax():
#             # if the request is AJAX and the page is out of range
#             # return an empty page
#             return HttpResponse('')
#         # if page is out of range deliver last page of results
#         gigs = paginator.page(paginator.num_pages)
#     if request.is_ajax():
#         return render(request,
#                       'gigs/gig/list_ajax.html',
#                       {'section': 'gigs', 'gigs': gigs})
#     return render(request,
#                   'gigs/gig/home.html',
#                   {'section': 'gigs', 'gigs': gigs})




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
