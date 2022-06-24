# C8_Hermes / Hermes
------------
### 팀원소개
------------
> + (1) 우송대학교 / 김나연 / 개발자 / 리더
> + (2) 대구가톨릭대학교 / 정승균 / 개발자 / 소통
> + (3) 상명대학교 / 최유진 / 개발자 / 서버관리
> + (4) 숭실대학교 / 유나경 / 디자이너 / 영상제공
> + (5) 인하대학교 / 임주민 / 개발자 / 자료취합
### 동작 방식
------------
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
------------
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
