
## 6단계: Pull Request에서 GitHub Copilot 사용하기

축하합니다! 이 실습에서의 코딩 작업(그리고 VS Code 사용)이 모두 끝났습니다. 이제 작업을 병합할 시간입니다. :tada:  
마무리로, Pull Request 속도를 높여 줄 **접근 권한이 제한된 Copilot 기능 두 가지**를 알아봅시다!

#### Copilot Pull Request 요약

일반적으로는 메모와 커밋 메시지를 검토한 뒤 Pull Request 설명을 직접 요약해야 합니다.  
커밋 메시지가 일관되지 않거나 코드에 문서화가 잘 되어 있지 않은 경우, 이 작업에는 시간이 꽤 걸릴 수 있습니다.

다행히도 Copilot은 Pull Request에 포함된 **모든 변경 사항을 고려하여 중요한 하이라이트를 자동으로 정리**해 주며, **참고(레퍼런스)**도 함께 제공합니다!

> [!NOTE]
> 이 기능은 **Copilot Free** 요금제에서는 사용할 수 없습니다.  
> [[docs]](https://docs.github.com/en/enterprise-cloud@latest/copilot/using-github-copilot/using-github-copilot-for-pull-requests/creating-a-pull-request-summary-with-github-copilot)

#### Copilot 코드 리뷰

작업 결과를 여러 시각에서 보는 것은 언제나 도움이 됩니다.  
정식 동료 리뷰를 진행하기 전에, Copilot에게 **1차 코드 리뷰**를 요청해 봅시다.

Copilot은 간단한 수정으로 해결할 수 있는 일반적인 실수를 잘 찾아내지만,  
항상 **책임감 있게 사용하는 것**을 잊지 마세요.

### :keyboard: 활동: Copilot으로 PR 요약 및 리뷰하기

1. 웹 브라우저에서 새 탭을 열고 실습을 진행하고 있는 리파지토리로 이동합니다.
1. **새 Pull Request를 생성하라는 알림 배너**가 보일 수 있습니다.  
   해당 배너를 클릭하거나, 상단의 **Pull Requests** 탭을 사용해 새 Pull Request를 생성하세요.
   <img width="1156" height="444" alt="image" src="https://github.com/user-attachments/assets/cdc4cbae-72be-415e-ab14-daaa582341e8" />  <br>
   <br>
   <img width="1188" height="284" alt="image" src="https://github.com/user-attachments/assets/973534a1-c62e-4bb8-9ae7-5ae904988f6b" /> <br>

   다음 설정을 사용합니다.
   - **base:** `main`
   - **compare:** `build-octofit-app`
   - **title:** `회원가입 유효성 검사 및 기타 활동 추가`
>
> ```prompt
> 회원가입 유효성 검사 및 기타 활동 추가
> ```
<br>

     
3. (선택) **Add a description** 영역에서 필요하면 편집 모드로 전환한 뒤,  
   **Copilot actions** 아이콘을 클릭하고 **Summary** 액션을 선택합니다.  
   잠시 후 Copilot이 설명을 자동으로 추가합니다. :memo:  
   Copilot 요약 버튼
   
   <img alt="Copilot summarize button " width="300px" src="https://github.com/user-attachments/assets/3fc5fab4-db03-4ab8-8a16-cdd71ec2ded0">  <br>
   <br>
   <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/a3f45d4f-3374-48d4-8c4f-dd256a9589d4" />  <br>
   
4. (선택) 우측 상단 정보 패널의 **Reviewers** 섹션에서,  
   **Copilot 아이콘** 옆에 있는 **Request** 버튼을 클릭합니다.  
   잠시 기다리면 Copilot이 Pull Request에 리뷰 코멘트를 추가합니다.  
   Copilot 리뷰 버튼
   
   <img alt="Copilot review button" width="300px" src="https://github.com/user-attachments/assets/39b15002-a235-4c25-b09d-6a8097e27b62">

> 🪧 **참고:** Copilot에게 리뷰를 요청했다는 로그 항목이 표시되는 것을 확인하세요.

1. 하단에서 **Create pull request** 버튼을 클릭합니다.
   
1. 하단에서 **Merge pull request** 버튼을 클릭합니다.  <br>
   훌륭합니다! 모든 작업이 완료되었습니다! :tada:
   
1. 잠시 기다리면 Mona가 작업을 확인하고 피드백을 제공하며,  
   이 레슨에 대한 최종 리뷰를 게시합니다!
