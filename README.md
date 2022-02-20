# MapleJhillaTimer
진힐라 하드/노말 자동 주기 계산 타이머

- 실행 파일 : dist 폴더 내 존재

## 요구 사항
### 메이플스토리 게임창
- 1366x768, 창모드
- `창모드 시 화면 밖에 채팅창 표시`는 상관 없으나,
- 1366x768 크기의 화면이 가려지지 않도록 위치 시키는 것이 좋음

## 사용 방법
![image](https://user-images.githubusercontent.com/89760255/154830358-6253a20c-75e5-4b55-af10-15de5bb4b8e6.png)

- 진힐라 입장과 동시에 `시작` 버튼 누르기

![image](https://user-images.githubusercontent.com/89760255/154830401-7f88821d-65d3-476b-b8a3-3a1872190b29.png)

- 타이머의 현재 시간이 게임 내 남은 시간과 일치하도록 `1초+`, `1초-` 버튼을 눌러 조정
- 이후부터 타이머가 자동으로 낫베기 패턴을 인식하고 다음 낫베기 시간과 그때까지 남은 시간을 계산하여 표시함.
- `리셋`버튼으로 초기상태로 되돌림.
### 소리 알림
- 낫베기 1분 전에 알림
- 낫베기 후 다음 시간 알림

## 소스 파일
- `main.py` : 메인 소스
- `%d.mp3` : 0~9까지 숫자 소리
- `1mleft.mp3` : 1분 남았을 때 소리
- `nextpt.mp3` : 다음 패턴 알림 소리
### 필요 패키지
- 파이썬 3.9.5
- tkinter : 내장
- time : 내장
- pygame
- Pillow
- numpy
- opencv-python
- pypiwin32

### 간단한 원리
- 메이플 화면을 기준으로 스크린샷을 찍음
- 스크린샷에서 다음 색상을 찾음
  - 진힐라 체력바의 20퍼, 40퍼 지점의 색상
  - 낫베기할 때 낫의 빨간색, 검은색이 나오는 지점의 색상
- 낫베기 감지 후 20퍼, 40퍼 색상이 1~4페이즈에 중 어디에 해당하는 지 확인
- 페이즈에 따른 새로운 주기 계산
