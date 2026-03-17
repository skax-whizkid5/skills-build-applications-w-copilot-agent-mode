
## Step1 : GitHub Copilot agent mode 시작하기
**“GitHub Copilot agent mode로 애플리케이션 빌드하기”** 실습에 오신 것을 환영합니다! :robot:  
이 실습에서는 GitHub Copilot agent mode를 사용해 **피트니스 목표와 진행 상황을 추적하는 애플리케이션**을 구축합니다. 🏋️‍♂️🏃‍♀️💪

### GitHub Copilot agent mode란?
Copilot agent mode는 앱을 처음부터 생성하고, 여러 파일에 걸친 리팩터링을 수행하며, 테스트를 작성·실행하고, 레거시 코드를 최신 프레임워크로 마이그레이션할 수 있습니다. 문서를 자동으로 생성하고, 새로운 라이브러리를 통합하며, 복잡한 코드베이스에 대한 질문에 답해 줄 수도 있습니다.  
Copilot agent mode는 **워크스페이스를 이해하는 AI 협업자**로서 개발 생산성을 크게 높여 주며, 개발 흐름을 조율하되 **사용자가 항상 제어권을 유지**하도록 돕습니다.

Copilot agent mode는 목표를 달성하기 위해 보다 **자율적이고 동적인 방식**으로 동작합니다. 요청을 처리할 때 필요에 따라 다음 단계를 여러 번 반복합니다.

- 관련 컨텍스트와 수정할 파일을 자율적으로 판단합니다.
- 작업을 완료하기 위해 코드 변경과 터미널 명령을 함께 제안합니다.  
  (예: 코드 컴파일, 패키지 설치, 테스트 실행 등)
- 코드 수정 결과와 터미널 출력의 정확성을 모니터링하고, 문제가 있으면 반복적으로 수정합니다.

> [!NOTE]
> GitHub Copilot agent mode에 대해 더 알아보려면  
> [Use agent mode documentation](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)을 참고하세요.

### :keyboard: 활동: GitHub Copilot agent mode 개발 환경 살펴보기
1. 아래 버튼을 **마우스 오른쪽 클릭**하여 새 탭에서 **Create Codespace** 페이지를 엽니다.  
   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)
   - 모든 GitHub 계정에 포함된 Codespaces 는 **남은 시간**이 있다면 **Free Tier**를 사용해도 괜찮습니다.
   - 기본 Codespace 설정을 그대로 사용해도 됩니다.
1. **Repository** 필드가 원본이 아닌 **본인의 실습용 복사본**인지 확인한 다음, 초록색 **Create Codespace** 버튼을 클릭합니다.
   - ✅ 내 복사본: `/{{full_repo_name}}`
   - ❌ 원본: `/0317-HOL1-skills-build-applications-w-copilot-agent-mode`
   - ❌ 원본: `/skills/build-applications-w-copilot-agent-mode`
1. Visual Studio Code가 로드될 때까지 잠시 기다립니다.
1. 계속 진행하기 전에 프로젝트 폴더 구조를 잠깐 살펴봅시다.
   - 왼쪽 내비게이션 바에서는 파일 탐색기, 디버거, 검색을 사용할 수 있습니다.
   - 하단 패널(Ctrl+J)에서는 디버거 출력 확인, 터미널 명령 실행, 웹 서비스 포트 설정을 할 수 있습니다.
   - `docs` 폴더에는 **Copilot agent mode가 앱을 생성하는 데 참고할 또 다른 샘플 애플리케이션 저장소**가 들어 있습니다. 이에 대해서는 다음 단계에서 자세히 다룹니다!
1. VS Code 상단에서 **Copilot 아이콘**을 찾아 클릭하여 Copilot Chat 패널을 엽니다.  
   <img width="518" height="165" alt="image" src="https://github.com/user-attachments/assets/9313c29b-129c-4834-b797-f859aca41fa6" />
1. GitHub Copilot을 처음 사용하는 경우, 사용 약관에 동의해야 계속 진행할 수 있습니다.
   - **Accept** 버튼을 클릭해 계속하세요.

### :keyboard: 활동: Copilot agent mode로 브랜치 생성 및 게시하기 🙋
아주 잘했습니다! 이제 커스터마이징을 시작할 수 있도록 **브랜치 생성**을 Copilot에게 도와달라고 요청해 봅시다.

> [!NOTE]
> - Copilot agent mode는 대화형이므로 질문을 할 수도 있고, Copilot이 질문을 할 수도 있습니다.
> - Copilot agent mode가 응답할 때까지 잠시 기다린 뒤, 제시된 명령을 실행하려면 **Continue** 버튼을 누르세요.

1. 아직 VS Code에 있지 않다면 VS Code로 돌아옵니다.
1. GitHub Copilot Chat 창이 열려 있지 않다면 엽니다.
1. 프롬프트 입력 영역에서 드롭다운하여 **Agent** 모드와 **GPT-5.3-Codex** 모델을 선택하고, 아래 프롬프트를 **GitHub Copilot Chat**에 복사해 붙여넣습니다.  
   <img width="359" height="623" alt="image" src="https://github.com/user-attachments/assets/eab9b854-845e-49e5-843a-7223319ccfd0" />
1. Copilot agent mode에게 **`build-octofit-app`**이라는 새 Git 브랜치를 생성하고 게시하도록 요청합니다.
   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
   >
   > ```prompt
   > build-octofit-app 이라는 이름의 새 Git 브랜치를 생성하고 게시해 주세요.
   > ```
   Copilot agent mode가 응답하고, 명령 실행을 위해 **continue**를 요청할 것입니다.<br/>
   <img src=https://github.com/user-attachments/assets/d1652fc1-78e5-49c6-9303-b455815eea8f width=40% height=40% />
1. 명령이 마음에 들면 `Continue` 버튼을 눌러 Copilot agent mode가 대신 실행하도록 합니다. 복사·붙여넣기는 필요 없습니다!
1. 잠시 후 VS Code 하단 상태 표시줄의 왼쪽에서 활성 브랜치를 확인합니다. **`build-octofit-app`**으로 표시되면 이 단계는 완료입니다!
   <img width="516" height="127" alt="image" src="https://github.com/user-attachments/assets/915d7b60-057d-4a1a-bba8-8a558417b862" />
1. 브랜치가 GitHub에 푸시되면, Mona가 이미 작업을 확인하고 있을 것입니다. 잠시 기다리며 댓글을 확인하세요. 진행 상황과 다음 레슨에 대한 안내가 도착할 것입니다.

<details>
<summary>문제가 있나요? 🤷</summary><br/>
피드백이 오지 않는다면 다음을 확인해 보세요.
- 브랜치 이름이 정확히 `build-octofit-app`인지 확인하세요. (접두사/접미사 없음)
- 해당 브랜치가 실제로 **본인 저장소에 게시**되었는지 확인하세요.
</details>
