# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
        return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']

    word_list = fulltext.split()

    word_dict = {}

    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    sorted_dict = sorted(word_dict.items(), key=lambda kv: kv[1], reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(word_list), 'sorted_dict': sorted_dict})


def about(request):
    return render(request, 'about.html')