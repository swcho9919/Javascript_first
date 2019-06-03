from django.shortcuts import render, render_to_response
from .models import Post
from django.http import JsonResponse, HttpResponse
import json
from .forms import PostForm

# Create your views here.
def post_home(request,):
    if request.method == "POST" and request.is_ajax():
        form = PostForm(request.POST)
        post=form.save(commit=False)
        post.save()
        return JsonResponse({"success" : True}, status=200)
    return JsonResponse({"success": False}, status=400)
        # post_text = request.Post.get('the_post')
        # response_data = {}
        # post = Post(text=post_text)
        # post.save()

        # response_data['post.pk'] = post.pk
        # response_data['content'] = post.content

        # return HttpResponse(
        #     json.dumps(response_data),
        #     content_type='application/json',
        # )
def home(request):
    posts = Post.objects.all()
    form = PostForm()
    return render(request, "home.html", {'form':form, 'posts':posts})

def delete(request, post_pk):
    post = Post.objects.get(
        pk=int(QueryDict(request.body).get('postpk')))
    post.delete()
    return HttpResponse
