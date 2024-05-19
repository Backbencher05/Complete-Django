from django.shortcuts import render, get_object_or_404
from blog.models import Post


# Create your views here.
# let first create FBV
def post_list_view(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post_list':post_list})


def post_detail_view(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    # I want to get partiicular, post based on the year, month and day 
    # and based on the post
    # ex: 2019/09/29/indian-cricket-team-info
    # based on this information I am providing, can you get the post and 
    # sent it to postdetail.html page 
     
    # its same as 
    # employee = Employee.objects.get(eno =101)
    # employee = get_object_or_404(Employee, eno=101)
    return render(request, 'blog/post_detail.html', {'post': post})
                            