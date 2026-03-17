
## 4단계: Django REST Framework 설정, 서버 시작, API 테스트

> [!NOTE]
> **백그라운드 설명:** 이 실습에서는 GitHub Copilot의 응답을 안내하는 **커스텀 지침 파일**을 사용합니다.  
> `.github/instructions/octofit_tracker_django_backend.instructions.md` 지침 파일에는 Django REST Framework 설정, URL 패턴, API 엔드포인트 가이드라인이 포함되어 있으며, Copilot은 이 단계를 위한 코드를 생성할 때 해당 내용을 참조합니다.

이 단계에서는 다음 작업을 수행합니다.

- Django REST Framework 설정
- 서버 시작
- `curl`을 사용한 API 테스트

아래 프롬프트를 **GitHub Copilot Chat**에 복사하여 붙여넣고, 프롬프트 입력 드롭다운에서 **“Ask”** 또는 **“Edit”** 대신 **“Agent”**를 선택하세요.

> [!TIP]
> - Copilot agent mode는 대화형이므로 질문을 받을 수도 있고, 질문을 할 수도 있습니다.
> - Copilot의 응답을 잠시 기다린 뒤, Copilot agent mode가 제시한 명령을 실행하려면 **continue** 버튼을 누르세요.
> - Copilot agent mode가 생성하거나 수정한 파일은 작업이 완료될 때까지 유지하세요.
> - Agent mode는 코드베이스를 평가하고 명령을 실행하며, 코드베이스의 일부를 추가/리팩터링/삭제할 수 있고, 과정 중 실수가 발생하면 자동으로 복구(self-heal)할 수 있습니다.

**Copilot Chat 패널에서 플러스 `+` 아이콘을 눌러 새 Copilot Chat 세션을 여세요.**

### :keyboard: 활동: Django REST Framework 설정 및 REST API 엔드포인트 테스트

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> 아래 프롬프트를 **한번에** 실행해 주세요.
>
> ```prompt
> codespace URL을 설정하고, VS Code launch.json을 통해 서버를 시작한 다음 API를 테스트해 보겠습다.
>
> - 모든 Django 프로젝트 파일은 `octofit-tracker/backend/octofit_tracker` 디렉터리에 있습니다.
> - `settings.py`와 `urls.py`의 URL만 업데이트하세요.
> - REST API 엔드포인트 형식: https://$CODESPACE_NAME-8000.app.github.dev/api/[component]/
> - 전체 URL 예시: https://$CODESPACE_NAME-8000.app.github.dev/api/activities/
> - `$CODESPACE_NAME` 값은 하드코딩하지 말고 변수를 사용하세요.
> - `views.py`는 업데이트하지 마세요.
>
> 1. `urls.py` 파일을 수정하여 REST API URL 엔드포인트의 반환 값을 환경 변수 `$CODESPACE_NAME` (예: `https://$CODESPACE_NAME-8000.app.github.dev`)으로 대체하고 Django의 HTTPS 인증서 문제를 방지하세요.
> 2. `settings.py` 파일의 `ALLOWED_HOSTS` 값을 업데이트하여 Django 백엔드가 codespace URL 과 localhost(즉, `$CODESPACE_NAME` 값) 모두에서 정상적으로 동작하도록 합니다.
> 3. `curl` 명령을 사용해 API 엔드포인트를 테스트합니다.
> ```

> [!IMPORTANT]
> GitHub Copilot agent mode가 제안하는 방식으로 Python Django 앱을 **시작하지 마십시오**.  
> 이 화면이 보이면 **cancel**을 누르고 다음 활동을 진행하세요.

### :keyboard: 활동: Python Django 앱 시작 및 출력 확인

이제 실제로 Django 애플리케이션을 실행해 봅시다!  
왼쪽 사이드바에서 **`Run and Debug`** 탭을 선택한 다음, **Start Debugging** 아이콘을 클릭하세요.

<img alt="Run Django" src="https://github.com/user-attachments/assets/a6c32898-bbeb-41ed-a8c5-488c8a42d507" width=30% height=30%>

포트 8000에 대해 표시되는 실행 중인 Django REST API URL로 이동합니다. 예시는 다음과 같습니다.

<img alt="django-rest-api-port" src="https://github.com/user-attachments/assets/627f3cbe-96ae-4a30-b38b-acd3cecf96ee" width=30% height=30%>

웹 브라우저에서 열면 다음과 같은 경고 화면이 나타납니다.

<img alt="django-rest-api" src="https://github.com/user-attachments/assets/cb52d137-e78d-440b-8e9c-c322d7c49b48" width=30% height=30%>

`Continue`를 클릭하면, 다음과 같이 **codespace 이름이 포함된 화면**이 표시될 것입니다.

<img alt="django-rest-api" src="https://github.com/user-attachments/assets/45ac98ba-aa7b-4953-81d6-e38bba97ae35" width=50% height=50%>

1. 이제 URL 엔드포인트에 codespace 이름을 포함하도록 Django 프로젝트를 업데이트했으므로,  
   변경 사항을 `build-octofit-app` 브랜치에 반영합니다.
1. 새 변경 사항이 완료되었으므로, **소스제어**에서 **커밋 및 푸시** 메뉴를 선택하여 `build-octofit-app` 브랜치에 반영하세요.  (소스 제어의 변경 내용 창에서 **커밋 메시지 생성** 을 클릭하면 변경된 내용에 대한 커밋 메시지가 자동 생성 됩니다.)              <br>
   <img width="469" height="329" alt="image" src="https://github.com/user-attachments/assets/940be8c5-5620-40e7-858b-1946ae1c2729" />   <br>
1. Mona가 작업을 확인하고 피드백을 제공하며 다음 레슨을 공유할 때까지 잠시 기다려 계속 진행하세요!

<details>
<summary>문제가 있나요? 🤷</summary><br/>
피드백이 오지 않는다면 다음 사항을 확인해 보세요.
- 다음 파일이 `build-octofit-app` 브랜치에 커밋되었고 GitHub로 푸시/동기화되었는지 확인하세요.
  - `octofit-tracker/backend/octofit_tracker/settings.py`
  - `octofit-tracker/backend/octofit_tracker/views.py`
- Mona가 오류를 발견했다면, 수정 후 다시 푸시하세요. Mona는 필요할 때마다 여러 번 작업을 확인합니다.
</details>
