---
모드: 'agent'
모델: GPT-5.3-Codex
설명: 'Octofit Tracker Django 앱을 위한 octofit_db 데이터베이스를 설정, 구성 및 테스트 데이터를 적재합니다'
---

# 환경 설정
- 기존 Python 가상 환경 `octofit-tracker/backend/venv` 을 사용합니다.
- 새로운 Python 가상 환경을 생성하지 마세요.
- 다음 명령으로 활성화 합니다 : `source octofit-tracker/backend/venv/bin/activate`
- `mongodb-org-shell` 은 이미 설치되어 있으므로, MongoDB 와 상호작용 할 때 `mongosh` 를 사용합니다.
- Django 프로젝트는 `octofit-tracker/backend/octofit_tracker` 에 위치합니다.

# 데이터베이스 초기화 및 데이터 적재
1. MongoDB 서비스가 실행 중인지 확인합니다.
2. `settings.py`에서 Djongo를 사용해 `octofit_db` 데이터베이스에 연결하도록 Django를 구성합니다. 인증이나 비밀번호는 필요하지 않습니다.
3. `INSTALLED_APPS`에 `octofit_tracker`, `rest_framework`, `djongo`가 포함되어 있는지 확인합니다.
4. `settings.py`에서 CORS를 활성화하여 모든 origin, method, header를 허용합니다. 모든 호스트 `*`를 허용합니다.
5. CORS 미들웨어 구성 요소를 설치하고 설정합니다.
6. Python 가상 환경에서 `makemigrations`와 `migrate`를 실행합니다.
7. `octofit_db` 데이터베이스를 초기화하고 users, teams, activities, leaderboard, workouts 에 대한 컬렉션을 생성합니다
8. user 컬렉션의 `email` 필드에 대해 고유 인덱스를 보장합니다. (예: `db.users.createIndex({ "email": 1 }, { unique: true })`).
9. `octofit-tracker/backend/octofit_tracker/management/commands/populate_db.py` 에 있는 Django 관리 명령을 사용해 모든 컬렉션에 대한 테스트 데이터를 적재합니다. <br>
   a. 도움말 메시지: 'octofit_db 데이터베이스에 테스트 데이터를 입력합니다.'  
   b. 데이터 삭제 및 삽입에는 Django ORM 을 사용합니다.  
   c. 샘플 데이터는 슈퍼히어로로 구성하고, 팀은 marvel 팀과 dc 팀을 사용합니다.
10. `mongosh` 를 사용하여 데이터베이스와 컬렉션이 성공적으로 생성되고 데이터가 적재되었는지 확인합니다.
11. `octofit_db` 데이터베이스의 컬렉션 목록을 나열하고 각 컬렉션의 샘플 문서를 표시합니다.

# 검증
- 데이터 적재 후 `mongosh` 를 사용해 `octofit_db` 데이터베이스에 올바른 컬렉션과 테스트 데이터가 포함되어 있는지 확인합니다.
- 모든 컬렉션에 대해 Django REST API 엔드포인트가 정상적으로 제공되는지 확인합니다.
