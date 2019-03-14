from django.shortcuts import render, get_object_or_404, redirect
from .models import Posting, Comment

# Create your views here.
def posting_list(request) :
    postings = Posting.objects.order_by('-updated_at')
    return render(request, 'sns/list.html',{
        'postings':postings
    })

def posting_detail(request,posting_id):
    posting = get_object_or_404(Posting,id=posting_id)
    comments = posting.comment_set.order_by('-create_at') #TODO : Dock-typing
    return render(request,'sns/detail.html',{
        'posting':posting,
        'comments':comments
    })

def create_posting(request) :
    if request.method == 'POST' :
        """
        DB에 칼럼을 추가하는 방법
        [1]
        posting = Posting()
        posting.content = request.POST.get('content')
        ...
        posting.save()
        
        [2]
        posting = Posting(content=request.POST.get('content'),...)
        posting.save()

        [3]
        - 이건 save()를 할 필요가 없다.
        posting = Posting.objects.create(
            content=request.POST.get('content'),
            ...)
        """
        posting = Posting.objects.create(
            content=request.POST.get('content'),
            icon= request.POST.get('icon'),
            image=request.FILES.get('image'),
        )

        return redirect('sns:posting_detail', posting.id)
    else :
        return redirect('sns:posting_list')

def create_comment(request, posting_id) :
    posting = get_object_or_404(Posting, id =posting_id)
    if request.method == 'POST':
        comment = Comment()
        comment.posting_id = posting.id
        comment.content = request.POST.get('comment')
        comment.save()
    return redirect('sns:posting_detail',posting_id)