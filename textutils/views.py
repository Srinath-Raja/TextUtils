from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Home")
    params = {'name': 'srk', 'place': 'Vadodara'}
    return render(request, 'index.html', params)


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    params = {}
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_-'''
    if removepunc == 'on':
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'remove punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (fullcaps == 'on'):
        analyzed = ""
        analyzed = djtext.upper()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            #print("here",char)
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
                params = {'purpose': 'new line remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (spaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
                params = {'purpose': 'space remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcounter == 'on'):
        analyzed = ""
        analyzed = 'Number of characters in your text is ' + str(len(djtext))
        params = {'purpose': 'count characters', 'analyzed_text': analyzed}

        djtext = analyzed

    if(removepunc!='on' and newlineremover!='on' and fullcaps!='on' and charcounter!='on' and spaceremover!='on'):
        return HttpResponse("Select one option")
    return render(request, 'analyze.html', params)
