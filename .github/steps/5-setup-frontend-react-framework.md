
## 5단계: 프론트엔드 React 프레임워크 설정, 컴포넌트 업데이트, OctoFit Tracker 앱 실행

> [!NOTE]
> **백그라운드 설명:** 이 실습에서는 GitHub Copilot의 응답을 안내하는 **커스텀 지침 파일**을 사용합니다.  
> `.github/instructions/octofit_tracker_react_frontend.instructions.md` 지침 파일에는 React 프레임워크 설정 명령, Bootstrap 통합, 프론트엔드 구조 가이드라인이 포함되어 있으며, Copilot은 이 단계를 위한 코드를 생성할 때 해당 내용을 참조합니다.

이 단계에서는 다음 작업을 수행합니다.

- `octofit-tracker` 프론트엔드 React 프레임워크 설정
- 다음 컴포넌트를 React 프레임워크를 사용하도록 업데이트
  - `src/App.js`
  - `src/index.js`
  - `src/components/Activities.js`
  - `src/components/Leaderboard.js`
  - `src/components/Teams.js`
  - `src/components/Users.js`
  - `src/components/Workouts.js`
- React 앱을 실행하고 출력 확인

아래 프롬프트를 **GitHub Copilot Chat**에 복사하여 붙여넣고, 프롬프트 입력 드롭다운에서 **“Ask”** 또는 **“Edit”** 대신 **“Agent”**를 선택하세요.

> [!NOTE]
> - Copilot agent mode는 대화형이므로 질문을 받을 수도 있고, 질문을 할 수도 있습니다.
> - Copilot의 응답을 잠시 기다린 뒤, Copilot agent mode가 제시한 명령을 실행하려면 **continue** 버튼을 누르세요.
> - Copilot agent mode가 생성하거나 수정한 파일은 작업이 완료될 때까지 유지하세요.
> - Agent mode는 코드베이스를 평가하고 명령을 실행하며, 코드베이스의 일부를 추가/리팩터링/삭제할 수 있고, 과정 중 실수가 발생하면 자동으로 복구(self-heal)할 수 있습니다.

**Copilot Chat 패널에서 플러스 `+` 아이콘을 눌러 새 Copilot Chat 세션을 여세요.**

### :keyboard: 활동: octofit-tracker 프론트엔드 React 프레임워크 설치

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> 아래 프롬프트를 **한번에** 실행해 주세요.
> 프로세스 진행을 묻는 경우 **허용** 버튼 또는 'y' 를 입력해 주세요. 
>
> ```prompt
> octofit-tracker frontend React 프레임워크를 설정하고, `--prefix`를 사용해 모든 파일이 `octofit-tracker/frontend` 디렉터리에 생성되도록 합니다.
>
> 1. `octofit-tracker/frontend` 디렉터리가 존재하는지 확인합니다.
> 2. React 앱을 생성합니다.
> 3. react, bootstrap, react-router-dom을 설치합니다.
> 4. `src/index.js` 파일에 bootstrap CSS를 import 합니다.
> 5. `.gitignore` 파일은 변경하지 마세요.
> ```
> <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/771bae24-4bc3-42ba-a4de-7ee0ed22b282" />
> <br>
> <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/ae7bf49d-0bd4-4337-b259-d08efe8ffead" />
> <br>



### :keyboard: 활동: octofit-tracker 프론트엔드 React 컴포넌트 업데이트

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> 변경 내용 점검을 위해서 **프롬프트 단위로** 실행해 주세요.
>
> ```prompt
> Octofit-tracker frontend React 컴포넌트를 업데이트합시다.
>
> - 다음 컴포넌트들을 React 프레임워크를 사용하여 backend REST API를 가리키도록 업데이트합니다.
>   - src/App.js
>   - src/index.js
>   - src/components/Activities.js
>   - src/components/Leaderboard.js
>   - src/components/Teams.js
>   - src/components/Users.js
>   - src/components/Workouts.js
> ```
> <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/fa5adc46-9408-4996-8958-d08c074c5618" />
> <br>
> <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/27561af8-394d-4ed9-84eb-a4008ed82759" />
> <br>

