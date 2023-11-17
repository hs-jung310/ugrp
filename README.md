# ugrp
fileupload(가칭) app 안에 구현
동작 방식 in view
1. fileupload() : request != post : fileupload.html
2. fileupload() : request == post : return loading() : generating image: return result.html with image

외부 접속 허용. 참고 사이트: 
https://velog.io/@devmin/Django-CORS-Setting-basic
이때 추가로 mysite/setting에서 허용 ip 수동 입력 해줘야 합니다. 코드 참고하시고 질문주세요. 
외부 ip 접속 시 포트포워딩 추가 설정 필요. 참고 자료 : https://hyunie-y.tistory.com/23
코드엔 외부 ip 노출 방지를 위해 지워놨습니다. 내부 ip 만 적어놨습니다. 참고하시고 질문주세요.

#수정해야 할 것
1. 코드 사용시 이용한건 prompt만 가지고 image 생성하는 모델입니다. 수정해야 합니다.
2. 화면 전환 작동 방식이 바뀌어야 합니다.
