from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import StoryForm, NewCommentForm
from .models import NewsStory, NewsComment, Tag
from django.db.models import Q


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = NewsComment.objects.filter(
            newsStory_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance=self.request.user)

        return data
    
    def post(self, request, *args, **kwargs):
        new_comment = NewsComment(content=request.POST.get('content'),
                                    author=self.request.user,
                                    newsStory_connected=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# def search_results(request):
#     # Get the search query from the user
#     search_query = request.GET.get('q')

#     # If a search query is provided, filter the NewsStory objects accordingly
#     if search_query:
#         news_stories = NewsStory.objects.filter(
#             models.Q(title__icontains=search_query) |  # Filter by title containing the search query
#             models.Q(content__icontains=search_query) |  # Filter by content containing the search query
#             models.Q(author__username__icontains=search_query) |  # Filter by author username containing the search query
#             models.Q(tags__name__icontains=search_query)  # Filter by tags containing the search query
#         ).distinct()
#     else:
#         # If no search query is provided, display all NewsStory objects
#         news_stories = NewsStory.objects.all()

#     context = {
#         'search_query': search_query,
#         'news_stories': news_stories
#     }
#     return render(request, 'news/index.html', context)

def search_results(request):
    if 'q' in request.GET:
        search_query = request.GET['q']
        search_results = NewsStory.objects.filter(
            Q(title__icontains=search_query) |  # Filter by title containing the search query
            Q(content__icontains=search_query) |  # Filter by content containing the search query
            Q(author__username__icontains=search_query) |  # Filter by author's username containing the search query
            Q(tags__name__icontains=search_query)  # Filter by tag names containing the search query
        ).distinct()

        context = {
            'search_query': search_query,
            'search_results': search_results
        }
        return render(request, 'news/search_results.html', context)

    return render(request, 'news/search_results.html')