> ```prompt
> - 각 컴포넌트에서 `fetch` URL을 backend codespace url로 변경합니다.
>    - 예: Django REST 프레임워크 백엔드의 경우 `https://$REACT_APP_CODESPACE_NAME-8000.app.github.dev/api/[component]/`
> - 모든 컴포넌트가 REST API 엔드포인트에서 데이터를 가져와 REACT frontend 에 표시하도록 합니다.
> - 올바른 포트와 프로토콜(http 또는 https)을 사용해야 합니다.
> ```
> <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/ac345921-a8e7-4759-9196-3509a45aae00" />
> <br>

> ```prompt 
> - `src/App.js`를 업데이트하여 모든 컴포넌트에 대한 메인 네비게이션을 포함합니다.
> - 네비게이션 메뉴에는 react-router-dom을 사용합니다.
> - React 앱에는 네비게이션 메뉴와 각 컴포넌트가 표시되어야 합니다.
> ```
> <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/f4b8a9a9-04a1-4e2e-8e3d-f60c9c0663d1" />
> <br>

> ```prompt 
> 모든 컴포넌트에 가져온 데이터를 로그에 출력하도록 업데이트하고, 페이지네이션된 결과(.results)와 일반 배열 응답 모두에 호환되도록 수정하세요.
> ```
> <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/cc4970c7-db71-4411-8e01-26ad5321c44e" />
> <br>

> ```prompt  
> 각 컴포넌트에 console.log 문을 추가하여 가져온 데이터와 REST API 엔드포인트를 로그로 출력합니다.
> ```
> <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/3ed82b45-7528-41b7-840c-bbd9a076c327" />
> <br>

### :keyboard: 활동: React 앱 실행 및 출력 확인

이제 실제로 React 애플리케이션을 실행해 봅시다!  
왼쪽 사이드바에서 **`Run and Debug`** 탭을 선택한 다음, **Start Debugging** 아이콘을 클릭하세요.

<img alt="Run React Frontend" src="https://github.com/user-attachments/assets/b76a8e82-8435-4cbd-9540-8143756d1c60"  width=30% height=30%>

포트 3000에 대해 표시되는 실행 중인 React 프론트엔드 URL로 이동합니다. 예시는 다음과 같습니다.

<img alt="react-frontend-port" src="https://github.com/user-attachments/assets/a0c8b213-ee5f-46dd-8675-686a7ba0818f" width=30% height=30%>

웹 브라우저에서 열면 다음과 같은 경고 화면이 나타납니다.

<img alt="django-rest-api" src="https://github.com/user-attachments/assets/cb52d137-e78d-440b-8e9c-c322d7c49b48" width=30% height=30%>

`Continue`를 클릭하면 다음과 같이 표시될 것입니다. <br>

<img alt="react-frontend-app" src="https://github.com/user-attachments/assets/f7f1a076-c259-49f6-8aa5-9ebcd5f0698d" width=50% height=50%>

### :keyboard: 활동: octofit tracker 앱에 포맷, 구조, 스타일 추가하기

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> App.css 스타일을 적용해 보기 좋게 만들어 봅시다.
>
> - App.js와 앱 내 모든 컴포넌트의 javascript 파일들이 다음 사항들을 준수하도록 일관성을 유지해야 합니다.
>   - 모든 JavaScript 컴포넌트의 데이터 표시에는 bootstrap 테이블을 사용합니다.
>   - 버튼에는 bootstrap 버튼을 사용합니다.
>   - 제목에는 bootstrap heading을 사용합니다.
>   - 링크에는 bootstrap 링크를 사용합니다.
>   - 네비게이션 메뉴에는 bootstrap navigation을 사용합니다.
>   - 폼에는 bootstrap form을 사용합니다.
>   - 카드에는 bootstrap card를 사용합니다.
>   - 모달에는 bootstrap modal을 사용합니다.
>   - 모든 컴포넌트 데이터에 대해 일관된 테이블 레이아웃을 적용합니다.
> ```
> <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/aeb53a8d-350c-4f67-9198-63c2562dba4b" />
> <br>
> <img width="1550" height="240" alt="image" src="https://github.com/user-attachments/assets/ece0227a-6dc4-48da-b409-e3fff85f9eb1" />
> <br>

