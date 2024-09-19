# views.py

from django.shortcuts import render

def menu(request):
    # No dynamic content yet
    return render(request, 'menu.html', {})

def about(request):
    # Dictionary containing dynamic content for the About page
    about_content = {
        'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."
    }
    # Pass the content to the template
    return render(request, 'about.html', {'content': about_content})
