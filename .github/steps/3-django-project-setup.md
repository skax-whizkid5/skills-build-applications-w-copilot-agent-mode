
## 3단계: octofit_db MongoDB 데이터베이스 초기화 및 생성, Django 프로젝트/앱 생성, Django 프로젝트/앱 파일 업데이트, MongoDB 데이터베이스 적재

> [!NOTE]
> **백그라운드 설명:** 이 실습에서는 GitHub Copilot의 응답을 안내하는 **커스텀 지침 파일**을 사용합니다.  
> `.github/instructions/octofit_tracker_setup_project.instructions.md` 및  
> `.github/instructions/octofit_tracker_django_backend.instructions.md` 지침 파일에는 Django 백엔드 가이드라인, MongoDB 설정, 프로젝트 구조가 포함되어 있으며, Copilot은 이 단계를 위한 코드를 생성할 때 해당 내용을 참조합니다.

이 단계에서는 다음 작업을 수행합니다.

- `octofit_db` MongoDB 데이터베이스 구조 설정
- `octofit-tracker/backend/octofit_tracker` 앱 파일 업데이트:
  - `settings`, `models`, `serializers`, `urls`, `views`, `tests`, `admin` 파일
- `octofit_db` 데이터베이스에 테스트 데이터 적재
- `octofit_db` 데이터베이스에 테스트 데이터가 정상적으로 적재되었는지 검증

> [!NOTE]
> 아래 프롬프트를 **GitHub Copilot Chat**에 복사하여 붙여넣고, 프롬프트 입력 드롭다운에서 Ask 또는 Edit 대신 **Agent**를 선택하세요.
> - Copilot agent mode는 대화형이므로 질문을 받을 수도 있고, 질문을 할 수도 있습니다.
> - Copilot의 응답을 잠시 기다린 뒤, 제시된 명령을 실행하려면 **`Continue`** 버튼을 누르세요.
> - Copilot agent mode가 생성하거나 수정한 파일은 작업이 완료될 때까지 유지하세요.
> - Agent mode는 코드베이스를 평가하고 명령을 실행하며, 코드베이스의 일부를 추가/리팩터링/삭제할 수 있고, 과정 중 실수가 발생하면 자동으로 복구(self-heal)할 수 있습니다.

**Copilot Chat 패널에서 플러스 `+` 아이콘을 눌러 새 Copilot Chat 세션을 여세요.**

### :keyboard: 활동: Python Django 프로젝트/앱 설정하기

이 활동에서는 VS Code의 **프롬프트 파일(prompt files)** 기능을 활용합니다.  
IT 부서에서 Django 프로젝트 애플리케이션 생성을 위해 미리 만들어 둔 프롬프트 파일을 사용합니다.  
프롬프트 입력 영역에서 드롭다운하여 **Agent** 모드와 **GPT-5.3-Codex** 모델을 선택하고, 아래 프롬프트를 **GitHub Copilot Chat**에 복사해 붙여넣습니다.

#### 프롬프트 파일이란?
- 프롬프트 파일은 반복적으로 사용되는 개발 작업을 위해 **Markdown 파일에 재사용 가능한 프롬프트를 정의**할 수 있게 해줍니다.
- 프롬프트 파일은 **독립 실행형 프롬프트**로, 채팅에서 바로 실행할 수 있습니다.
- 작업별 컨텍스트와 수행 방법에 대한 가이드라인을 포함할 수 있습니다.
- 커스텀 지침과 함께 사용하면 **복잡한 작업을 일관되게 실행**할 수 있습니다.

