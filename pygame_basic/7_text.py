import pygame
#배경 640*480
#캐릭터 70*70

pygame.init() #초기화

#화면 크기 세팅
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("kimme game")

#FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("/Users/kimme/Desktop/pygame_pj/pygame_basic/다운로드.jpeg")#이미지경로

#캐릭터(스프라이트)불러오기
character = pygame.image.load("") #크기 70*70 빨간이미지 넣기
character_size = character.get_rect().size #이미지 크기 구해옴
character_width = character_size[0] #캐릭터 가로크기
character_height = character_size[1] #캐릭터 세로크기
character_x_pos = (screen_width / 2) - (character_width  / 2)# 화면가로의 절반크기에 해당하는곳에 위치 (가로)
character_y_pos = screen_height - character_height# 화면세로크기 가장 하래에 해당하는 곳에 위치 (세로)

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6

#적 캐릭터
enemy = pygame.image.load("") #크기 70*70 노랑이미지 경로 넣기
enemy_width = character_size[0] #캐릭터 가로크기
enemy_height = character_size[1] #캐릭터 세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width  / 2)# 화면가로의 절반크기에 해당하는곳에 위치 (가로)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)# 화면세로크기 가장 하래에 해당하는 곳에 위치 (세로)

#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체생성(폰트,크기)

#총 시간
total_time = 10

#시작 시간
start_ticks = pygame.time.get_ticks() #시작 tick



#이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) #프레임/초 수 설정

#캐릭터가 100만큼 이동을 해야함
#10 fps : 1초 동안에 10번 동작 -> 1번에 몇만큼 이동? 10만큼 ! 10*10=100
#20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼! 5*20=100


    for event in pygame.event.get(): #이벤트 체크
        if event.type == pygame.QUIT: #창을 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님
        
        if event.type == pygame.KEYDOWN: #키가 눌러지면
            if event.key == pygame.K_LEFT:
                to_x -= character_speed  #5만큼 왼쪽으로 이동
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed 
            elif event.key == pygame.K_UP:
                to_y -= character_speed 
            elif event.key == pygame.K_DOWN:
                to_y += character_speed 
        
        if event.type == pygame.KEYUP: #방향키를 떼면
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    

    character_x_pos += to_x * dt #이동속도 고정
    character_y_pos += to_y * dt

     #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width
        character_x_pos = screen_width - 
        
    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    #충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos 
    enemy_rect.top = enemy_y_pos 

    #충돌 체크
    if character_rect.collidedict(enemy_rect): #사각형기준으로 충돌확인api
        print("충돌했어요")
        running = False 


    # screen.fill((0,0,255)) #r,g,b값
    screen.blit(background, (0.0)) #배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos)) #캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) #적 그리기
    
    #타이머 집어넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    #경과 시간(ms)을 천으로 나누어서 초(s)단위로 표시
    timer = game_font.render(str(int(total_time - elapsed_time)),True,(255,255,255))
    #출력할 글자, true, 글자 색상
    
    #그려주기
    screen.blit(timer,(10,10))

     #시간이 0이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False
    
    
    pygame.display.update() #게임화면 계속 그리기

    

pygame.time.delay(2000) #2초 대기
#pygame 종료
pygame.quit()

