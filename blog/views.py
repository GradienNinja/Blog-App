from django.shortcuts import render,redirect,get_object_or_404 
from .models import Post 
from .forms import PostForm 
# Create your views here.

def home(request):
  post = Post.objects.all()
  return render(request,'blog/index.html',{"posts" : post})
  

def create_post(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = PostForm()
  return render(request,'blog/create.html',{'form':form})
  
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit.html', {'form': form})