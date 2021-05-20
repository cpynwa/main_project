# main_project
실무에서 필요한 여러가지 유틸리티 모음
=====================

1. config finder
 - 주니퍼 config에서 인터페이스 기준으로 관련된 설정을 모두 찾아줌(현재까지 ipv6는 불가능)
 
2. optic finder
 - 주니퍼 장비명령어 특성상 인터페이스별로 어떠한 optic을 사용중인지 확인하기가 번거로움
 - 이런 어려움을 개선하고자 script로 optic을 찾아 interface와 매칭시켜줌
 
3. netconf Tester
 - 주니퍼 장비로 netconf를 사용하여 command 입력 기능
 - set system services netconf ssh
 - 장비에 위 명령이 추가되어야만 동작가능
 
4. 이후로 계속 추가 예정
