from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        #각 필드를 분리해서 보여주기
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
    inlines = [ChoiceInline] #Choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_date') #레코드 리스트 컬럼 지정
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)