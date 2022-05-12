Null위한 정보 (9조 미니 프로젝트)
----------
![썸네일](https://user-images.githubusercontent.com/59018674/168022586-0316cb26-b545-48cb-91be-03fdf90a7cd5.png)


👋프로젝트 소개
----------
>개발이 처음이시라구요? 개발지식이 Null~인 널! 위한 개발 정보 공유 플랫폼입니다. 기술을 선택하고 관련 서적, 영상을 확인하세요! 나만 알고 있는 개발 정보가 있다면 포스팅 해봐요🔥

<br>


📺시연영상
----------
https://youtu.be/G3FS9qookyY
<br>


👨‍💻프로젝트 기간
----------
2022.05.09 ~ 05.12

<br>


🔨사용 기술
----------
>BackEnd
 <img src="https://img.shields.io/badge/flask-000000?style=flat&logo=Flask&logoColor=white"/>
 <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=MongoDB&logoColor=white"/>

  
>FrontEnd
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=HTML5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=CSS3&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=JavaScript&logoColor=white"/>
  <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=Bootstrap&logoColor=white"/>

👨🏻‍🤝‍👨🏻팀원 소개
----------
    ☀4인 1조 팀 프로젝트☀
  -박성규: 회원가입 FE & BE
  
  -박성렬: 메인페이지 FE & BE
  
  -최서호: 로그인 FE & BE
  
  -이기안: 디테일 FE & BE
    
  <br>


  💣트러블 슈팅
  ----------
  1. 몽고db localhost 27017 문제 -> 개인 클라우드로 url변경
  2. 회원가입db 와 로그인db 따로만들어서 변수값 통일 문제
    -> db url 및 변수 통일 후 해결.
  3. 게시물 좌측 정렬되는 문제
    ->margin: 20px auto 0px auto;
              width: 95%;
              max-width: 1200px; 추가로 가운데 정렬 완료.
  4. 이미지 화질이 좋지 않은 문제
->db에 이미지url 해상도 좋은 이미지로 변경,
class="row row-cols-1 row-cols-md-2 g-4"를
               class="row row-cols-1 row-cols-md-4 g-4"로 변경하여
한줄에 4개씩 나오게 하여 이미지 사이즈를 줄여서
이미지가 깨지는 문제 해결.

5. 파일 공유시 패키지 유무의 차이
-> 각 프로젝트별 venv가 아닌 외부라이브러리로 인터프리터
설정하여 매번 패키지 설치해야하는 문제 해결
