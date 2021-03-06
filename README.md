
# Qlik Sense Portal


## QMC 설정


![Alt Text](https://github.com/HyunAm0225/gt-qlik/blob/master/gif/QMC설정.PNG)


## 인증 방식


- Qlik Sense와 Django의 인증 방식은 Ticket인증방식을 사용했습니다.

  

## 실행하기전 준비


### secret.json 만들기


최상단에 secret.json이라는 파일을 만들어서 다음과 같이 입력해줍니다.

  

![Alt Text](https://github.com/HyunAm0225/gt-qlik/blob/master/gif/secret_json.PNG)

  

### requirements.txt를 통한 패키지 종속성 관리
  
  다음과 같은 명령어를 입력해서 빠르게 패키지를 설치합니다.

    pip install -r requirements.txt

  
  

# App 구성

  

  

### accounts

  

  

- 유저의 계정 정보를 관리하는 앱입니다.

  

  

###  chart

  

  

- Qlik Sense Sheet안에 있는 chart를 관리 하는 앱입니다.

  

  

###  main

  

  

- 메인 화면을 보여주기 위해 만들어준 앱 입니다. Menu앱에서 등록한 sheet들을 iframe을 통해 볼 수 있습니다.

  

  

###  menu

  

  

- Qlik Sense에서 App안에 있는 sheet를 관리하는 앱 입니다.

  

  

###  cart

  

  

- Qlik Sense에서 만든 Chart를 개인화면에 구현하기 위한 장바구니 입니다.

  

  

# 개인화 실행 화면

  

  

![Alt Text](https://github.com/HyunAm0225/gt-qlik/blob/master/gif/Qlik-SSO.gif)