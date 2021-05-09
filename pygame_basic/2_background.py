import pygame

pygame.init() #초기화

#화면 크기 세팅
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("kimme game")

#배경 이미지 불러오기
background = pygame.image.load("/Users/kimme/Desktop/pygame_pj/pygame_basic/다운로드.jpeg")#이미지경로
#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #이벤트 체크
        if event.type == pygame.QUIT: #창을 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님
   
    # screen.fill((0,0,255)) #r,g,b값
    screen.blit(background, (0.0)) #배경 그리기
    pygame.display.update() #게임화면 계속 그리기



#pygame 종료
pygame.quit()
