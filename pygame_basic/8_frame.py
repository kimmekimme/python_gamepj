import pygame
###############################################
#기본 초기화 (반드시 해야하는 것들)
pygame.init() #초기화

#화면 크기 세팅
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("kimme game")

#FPS
clock = pygame.time.Clock()
###############################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도 폰트 등)


#이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(30) #프레임/초 수 설정

#캐릭터가 100만큼 이동을 해야함
#10 fps : 1초 동안에 10번 동작 -> 1번에 몇만큼 이동? 10만큼 ! 10*10=100
#20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼! 5*20=100

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): #이벤트 체크
        if event.type == pygame.QUIT: #창을 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님
        
   
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt #이동속도 고정
    character_y_pos += to_y * dt

    # 4. 충돌 처리
  
   

    # 5. 화면에 그리기
    
    
    pygame.display.update() #게임화면 계속 그리기

    
pygame.quit()
