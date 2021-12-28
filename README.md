> # 네이밍
>     - 변수명: 스네이크_케이스(bms_rack_log)
>     - 함수명 및 메서드명: 스네이크_케이스(decode_u32)
>     - 클래스명: 첫 글자 대문자, 이후 카멜케이스(UserBaseModel)
>     - 패키지 및 모듈(파일): 스네이크 케이스(menu_info.py) 
---
> # port 규칙
>     - local: nines_api -> 11001, octo_auth -> 11003
>     - dev / stage / prod: 프로젝트별 nginx, gunicorn 포트 할당 
>         - nginx: 11001 ~ 11020 (현재 11001-nines_api, 11003-octo_auth)
>         - gunicorn: 17801 ~ 17820 (현재 17801-nines_api, 17803-octo_auth)
>         
>         * nginx - gunicorn 포트 끝 숫자 맞추기

---
> # 코딩 컨벤션
> ## PEP8대로 코드 작성(pylint 활용)
> 몇 가지 예:
>    * 여러 라이브러리 한줄에 import 하지 않기
>       ~~~
>       # 잘못된 예
>       import sys, os, time 
>       
>       # 올바르 예
>       import sys
>       import os
>       import time
>       
>       # 예외 ( from ~ import ~ )
>       from tensorflow.keras import Sequential, layers
>       ~~~
>       
>    * 클래스 시작부 위에 두칸 띄우기(간격 두기)
>    * 함수는 한 칸
>    * 제일 마지막 줄 한칸 띄우기
---
> # 폴더 구조
>     * api: api 엔드포인트(라우터), 서비스(services) 폴더
>     * common_utils: 공통적인 모듈 모아두는 폴더
>     * crud: db에 쿼리 보내고, 결과 반환하는 코드들
>     * database: 데이터베이스 연결 하는 부분
>     * models: pydantic 모델 모아두는 폴더
>     * tests: 테스트 파일들 모아놓은 폴더
>     
>      octo_auth
>        │
>        ├── src/                                 - 어플리케이션 폴더
>        │   ├── __init__.py                      - 서버 파이썬 모듈 초기화
>        │   │── main.py                          - 서버 실행 부분
>        │   ├── errors.py                        - 422 에러, 나머지 전체 에러 처리
>        │   │ 
>        │   ├── api/                  
>        │   │   ├── urls.py                      - 라우터 등록하는 파일
>        │   ├── common_utils/         
>        │   │   ├── api_history/                 - api_history 관련 공통 모듈 폴더         
>        │   │   │   └── api_history_doc.py       - api_history_doc 관련 함수 모아놓는 파일    
>        │   │   │
>        │   │   ├── date/                        - date 관련 공통 모듈 폴더         
>        │   │   │   └── date_utils.py            - date 관련 함수 모아놓는 파일(예시)    
>        │   │   │
>        │   │   └── log                          - log 관련 공통 모듈 폴더          
>        │   │       └── log_utils.py             - log 관련 함수 모아놓는 파일(미완성)  
>        │   │ 
>        │   ├── crud/         
>        │   │   ├── mongodb/                     - 몽고디비 crud 파일 및 폴더
>        │   │   │   ├── meta/                    - meta 데이터베이스 폴더
>        │   │   │   │
>        │   │   │   └── session/                 - session 데이터베이스 폴더  
>        │   │   │       └── session.py           - session 컬렉션 파일      
>        │   │   │
>        │   ├── database/         
>        │   │   ├── __init__.py       
>        │   │   ├── base.py                      - db 공통 동작들 모아놓는 파일
>        │   │   ├── mariadb.py                   - mariadb 관련 함수들 모아놓는 파일 (예시)
>        │   │   └── mongodb.py                   - mongodb 연결 관련 함수들(host, client)
>        │   │ 
>        │   ├── models/
>        │   │ 
>        │   └── tests/                 
>        │       ├── test_mongodb.py              - mongodb.py에 대한 테스트 파일(미완성)
>        │       └── test_main.py                 - main.py에 대한 테스트 파일(미완성)
>        │ 
>        ├── README.md                            - 리드미 파일
>        ├── install.sh                           - 설치해야할 라이브러리들 모아놓은 스크립트
>        └── restart.sh                           - nginx, gunicorn 재시작 스크립트
>
