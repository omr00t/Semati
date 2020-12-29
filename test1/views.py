from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
import re


from .helper import get_all_book_questions, get_result

def index(request):
    return render(request, "index.html", {})
def take_test(request, test_id):
    """
    Test IDs: 
    1. Grade 9 - males.
    2. Grade 10- males.
    3. Grade 11- males.
    4. Grade 12- males.

    5. Grade 9 - females.
    6. Grade 10- females.
    7. Grade 11- females.
    8. Grade 12- females.
    """
    context = {}
    # Males:
    if(test_id >= 1 and test_id <= 8):
        pass
    else:
        raise Http404()

    if(request.method == "POST"):
        # I probably need perform checks here...
        request.session['post_data'] = request.POST
        request.session['test_type'] = test_id
        request.session['full_url'] = request.build_absolute_uri(reverse('take_test', args=[test_id]))
        return HttpResponseRedirect(reverse("show_result", args=[]))

    context.update({"questions":get_all_book_questions(), "test_id": test_id})
    return render(request, "take_test.html", context)


def show_result(request):
    context = {}
    post_data = str(request.session.get('post_data'))[91:]  # [91:] to execlude the CSRF token..
    full_url  = request.session.get('full_url')
    answered_questions = re.findall('q[0-9][0-9]?', post_data)
    try:
        test_id   = int(request.session.get('test_type'))
    except TypeError:
        raise Http404() 
    if(answered_questions):
        context.update({'answered': True})
        personalities = get_result(answered_questions, test_id) 
        # Modify personalities list to be a separate list containing personalities only:
        personalities = list(personalities.keys() )
        # This holds first letters of each personality:
        personalities_result_letters = personalities[0].personality_letter + ' ' + \
                                       personalities[1].personality_letter + ' ' + \
                                       personalities[2].personality_letter
        context.update({"personalities": personalities, "personalities_result_letters": personalities_result_letters})
        return render(request, "take_test.html", context)
    else:
        context.update({"noAnswersReceived": True, "full_url": full_url})
        return render(request, "take_test.html", context)
