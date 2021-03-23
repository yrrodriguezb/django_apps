from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from common.decorators.http import ajax_required
from .models import Image
from .forms import ImageCreateForm


class ImageListView(ListView):
    model = Image
    paginate_by = 20
    template_name = 'images/image/list.html'
    context_object_name = 'images'


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # If the request is AJAX and the page is out of range
            # return an empty page
            return HttpResponse('', status=404)
        # If page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request, 'images/image/list_ajax.html', { 'images': images })
    return render(request,'images/image/list.html',{ 'images': images })


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html', { 'form': form })


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    like_image_user = image.users_like.filter(username=request.user.username).exists()
    return render(request, 'images/image/detail.html', { 'image': image, 'like_image_user': like_image_user })


@ajax_required
@login_required
@require_POST
def image_like(request):
    from json import loads
    post_data = dict(loads(request.body.decode("utf-8")))
    image_id = post_data.get('id')
    action = post_data.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            elif action == 'unlike':
                image.users_like.remove(request.user)
            likes = image.users_like.count()
            return JsonResponse({ 'code': 200,  'status':'ok', 'likes': likes })
        except:
            pass
    return JsonResponse({ 'code': 500, 'status': 'error' })