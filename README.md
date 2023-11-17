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
