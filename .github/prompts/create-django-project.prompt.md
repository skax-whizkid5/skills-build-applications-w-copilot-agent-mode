---
모드: 'agent'
모델: GPT-5.3-Codex
설명: 'Create a Django project, start it, and run it'
---

당신의 작업은 이미 모든 사전 요구 사항이 포함되어 있는 `octofit-tracker/backend/venv` 디렉터리의 Python 가상 환경을 사용하여 `octofit-tracker/backend/octofit_tracker` 디렉터리에 Django 프로젝트를 생성하는 것입니다.


Django 프로젝트를 생성하려면 다음 단계를 따르십시오.
1. 루트 디렉터리에 있는지 확인하고 디렉터리를 변경하지 마십시오.
2. source octofit-tracker/backend/venv/bin/activate
3. octofit-tracker/backend 디렉터리에서 django-admin startproject octofit_tracker 실행합니다.
4. python manage.py migrate
5. 레포지토리에 포함된 .vscode/launch.json 설정을 사용하여 Django 앱을 실행하도록 사용자에게 안내합니다.
