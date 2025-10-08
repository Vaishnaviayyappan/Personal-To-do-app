from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    # If the form is submitted (POST request)
    if request.method == 'POST':
        # Get the title from the submitted form data
        title = request.POST.get('title')
        if title: # Make sure the title is not empty
            # Create a new TodoItem and save it to the database
            TodoItem.objects.create(title=title)
        # Redirect to the same page to prevent form resubmission on refresh
        return redirect('todo_list')

    # If it's a GET request, display the to-do list
    # Get all incomplete to-do items from the database
    items = TodoItem.objects.filter(completed=False)
    
    # Render the HTML template with the list of items
    return render(request, 'todo/todo_list.html', {'items': items})
