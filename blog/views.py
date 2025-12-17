# blog/views.py
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import BlogPost, Tag

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 5  # production-friendly

    def get_queryset(self):
        queryset = BlogPost.objects.filter(published=True)
        tag_slug = self.kwargs.get('tag_slug')

        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)

        return queryset.select_related('author').prefetch_related('tags')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context



class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class BlogCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'content', 'image', 'tags', 'published']
    template_name = 'blog/blog_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
