from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,\
                                       PermissionRequiredMixin
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    RedirectView,
    UpdateView

)
from .models import Gig


class CreatorMixin(object):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(creator=self.request.user)


# class CreatorEditMixin(object):
#     def form_valid(self, form):
#         form.instance.creator = self.request.user
#         return super().form_valid(form)


class CreatorGigMixin(CreatorMixin,
                    LoginRequiredMixin,
                    PermissionRequiredMixin):
    model = Gig
    fields = ['title', 'price', 'image', 'delivery', 'added_files', \
              'quality', 'colors_included', 'mockups_included', \
              'description',]
    success_url = reverse('gig-list')


# class CreatorGigEditMixin(CreatorGigMixin, CreatorEditMixin):
#     pass


# class ManageGigListView(CreatorGigMixin, ListView):
#     template_name = 'gigs/dashboard.html'


# class CourseCreateView(CreatorGigEditMixin, CreateView):
#     pass


# class CourseUpdateView(CreatorGigEditMixin, UpdateView):
#     pass


# class CourseDeleteView(CreatorGigMixin, DeleteView):
#     pass


class ManageGigList(CreatorGigMixin, ListView):
    '''retrieve only gigs
        created by the current user.'''
    model = Gig
    template_name = "gigs/dashboard.html"
    permission_required = 'gigs.view_gig'
    # context_object_name = "all_gigs_by_user"

    def get_queryset(self):
        '''prevent users from editing, updating, or deleting
           courses they didn't create'''
        qs = super().get_queryset()
        return qs.filter(creator=self.request.user)



def gig_view(request):
    "A view to display all the gigs"
    gigs = Gig.objects.all()
    context = {'gigs': gigs}
    return render(request, 'pages/home.html', context)



class GigDetailView(DetailView):
    '''Detail page for each Gig'''
    model = Gig
    template_name = "gigs/detail.html"


class GigCreateView(LoginRequiredMixin, CreateView):
    '''Requires a user to login
       to add new gig to the database'''
    model = Gig
    fields = ['title', 'price', 'image', 'delivery', 'added_files', \
              'quality', 'colors_included', 'mockups_included', \
              'description',]
    template_name = "gigs/create.html"


    def form_valid(self, form):
        '''Validated a form for the right input'''
        form.instance.creator = self.request.user
        return super().form_valid(form)


class GigUpdateView(UpdateView):
    model = Gig
    fields = {'title', 'price', 'image', 'delivery', 'added_files', \
              'quality', 'colors_included', 'mockups_included', \
              'description',}
    template_name = "gigs/update.html"