자세한 내용은 [VS Code Docs: Prompt Files](https://code.visualstudio.com/docs/copilot/customization/overview#_prompt-files)를 참고하세요.

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> /create-django-project
> ```

> [!NOTE]
> - Copilot의 응답을 잠시 기다린 뒤, Copilot agent mode가 제시하는 각 명령을 실행하려면 **`Continue`** 버튼을 누르세요.
> - Copilot agent mode가 완료될 때까지 생성·수정된 파일을 유지하세요.

> [!IMPORTANT]
> - GitHub Copilot agent mode가 제안하는 방식으로 Python Django 앱을 **시작하지 마십시오**.  
>   아래 이미지를 보게 되면 **cancel**을 누르세요.
>
> <img src="https://github.com/user-attachments/assets/02a875c1-19a4-417b-ab03-aefbbe2186d4" width=50% height=50%>  <br>

<img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/6d54b9ee-adc5-49a8-885e-b8ac80703c82" />


### :keyboard: 활동: octofit_db MongoDB 데이터베이스 초기화, 생성 및 데이터 적재

이번에도 IT 부서에서 만들어 둔 프롬프트 파일을 활용하여 `octofit_db` MongoDB 데이터베이스를 초기화하고 생성합니다.  
아래 프롬프트를 GitHub Copilot Chat에 복사하여 붙여넣고, **“Agent”**를 선택하세요.

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> /init-populate-octofit_db
> ```
<img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/92674da3-c42f-42bb-8b2f-4aa4b3ee730d" />



### :keyboard: 활동: Python Django 프로젝트/앱 파일을 업데이트하는 프롬프트 파일 생성하기

이제 다른 직원들과 공유할 수 있도록, `octofit-tracker` 앱 개발을 위한 **자체 프롬프트 파일**을 생성해 보겠습니다.  
아래 프롬프트를 GitHub Copilot Chat에 복사하여 붙여넣고, **Agent**를 선택하세요.

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> 다음 단계를 **하나씩** 따라가며 명령을 실행해 주세요.
>
> ```prompt
> `.github/prompts` 디렉터리에 `update-octofit-tracker-app.prompt.md`라는 프롬프트 파일을 생성하고, 해당 프롬프트 파일에 `mode: 'agent`와 `model: GPT-5.3-Codex`을 추가합니다.
> ```
> <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/9f0938c5-1bc7-43ea-813a-496bdd6cb9fd" />
> <br>

> ```prompt
> # Django 앱 업데이트
>
> - 모든 Django 프로젝트 파일은 `octofit-tracker/backend/octofit_tracker` 디렉터리에 있습니다.
> - MongoDB 연결 및 CORS를 위해 `settings.py`를 업데이트합니다.
> ```
> <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/80f7bdbd-14a0-4964-aa87-271ecc3b6c25" />
> <br>

> ```prompt
> users, teams, activities, leaderboard, workouts 컬렉션을 지원하도록 `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py`, `admin.py`를 업데이트합니다.
> ```
> 작업 중에 사용자 확인을 위한 프롬프트를 요구하면 해당 내용을 판단해서 대응합니다.
> <img width="429" height="539" alt="image" src="https://github.com/user-attachments/assets/68fe37f2-1910-4b21-ada5-582973d0c084" />
> <br>
> <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/62da5f7d-6eef-4b64-b3ca-ea33fca4bd0d" />
> <br>

> ```prompt
> `/`가 API를 가리키고, `urls.py`에 `api_root`가 있는지 합니다.
> ```
> <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/954ad997-6b1e-45cb-a4ce-8bbc00889bab" />
> <br>


> [!TIP]
> 프롬프트 파일을 사용해 **반복 가능한 작업과 워크플로우**를 정의하세요.
>
> 프롬프트 작성 시에는 **무엇(WHAT)을 해야 하는지**에 집중하고,  
> **어떻게(HOW) 수행할지는 지침 파일을 참조**하도록 하면 좋습니다.

자세한 내용은 [VS Code Docs: Prompt Files](https://code.visualstudio.com/docs/copilot/customization/overview#_prompt-files)를 참고하세요.

### :keyboard: 활동: 프롬프트 파일을 사용해 Python Django 프로젝트/앱 파일 업데이트하기

아래 프롬프트를 GitHub Copilot Chat에 복사하여 붙여넣고, **“Agent”**를 선택하세요.

> https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff
>
> ```prompt
> /update-octofit-tracker-app
> ```
> <img width="587" height="538" alt="image" src="https://github.com/user-attachments/assets/fe78abc9-b2af-456b-89a7-8b6219f39245" />


> [!IMPORTANT]
> - GitHub Copilot agent mode가 제안하는 방식으로 Python Django 앱을 **시작하지 마십시오**.  
>   아래 이미지를 보게 되면 **cancel**을 누르세요.
>
> <img src="https://github.com/user-attachments/assets/02a875c1-19a4-417b-ab03-aefbbe2186d4" width=50% height=50%>

1. 이제 데이터베이스 구조를 생성하고, Django 프로젝트 파일을 업데이트하고, 데이터베이스를 채웠으니 변경 사항을 `build-octofit-app` 브랜치에 반영합니다.
1. 새 변경 사항이 완료되었으므로, **소스제어**에서 **커밋 및 푸시** 메뉴를 선택하여 `build-octofit-app` 브랜치에 반영하세요.  (소스 제어의 변경 내용 창에서 **커밋 메시지 생성** 을 클릭하면 변경된 내용에 대한 커밋 메시지가 자동 생성 됩니다.)              <br>
   <img width="469" height="329" alt="image" src="https://github.com/user-attachments/assets/940be8c5-5620-40e7-858b-1946ae1c2729" />   <br>
1. Mona가 작업을 확인하고 피드백을 제공하며 다음 레슨을 공유할 때까지 잠시 기다려 계속 진행하세요!

<details>
<summary>문제가 있나요? 🤷</summary><br/>
피드백이 오지 않는다면 다음 사항을 확인해 보세요.
- 다음 파일이 `build-octofit-app` 브랜치에 커밋되었고 GitHub로 푸시/동기화되었는지 확인하세요.
  - `octofit-tracker/backend/octofit_tracker/settings.py`
  - `octofit-tracker/backend/octofit_tracker/management/commands/populate_db.py`
- Mona가 오류를 발견했다면, 수정 후 다시 푸시하세요. Mona는 필요할 때마다 여러 번 작업을 확인합니다.
</details>
