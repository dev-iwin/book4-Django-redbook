from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice

# QuestionAdmin 클래스에 사용되어야 해서, 앞에 적는군.
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    # 부모 클래스를 바꾸고 테이블 형태로 보이게 하여 화면이 길어지는 것을 완화.
    model = Choice
    extra = 2  # 추가 입력할 수 있는 칸의 개수. 그 위에는 기존에 등록해둔 항목들이 보임.

class QuestionAdmin(admin.ModelAdmin):
    # 4.1.3 필드 순서 변경 : [ Home > Polls > Question > 항목 ] 여기에 보이는 필드 순서 변경.
    # fields = ['pub_date', 'question_text']  # 일시 정보가 위, 텍스트가 아래로 위치가 바뀜.
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
       #('Date Information', {'fields': ['pub_date']})
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]  # 왜 ['question_text'], ['pub_date'] 등 처럼 대괄호가 쓰이는 걸까? (질문)
       # 아무튼, 튜플의 첫번째 인자는 헤더의 제목이 되고, 대괄호들은 필드를 의미하고 제목으로 보여지는군.
    inlines = [ChoiceInline]  # Question 테이블의 항목을 누르면, 만들어둔 항목과 추가 생성 가능한 칸이 같이 보임.
    list_display = ('question_text', 'pub_date')  # models.py에서 정의한 변수만 칼럼으로 지정 가능(그 외 오류남).
    list_filter = ['pub_date']  # 모델에서 클래스에 정의한 변수로 설정. 그 필드 타입에 적합한 항목의 필터가 생성됨.
    search_fields = ['question_text']  # 퀘스천 텍스트에 대해 검색 가능.

class ChoiceAdmin(admin.ModelAdmin):
    list_filter = ['votes']  # 될까? 된다. 필터의 검색 조건은, 해당 클래스에 정의된 멤버여야 함.

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)


