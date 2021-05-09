import pygame

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

    # screen.fill((0,0,255)) #r,g,b값
    screen.blit(background, (0.0)) #배경 그리기
    
    screen.blit(character,(character_x_pos,character_y_pos)
      
    pygame.display.update() #게임화면 계속 그리기
    


#pygame 종료
pygame.quit()
