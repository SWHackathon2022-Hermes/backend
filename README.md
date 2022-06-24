# C8_Hermes / Hermes
<br><img width=1280 src="https://user-images.githubusercontent.com/76610340/175432388-99bbf4b4-3586-4faa-b0f0-07d0dd2f1c88.png">
------------
## 🧑🏻‍💻 Hermes Team

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/seunggyun-jeong"><img src="https://user-images.githubusercontent.com/76610340/175435864-1f73aef9-ec25-4e9b-bf0e-61d3a8a26d3e.png" width="200px;" alt=""/><br />정승균<br />(iOS Developer)</td>
    <td align="center"><a href="https://github.com/jumining"><img src="https://user-images.githubusercontent.com/76610340/175436187-bc4d8810-87ac-4638-b13d-ecdde80ad404.png" width="200px;" alt=""/><br />임주민<br />(iOS Developer)</td>
  <td align="center"><a href="https://github.com/NayounK1m"><img src="https://user-images.githubusercontent.com/76610340/175436205-453aeefb-2fa5-4e01-825a-b5201cff2f71.png" width="200px;" alt=""/><br />김나연<br />(BackEnd Developer)</td>
          <td align="center"><a href="https://github.com/yujin37"><img src="https://user-images.githubusercontent.com/76610340/175436235-f5331a3f-88d4-4905-bbdc-4b445ec483ea.png" width="200px;" alt=""/><br />최유진<br />(AI Developer)</td>
             <td align="center"><img src="https://user-images.githubusercontent.com/76610340/175435986-1ea866a3-7ac7-474a-81ed-ff12d78d8759.png" width="200px;" alt=""/><br />숭실대학교<br />유나경<br />(UX/UI Designer)</td>
        </tr>
</table>

<br>

<br>

## 🌱 프로젝트 배경/목표
1) 전동휠체어 배터리가 없어져서 멈추면 혼자 있을때 아예 움직일 수가 없기 때문에 119나 경찰을 부르는 경우가 있어, 미리 가까운 급속충전기 위치를 안내해주는 것이 목표입니다. 
2) 지하철을 이용하러 갈 때, 휠체어로 이동할 수 있는 길이 한정적이여서 지하철 내에 있는 휠체어 리프트의 위치를 안내해서 이용에 도움을 주는 것이 목표입니다.
3) 지하철 내에 휠체어 사용자들이 이용할 수 있는 화장실의 위치를 안내해 이용에 도움을 주는 것이 목표입니다.
4) 휠체어를 이용하다보면 고르지 않은 길과 타일에 바퀴가 잘 빠져서 혼자서 빠져나가기 힘들거나, 휠체어가 걸려 뒤로 넘어가서 위험한 일이 생기고는 합니다. 보도는 모든 사람이 이용하는 공공재로서 누구나 차별 받지 않고 이용할 수 있어야 한다는 점을 감안할 때, 해당 부분에서 도로의 타일이 튀어나와있거나 바퀴가 빠질 정도의 홈이 있는 등의 유형(type)을 선택 및 자세한 내용 작성과 사진 촬영 그리고 어디인지 위치 등록을 해서 불편을 해소해 주는 것이 목표입니다.

<br>
 
### 동작 방식

  ##### [ train.py ]
------------
   * intents.json 내의 데이터 기반으로 학습
   * 단어 토큰화
   * 모델 생성
   * 모델 컴파일
   * 모델 저장
  ##### [ app.py ]
------------
   * 채팅 입력 시 호출
   * 사용자 쿼리를 기반으로 해당 응답 반환
   * 사용자에게 제공할 응답 예측
   * POST, form-data로 클라이언트와 송수신
  ##### [ intents.json ]
------------
   * 서울 기준 지역별 휠체어 대여 관련 정보
   * 서울 장애인 콜택시 예약 안내
   * 도로파손 신고 전화번호
   * 저상버스 예약 안내
   * 그 외 기본 인사, 오류, 챗봇 소개 등
  ##### [ restapi.py ]
------------
   * mysql DB 연결
   * Rest-API Json 형식 POST
   * 클라이언트로부터 민원 Data(유형, 위치, 상세위치, 설명) 저장
### 개발/배포 환경

  ##### Python 3.10, 라이브러리
------------
  * TensorFlow
  * Flask
  * nltk
### 활용/참고 정보
------------
+ AI Chat bot
https://github.com/mainadennis/An-AI-Chatbot-in-Python-and-Flask/tree/6cb96505fc1da684277ef77569d5f2f2e622fcc7
+ Python Flask Rest API
https://medium.com/@feedbotstar/python-flask-%EB%A1%9C-%EA%B0%84%EB%8B%A8%ED%95%9C-rest-api-%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0-60a29a9ebd8c
### 테스트 환경
  ##### Set up
------------
```
1. VsCode : Python -m venv .venv
2. cmd : pip install --upgrade tensorflow
3. cmd : pip install -U nltk
4. cmd : pip install -U Flask
5. cmd : pip install flask-ngrok
```
#### 실행 순서
  ##### 챗봇 모델 생성 및 서버
  > * 챗봇 모델 생성 및 학습 : backend\Chatbot\train.py
  > * 챗봇 서버 구동 :backend\Chatbot\app.py
  ##### 등록 민원 저장 서버
  > * backend\Reportview_bot\restapi.py

<br>

### 👉 [Hermes 영상 Youtube 바로가기](https://www.)

<br>

### 👉 [Hermes 문서 Notion 바로가기](https://www.notion.so/Hermes-55dde0987fad40d0a0648eedcf63b14e)
