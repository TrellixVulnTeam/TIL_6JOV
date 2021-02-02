# 1. mybo 앱 설치
# - (mysite) C:\project\mysite>django-admin startapp mybo
# 2. 웹 서버 구동
# - (mysite) C:\project\mysite>python manage.py runserver
# 3. localhost:8000/mybo 접속
# 1)config->urls.py 파일 참조
# 2)mybo/ 매핑규칙 확인
# 3)views.py -> index 함수 호출
#
# 4. 장고는 모델로 데이터 관리(저장,검색,...)
# -sql문을 전혀 몰라도 데이터 관리가 가능
#
# 5. migrate 명령 : admin, auth, sessions 등의 앱이 필요로 하는 테이블을 생성
# - (mysite) c:\project\mysite>python manage.py migrate
# 테이블?데이터(학생 1명)를 저장하기 위한 데이터 집합의 모음(테이블은 학생이 소속된 반과 같음)
# 전국학교 데이터베이스는 테이블, ... 의 모음
#
# 데이터베이스관리시스템:데이터베이스를 관리하는 프로그램
# -sqlite3, 몽고, mysql, mssql, oracle,...
#
#
# 6. DB 관리도구 설치
# 파이썬 설치 -> 파이참(도구) -> 코딩
# sqlite 설치 ->   DB Browser for SQLite(도구) ->데이터 관리
# - sqlitebrowser.org/dl 에 접속하여 다운로드 및 설치 진행
#
# -sql을 모르는 왕초보도 장고의 ORM(object relational mapping)으로 데이터 작업을 할 수 있음
# (파이썬으로 데이터 작업을 할 수 있는 ORM이 우리를 대신하여 SQL문 생성->실행)
# -쿼리문의 단점 : 쿼리문의 일관성이 없음, 잘못된 쿼리문의 실행으로 인해 시스템이 저하될 수 있음,
# db변경하는 경우, 변경 전에 작성된 쿼리문이 변경 후의 db에서 실행이 잘 안되는 경우가 발생할 수 있음
# ==========> 그래서, 장고의 ORM은 위에 열거된 단점들을 극복
#
# 7. 질문 / 답변 모델(model)
# -머신러닝 모델 : 빅데이터 환경에서 데이터들 사이의 규칙(패턴)을 발견하여 함수(수식)를 생성.
# 새롭게 입력된 값에 대한 예측값이나 분류결과를 도출해내기 위한 함수
# -장고 모델 : 데이터 관리(저장,검색,...)
# ex) 장고 질문/답변 모델 : 질문/답변 데이터 관리 모델
#
# -질문 모델 구성 요소 : 질문의 제목, 질문 내용, 질문 작성일, ...
# -답변 모델 구성 요소 : 질문, 답변 내용, 답변 작성일, ...
#
# 8. 질문 모델 작성
# -모델은 클래스로 정의
# -Question
#
#
#
# 9. 장고는 모델을 이용하여 테이블 생성
#
# 10. 테이블 실제 생성
# - 새롭게 테이블 생성/수정하는 경우에는 먼저 테이블 작업을 위한 파일을 생성한 다음, 테이블 생성해야 함
#
# 1)테이블 작업을 위한 파일을 생성
# (mysite) c:\project\mysite>python manage.py makemigrations
# -> 파이참에서 mybo\migrations에 0001_initial.py가 생성
#
# 2) 테이블 생성(migrate 명령으로 테이블 생성)
# (mysite) C:\projects\mysite>python manage.py migrate
#
# 11. 데이터 생성/저장/조회
# 1) 장고 쉘 실행
# (mysite) c:\project\mysite>python manage.py shell
# >>>from mybo.models import Question, Answer
#
# 2) 질문 생성하여 데이터베이스(질문 테이블)에 저장
# >>>from django.utils import timezone
# >>>q=Question(subject="mybo가 뭔가요?", content="mybo를 만들고 있습니다.", create_date=timezone.now())
# >>>q.save()
# => 질문 객체 생성(질문 1건)  -> save() -> DB에 저장
#
# 3) 질문 데이터 확인
# >>>q.id
# 1
#  >>>q=Question(subject="장고 모델이 뭔가요?", content="id가 자동으로 부여되고 있습니다.", create_date=timezone.now())
# >>>q.save()
# >>> q.id
# 2
#
# 3-1) 전체 질문 데이터 객체 확인
# >>> Question.objects.all()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