### :keyboard: 선택 활동: octofit tracker 앱을 더 보기 좋게 만들고 색상 추가하기

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> App.css를 수정하여 더 보기 좋게 스타일링해 봅시다.
>
> - App.css 파일을 수정하여 다음을 수행합니다.
>   - 배경에 색상을 추가합니다.
>   - 텍스트에 색상을 추가합니다.
>   - 테이블에 색상을 추가합니다.
>   - 버튼에 색상을 추가합니다.
>   - 제목에 색상을 추가합니다.
>   - 링크에 색상을 추가합니다.
>   - 네비게이션 메뉴에 색상을 추가합니다.
>   - 앱 왼쪽에 정렬된 octofitapp-small 로고를 추가하여 보기 좋게 만듭니다.
>   - 앱에 favicon을 추가하여 보기 좋게 만듭니다.
> ```
> <img width="1558" height="504" alt="image" src="https://github.com/user-attachments/assets/258ce76d-e087-410e-9461-744c1366c61a" />
> <br>


### :keyboard: 선택 활동: 외형을 반복적으로 개선하고 다양한 모델 시도하기

> [!TIP]
> - 애플리케이션 외형을 변경하거나 기능을 추가하고,
>   다양한 모델을 시도하기 위해 자신만의 프롬프트를 만들어 보세요.

1. 이제 모든 애플리케이션 컴포넌트에 대한 React 프론트엔드를 생성했으므로,  
   변경 사항을 `build-octofit-app` 브랜치에 반영합니다.
1. 새 변경 사항이 완료되었으므로, **소스제어**에서 **커밋 및 푸시** 메뉴를 선택하여 `build-octofit-app` 브랜치에 반영하세요.  (소스 제어의 변경 내용 창에서 **커밋 메시지 생성** 을 클릭하면 변경된 내용에 대한 커밋 메시지가 자동 생성 됩니다.)              <br>
   <img width="469" height="329" alt="image" src="https://github.com/user-attachments/assets/940be8c5-5620-40e7-858b-1946ae1c2729" />   <br>
1. Mona가 작업을 확인하고 피드백을 제공하며 다음 레슨을 공유할 때까지 잠시 기다려 계속 진행하세요!

<details>
<summary>문제가 있나요? 🤷</summary><br/>
피드백이 오지 않는다면 다음 사항을 확인해 보세요.
- 다음 파일이 `build-octofit-app` 브랜치에 커밋되었고 GitHub로 푸시/동기화되었는지 확인하세요.
  - `octofit-tracker/frontend/src/components/Activities.js`에  
    `-8000.app.github.dev/api/activities/`가 포함되어 있는지
  - `octofit-tracker/frontend/src/components/Leaderboard.js`에  
    `-8000.app.github.dev/api/leaderboard/`가 포함되어 있는지
  - `octofit-tracker/frontend/src/components/Teams.js`에  
    `-8000.app.github.dev/api/teams/`가 포함되어 있는지
  - `octofit-tracker/frontend/src/components/Users.js`에  
    `-8000.app.github.dev/api/users/`가 포함되어 있는지
  - `octofit-tracker/frontend/src/components/Workouts.js`에  
    `-8000.app.github.dev/api/workouts/`가 포함되어 있는지
- Mona가 오류를 발견했다면, 수정 후 다시 푸시하세요. Mona는 필요할 때마다 여러 번 작업을 확인합니다.
</details>
