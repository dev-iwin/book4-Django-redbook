# 4.2 장고 파이썬 쉘로 데이터 조작하기
# >python manage.py shell
# 입력란이 >>> 로 바뀜

from polls.models import Question, Choice  # 프로젝트 디렉토리에서 장고 파이썬 쉘을 실행해야 하는 듯?
from django.utils import timezone
# from django.conf import timezone
import datetime as dt  # 책에는 없었는데.


# 4.2.1 Create - 데이터 생성/입력 #########################################
# SQL용어의 INSERT 문장을 내부적으로 실행
q = Question(question_text="What's new thang?", pub_date=timezone.now())  #  settings.py 대로 됨
q.save()

# 4.2.2 Read - 데이터 조회 #########################################
# QuerySet은 테이블로부터 꺼내 온 객체들의 콜렉션으로, SQL 용어의 SELECT 문장에 해당
# 필터는 조건에 따라 레코드를 추출하여 QuerySet을 만들어주는 기능으로, SQL 용어의 WHERE 절에 해당
# 메소드 : all(), filter(), exclude(), get()
# get()만 객체 하나를 반환, 그 외 메소드는 QuerySet 객체를 반환(체인식 호출 가능)

Question.objects.all()
# Question테이블.레코드들.모두 를 QuerySet 콜렉션으로 반환
'''
<QuerySet [<Question: What is your hobby?>,
<Question: Who do you like best?>,
<Question: Where do you live?>,
<Question: What's new?>]>
이런 객체가 반환됨
'''
'''
s를 빼먹고 object 라고만 치니까 다음과 같은 오류 발생.
File "<console>", line 1, in <module>
AttributeError: type object 'Question' has no attribute 'object'
'''


Question.objects.filter(
    question_text__startswith='What'
).exclude(
    pub_date__gte=dt.date.today()
).filter(
    pub_date__gte=timezone.make_aware(dt.datetime(2018, 5, 5))
)

'''
C:\Users\USER\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\models\fields\__init__.py:1309: RuntimeWarning: DateTimeFi
eld Question.pub_date received a naive datetime (2021-02-13 00:00:00) while time zone support is active.
  warnings.warn("DateTimeField %s.%s received a naive datetime "
<QuerySet [<Question: What is your hobby?>]>
'''
# 데이트 타임 객체를 만들어서 대입해준다.
# 타임존이 없는 것이 나이브 데이트타임, 있는 건 aware
# date to datetime
# (오빠) https://www.tutorialspoint.com/How-to-convert-date-to-datetime-in-Python
# (나) https://stackoverflow.com/questions/1937622/convert-date-to-datetime-in-python
# https://docs.python.org/ko/3/library/datetime.html
# https://docs.python.org/ko/3/library/datetime.html#datetime-objects
# https://8percent.github.io/2017-05-31/django-timezone-problem/
# https://brownbears.tistory.com/42
# https://wayhome25.github.io/django/2017/03/20/django-ep5-model/
# https://8percent.github.io/2017-05-31/django-timezone-problem/
# https://docs.djangoproject.com/ko/3.1/topics/i18n/timezones/
# https://spoqa.github.io/2019/02/15/python-timezone.html
# http://abh0518.net/tok/?p=635

# 4.2.3 Update - 데이터 수정 #########################################
# SQL 용어로 UPDATE 절에 해당
## 필드 속성 값 수정 후 save() 메소드
q.question_text = 'What is a new show?'  # 메모리 상에서만 변경됨
q.save()  # 변경사항을 데이터베이스에도 저장
## 여러 객체를 한꺼번에 수정하는 update() 메소드
Question.objects.filter(pub_date__year=2018).update(question_text='Everything is the same')

# 4.3.4 Delete - 데이터 삭제 #########################################
# delete() 메서드는 SQL 용어로 DELETE 절에 해당
Question.objects.filter(pub_date__year=2021).delete()
# 출력 결과 (7, {'polls.Choice': 3, 'polls.Question': 4})  # 없으면 (0, {})
Question.objects.all().delete()  # 모두 지움
# .objects.delete() << 이렇게는 안 됨