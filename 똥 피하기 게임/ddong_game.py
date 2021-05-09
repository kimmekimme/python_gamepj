import random
import pygame
###############################################
#기본 초기화 (반드시 해야하는 것들)
pygame.init() #초기화

#화면 크기 세팅
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("똥 피하기 게임")

#FPS
clock = pygame.time.Clock()
###############################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도 폰트 등)
background = pygame.image.load("") #배경 이미지 파일 경로
character = pygame.image.load("") #캐릭터 이미지 파일 경로
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_width/2)
character_y_pos = screen_height - character_height

# 이동 위치
to_x = 0
character_speed = 10

# 똥 만들기
ddong = pygame.image.load("") #똥 이미지 파일 경로
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width-ddong_width)
ddong_y_pos = 0
ddong_speed = 10



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
        if event.type = pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key = pygame.K_RIGHT:
                to_x += character_speed
        if event.type = pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
        
   
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt #이동속도 고정
    character_y_pos += to_y * dt

    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    ddong_y_pos += ddong_speed

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width-ddong_width)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = characcharacter_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos
    
    if character_rect.collidedict(ddong_rect)
        print("Game Over/by kimme")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong,(ddong_x_pos, ddong_y_pos))
    
    pygame.display.update() #게임화면 계속 그리기

    
pygame.quit()
