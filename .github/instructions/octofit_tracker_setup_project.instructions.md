---
applyTo: "**"
---

# Octofit-tracker 피트니스 앱 설정 및 구조 가이드라인

## Octofit Tracker 앱의 목표와 단계 설명
다음 기능을 포함하는 Octofit Tracker 앱을 구축하고자 합니다.

* 사용자 인증 및 프로필
* 활동 기록 및 추적
* 팀 생성 및 관리
* 경쟁형 리더보드
* 개인 맞춤형 운동 제안

## Agent mode에서 명령을 실행할 때 디렉터리를 변경하지 말 것
- 디렉터리를 절대 변경하지 않습니다
- 대신 명령을 실행할 때 대상 디렉터리를 명시합니다

## 포트 포워딩
- 8000: public
- 3000: public
- 27017: private

위에 명시된 포트 외에 **다른 포트를 포워딩하거나 public으로 제안하지 마십시오**

## OctoFit Tracker 앱 구조
이 섹션에서는 OctoFit Tracker 앱의 구조를 정의합니다.

```text
octofit-tracker/
├── backend/
│   ├── venv/
|   ├── octofit_tracker/
└── frontend/
```

## OctoFit Tracker Python 가상 환경 생성

- 가상 환경을 생성하려면 다음 명령을 실행합니다:
  
  ```bash
  python3 -m venv octofit-tracker/backend/venv
  ```

## OctoFit Tracker Python 필수 패키지

### octofit-tracker/backend/requirements.txt 파일 생성

- octofit-tracker/backend/requirements.txt 파일에 다음 내용을 추가합니다
- 아래의 Python 패키지는 OctoFit Tracker project 전용으로만 설치합니다

```text
Django==4.1.7
djangorestframework==3.14.0
django-allauth==0.51.0
django-cors-headers==4.5.0
dj-rest-auth==2.2.6
djongo==1.3.6
pymongo==3.12
sqlparse==0.2.4
stack-data==0.6.3
sympy==1.12
tenacity==9.0.0
terminado==0.18.1
threadpoolctl==3.5.0
tinycss2==1.3.0
tornado==6.4.1
traitlets==5.14.3
types-python-dateutil==2.9.0.20240906
typing_extensions==4.9.0
tzdata==2024.2
uri-template==1.3.0
urllib3==2.2.3
wcwidth==0.2.13
webcolors==24.8.0
webencodings==0.5.1
websocket-client==1.8.0
```

## Python 가상 환경 요구사항

다음 Python 필수 패키지를 포함하는 requirements.txt 를 생성합니다.
생성한 requirements.txt 에 정의된 패키지를 설치합니다.

```bash
source octofit-tracker/backend/venv/bin/activate 
pip install -r octofit-tracker/backend/requirements.txt
```

## mongodb-org 서비스 및 데이터 생성

- mongod 실행 여부를 확인할 때는 항상 다음 명령을 사용합니다.
    `ps aux | grep mongod`
- mongodb-org 는 공식 MongoDB 패키지 입니다.
- mongosh 는 공식 클라이언트 구조 입니다.
- 데이터베이스 구조 및 데이터 생성 시 직접 MongoDB 스크립트를 사용하지 말고, 항상 Django's ORM 을 사용해야 합니다.
