#
# (mysite) c:\project\mysite>python manage.py shell
# Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from mybo.models import Question, Answer
# >>> from django.utils import timezone
# >>> q = Question(subject='mybo가 무엇인가요?', content='mybo에 대해서 알고 싶습니다.', create_date=timezone.now())
# >>> q.save()
# >>> q.id
# 3
# >>> Question.objects.all()
# <QuerySet [<Question: Question object (1)>, <Question: Question object (2)>, <Question: Question object (3)>]>
# >>> Question.objects.all()
# <QuerySet [<Question: Question object (1)>, <Question: Question object (2)>, <Question: Question object (3)>]>
# >>> quit()
#
# (mysite) c:\project\mysite>python manage.py shell
# Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from mybo.models import Question, Answer
# >>> Question.objects.all()
# <QuerySet [<Question: mybo가 뭔가요?>, <Question: 장고 모델이 뭔가요?>, <Question: mybo가 무엇인가요?>]>
# >>> Question.objects.filter(id=1)
# <QuerySet [<Question: mybo가 뭔가요?>]>
# >>> Question.objects.get(id=1)
# <Question: mybo가 뭔가요?>
# >>> Question.objects.get(id=9)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "C:\venvs\mysite\lib\site-packages\django\db\models\manager.py", line 85, in manager_method
#     return getattr(self.get_queryset(), name)(*args, **kwargs)
#   File "C:\venvs\mysite\lib\site-packages\django\db\models\query.py", line 429, in get
#     raise self.model.DoesNotExist(
# mybo.models.Question.DoesNotExist: Question matching query does not exist.
# >>> Question.objects.filter(id=9)
# <QuerySet []>
# >>> Question.objects.filter(subject__contains='장고')
# <QuerySet [<Question: 장고 모델이 뭔가요?>]>
# >>> Question.objects.get(id=2)
# <Question: 장고 모델이 뭔가요?>
# >>> q=Question.objects.get(id=2)
# >>> q
# <Question: 장고 모델이 뭔가요?>
# >>> q.subject="Django Model Question"
# >>> q.save()
# >>> q
# <Question: Django Model Question>
# >>> Question.objects.get(id=2)
# <Question: Django Model Question>
# >>> q=Question.objects.get(id=1)
# >>> q.delete()
# (1, {'mybo.Question': 1})
# >>> Question.objects.all()
# <QuerySet [<Question: Django Model Question>, <Question: mybo가 무엇인가요?>]>
# >>> Question.objects.get(id=2)
# <Question: Django Model Question>
# >>> q=Question.objects.get(id=2)
# >>> from django.utils import timezone
# >>> a=Answer(question=q, content="2번 글에 대한 답변입니다.", create_date=timezone.now())
# >>> a.save()
# >>> a.id
# 1
# >>> Answer.objects.get(id=1)
# <Answer: Answer object (1)>
# >>> a=Answer.objects.get(id=1)
# >>> a.question
# <Question: Django Model Question>
# >>> a
# <Answer: Answer object (1)>
# >>> a.content
# '2번 글에 대한 답변입니다.'
# >>> a.create_date
# datetime.datetime(2021, 2, 2, 7, 21, 11, 197640, tzinfo=<UTC>)
# >>> q
# <Question: Django Model Question>
# >>> q.answer_set.all()
# <QuerySet [<Answer: Answer object (1)>]>
# >>> a.question
# <Question: Django Model Question>
# >>> q.answer_set.all()
# <QuerySet [<Answer: Answer object (1)>]>
# >>> quit()
#
# (mysite) c:\project\mysite>python manage.py createsuperuser
# 사용자 이름 (leave blank to use 'i'): admin
# 이메일 주소: admin@mysite.com
# Password:
# Password (again):
# 비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
# 비밀번호가 너무 일상적인 단어입니다.
# 비밀번호가 전부 숫자로 되어 있습니다.
# Bypass password validation and create user anyway? [y/N]: y
# Superuser created successfully.
#
# (mysite) c:\project\mysite>python manage.py runserver
# Watching for file changes with StatReloader
# Performing system checks...
#
# System check identified no issues (0 silenced).
# February 02, 2021 - 16:38:46
# Django version 3.1.3, using settings 'config.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.
# [02/Feb/2021 16:39:44] "GET /admin HTTP/1.1" 301 0
# [02/Feb/2021 16:39:44] "GET /admin/ HTTP/1.1" 302 0
# [02/Feb/2021 16:39:47] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 2214
# [02/Feb/2021 16:39:47] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 200 2138
# [02/Feb/2021 16:39:47] "GET /static/admin/css/base.css HTTP/1.1" 200 16307
# [02/Feb/2021 16:39:47] "GET /static/admin/css/responsive.css HTTP/1.1" 200 18339
# [02/Feb/2021 16:39:47] "GET /static/admin/css/login.css HTTP/1.1" 200 1185
# [02/Feb/2021 16:39:47] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 200 1360
# [02/Feb/2021 16:39:47] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
# [02/Feb/2021 16:39:48] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
# [02/Feb/2021 16:39:48] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
# Not Found: /favicon.ico
# [02/Feb/2021 16:39:48] "GET /favicon.ico HTTP/1.1" 404 2077
# [02/Feb/2021 16:40:52] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
# [02/Feb/2021 16:40:52] "GET /admin/ HTTP/1.1" 200 3329
# [02/Feb/2021 16:40:52] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 380
# [02/Feb/2021 16:40:52] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
# [02/Feb/2021 16:40:52] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
# [02/Feb/2021 16:40:52] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
# Not Found: /
# [02/Feb/2021 16:41:55] "GET / HTTP/1.1" 404 2026
# [02/Feb/2021 16:41:59] "GET /admin/ HTTP/1.1" 200 3329
# [02/Feb/2021 16:42:07] "GET /admin/auth/user/add/ HTTP/1.1" 200 7047
# [02/Feb/2021 16:42:07] "GET /static/admin/css/forms.css HTTP/1.1" 200 8423
# [02/Feb/2021 16:42:07] "GET /static/admin/js/jquery.init.js HTTP/1.1" 200 347
# [02/Feb/2021 16:42:07] "GET /static/admin/js/core.js HTTP/1.1" 200 5418
# [02/Feb/2021 16:42:07] "GET /admin/jsi18n/ HTTP/1.1" 200 8314
# [02/Feb/2021 16:42:07] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 200 6078
# [02/Feb/2021 16:42:07] "GET /static/admin/js/actions.js HTTP/1.1" 200 6783
# [02/Feb/2021 16:42:07] "GET /static/admin/css/widgets.css HTTP/1.1" 200 10592
# [02/Feb/2021 16:42:07] "GET /static/admin/js/prepopulate.js HTTP/1.1" 200 1531
# [02/Feb/2021 16:42:07] "GET /static/admin/js/prepopulate_init.js HTTP/1.1" 200 492
# [02/Feb/2021 16:42:07] "GET /static/admin/js/urlify.js HTTP/1.1" 200 8632
# [02/Feb/2021 16:42:07] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 200 287630
# [02/Feb/2021 16:42:07] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 200 232381
# [02/Feb/2021 16:42:07] "GET /static/admin/js/change_form.js HTTP/1.1" 200 606
# [02/Feb/2021 16:42:13] "GET /admin/ HTTP/1.1" 200 3329
# [02/Feb/2021 16:42:15] "GET /admin/auth/group/ HTTP/1.1" 200 4736
# [02/Feb/2021 16:42:15] "GET /admin/jsi18n/ HTTP/1.1" 200 8314
# [02/Feb/2021 16:42:15] "GET /static/admin/css/changelists.css HTTP/1.1" 200 6281
# [02/Feb/2021 16:42:15] "GET /static/admin/img/search.svg HTTP/1.1" 200 458
# [02/Feb/2021 16:42:15] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 200 331
# [02/Feb/2021 16:42:17] "GET /admin/ HTTP/1.1" 200 3329
# C:\project\mysite\mybo\admin.py changed, reloading.
# Watching for file changes with StatReloader
# Performing system checks...
#
# System check identified no issues (0 silenced).
# February 02, 2021 - 16:45:53
# Django version 3.1.3, using settings 'config.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.
# [02/Feb/2021 16:45:56] "GET /admin/ HTTP/1.1" 200 3979
# [02/Feb/2021 16:47:04] "GET /admin/mybo/question/ HTTP/1.1" 200 6402
# [02/Feb/2021 16:47:04] "GET /admin/jsi18n/ HTTP/1.1" 200 8314
# [02/Feb/2021 16:47:21] "GET /admin/mybo/question/3/change/ HTTP/1.1" 200 7264
# [02/Feb/2021 16:47:21] "GET /admin/jsi18n/ HTTP/1.1" 200 8314
# [02/Feb/2021 16:47:21] "GET /static/admin/js/calendar.js HTTP/1.1" 200 7788
# [02/Feb/2021 16:47:21] "GET /static/admin/js/admin/DateTimeShortcuts.js HTTP/1.1" 200 19750
# [02/Feb/2021 16:47:21] "GET /static/admin/img/icon-clock.svg HTTP/1.1" 200 677
# [02/Feb/2021 16:47:21] "GET /static/admin/img/icon-calendar.svg HTTP/1.1" 200 1086
# [02/Feb/2021 16:47:31] "GET /admin/mybo/question/ HTTP/1.1" 200 6402
# [02/Feb/2021 16:47:33] "GET /admin/mybo/question/2/change/ HTTP/1.1" 200 7265
# [02/Feb/2021 16:47:33] "GET /admin/jsi18n/ HTTP/1.1" 200 8314
# [02/Feb/2021 16:47:38] "GET /admin/mybo/question/ HTTP/1.1" 200 6402
# [02/Feb/2021 16:47:42] "GET /admin/ HTTP/1.1" 200 3979
# [02/Feb/2021 16:47:46] "GET /admin/login/?next=/admin/ HTTP/1.1" 302 0
# [02/Feb/2021 16:47:46] "GET /admin/ HTTP/1.1" 200 3979
