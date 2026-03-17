# GitHub Copilot 에이전트 모드로 애플리케이션 만들기

<!-- ![](../../actions/workflows/0-start-course.yml/badge.svg?branch=main) -->
<img src="https://github.com/user-attachments/assets/1b3ea5df-f18d-4ed8-9ae6-f96dc1861818" alt="octofit-tracker" width="300"/>

_1시간 이내에 GitHub Copilot 에이전트 모드로 애플리케이션을 만들어 보세요._

## 환영합니다

사람들은 GitHub Copilot이 더 빠르고 더 적은 오류로 코드를 작성하도록 도와주는 점을 좋아합니다.
그런데 만약 GitHub가 자연어로 작성된 요구사항을 바탕으로 프레젠테이션(표현), 로직, 데이터 레이어를 갖춘 **멀티 티어 애플리케이션**을 만들어 줄 수 있다면 어떨까요?
이 실습에서는 GitHub Copilot 에이전트 모드에 프롬프트를 입력해 **완전한 애플리케이션**을 만들도록 해봅니다.

- **대상**: GitHub Copilot, 기본 GitHub 사용법, 기본 웹 개발에 익숙한 중급 개발자
- **학습 내용**: GitHub Copilot 에이전트 모드와 애플리케이션 개발에 활용하는 방법을 소개합니다.
- **만들 결과물**: 고등학교 체육 교사라는 설정에서, GitHub Copilot 에이전트 모드를 사용해 피트니스 애플리케이션을 만듭니다.
- **사전 준비**: Skills 실습: <a href="https://github.com/skills/getting-started-with-github-copilot">GitHub Copilot 시작하기</a>.
- **소요 시간**: 이 코스는 1시간 이내에 완료할 수 있습니다.

이 실습에서 여러분은 다음을 수행합니다:

1. 멀티 티어 애플리케이션을 만들기 위한 사전 구성된 개발 환경을 시작합니다.
1. GitHub Copilot Chat에서 프롬프트를 입력한 뒤, **Edit** 탭을 선택하고, edit/agent 드롭다운에서 **Agent mode**를 선택합니다.
1. 이 실습에서는 주로 최신 기본 LLM을 사용했습니다.
1. 다른 LLM 모델도 사용해 보며 출력 결과가 어떻게 달라지는지 확인합니다.
1. 각 단계마다 Copilot Chat 패널에서 플러스 `+` 아이콘을 눌러 **새 Copilot Chat 세션**을 엽니다.

### 이 실습을 시작하는 방법

실습을 자신의 계정으로 복사한 다음, 좋아하는 Octocat(Mona)에게 첫 번째 레슨을 준비할 **약 20초**를 주고, 그 다음 **페이지를 새로고침**하세요.

[![](https://img.shields.io/badge/Copy%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/new?template_owner=soondukkim&template_name=0317-HOL1-skills-build-applications-w-copilot-agent-mode&owner=%40me&name=skills-build-applications-w-copilot-agent-mode&description=Exercise:+Build+applications+with+GitHub+Copilot+agent+mode&visibility=public)

<details>
<summary>문제가 있나요? 🤷</summary><br/>

실습을 복사할 때는 다음 설정을 권장합니다:

- 소유자(owner)는 개인 계정 또는 리포지토리를 호스팅할 조직을 선택하세요.

- 프라이빗 리포지토리는 Actions 사용 시간이 차감��므로, 퍼블릭 리포지토리를 만드는 것을 권장합니다.

20초가 지나도 실습이 준비되지 않았다면, 리포지토리의 "Actions" 탭을 확인해 보세요(또는 `https://github.com/<YOUR-USERNAME>/<YOUR-REPO>/actions` 방문).

- 실행 중인 작업(job)이 있는지 확인하세요. 경우에 따라 조금 더 시간이 걸릴 수 있습니다.

- 페이지에서 실패한 작업(job)이 보인다면, 이슈를 등록해 주세요. 좋습니다, 버그를 찾으셨네요! 🐛

</details>

---
이 실습은 GitHub Skill repository 를 소스로 합니다.
https://github.com/skills/build-applications-w-copilot-agent-mode

&copy; 2025 GitHub &bull; [행동 강령](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT 라이선스](https://gh.io/mit)
