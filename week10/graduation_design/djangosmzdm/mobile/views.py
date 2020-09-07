from django.shortcuts import render
from django.db.models import Avg
from .models import Mobile

def mobile_short(request):
    ###  从models取数据传给template  ###
    shorts = Mobile.objects.all()
    search_key = request.GET.get('search_input')
    if search_key:
        condtions = {"comment__contains": search_key}
        shorts = shorts.filter(**condtions)
    # 评论数量
    counter = Mobile.objects.all().count()

    # 情感倾向
    sent_avg =f" {Mobile.objects.aggregate(Avg('sentiments'))['sentiments__avg']:0.2f} "

    # 正向数量
    queryset = Mobile.objects.values('sentiments')
    condtions = {'sentiments__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = Mobile.objects.values('sentiments')
    condtions = {'sentiments__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    return render(request, 'result.html', locals())