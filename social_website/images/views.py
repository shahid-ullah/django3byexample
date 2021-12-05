# images/views.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ImageCreateForm


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            new_item = form.save(commit=False)

            # assign current user to the item
            new_item.user = request.user
            new_item.save()
            return HttpResponse("image saved successfully")
    else:
        form = ImageCreateForm(data=request.GET)

    return render(
        request, 'images/image/create.html', {'section': 'images', 'form': form}
    )
