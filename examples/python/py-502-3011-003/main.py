# main/views.py
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

def message_list(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_list')
    else:
        form = MessageForm()
    messages = Message.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'main/message_list.html', {
        'messages': messages,
        'form': form,
    })
