from django.http import HttpResponse
def hello(response):
    return HttpResponse('''Hello
                        This is new Django 
                        project''')