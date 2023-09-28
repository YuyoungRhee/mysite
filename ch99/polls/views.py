from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Choice, Question

# Create your views here.

def index(request):
    #Question 테이블 객체에서 pub_date 컬럼의 역순으로 정렬하여 최근 5개 Question 객체를 가져옴
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    #render 함수는 템플릿 파일(index.html)에 context 변수를 적용하여 HTML 파일을 만들고 이를 담아서 HttpResponse 객체를 반환함
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #Question 모델 클래스로부터 pk=question_id 검색조건에 맞는 객체를 조회합니다.
    question = get_object_or_404(Question, pk=question_id) #첫번째 인자: 모델 클래스, 두 번째 인자부터는 검색 조건을 여러 개 사용할 수 있음.
    
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        # 설문 폼을 다시 보여 준다
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #POST 데이터를 정상적으로 처리하였으면,
        # 항상 HttpResponseRedirect를 반환하여 리다이렉션 처리함
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

