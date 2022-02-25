import pygame as p
s1  = 3
p.init() #파이게임 초기화

screen = p.display.set_mode([1000,1000]) #해상도 설정

p.display.set_caption("키보드 이미지 제어") #게임창 제목

#그림삽입
im = p.image.load("w.png")#이미지 변수에 저장  
im2 = p.image.load("f.png")

im_rect = im.get_rect(left = 100, top = 100) #left = x좌표 , top = y좌표

im2_rect = im.get_rect(left = 100, top = 800)
print(im_rect) 

playing = True

while playing:
    for event in p.event.get(): #사용자가 뭘 눌렀는지 확인
        if event.type == p.QUIT: #파이게임 x버튼을 눌렀을때
            p.quit() # 끄는 명령어
            quit() #결과창 끄는 명령어
            playing =  False #작동 중지
    if event.type == p.KEYDOWN:#키보드를 눌렀을때 
        if event.key == p.K_UP: #위쪽 방향키를 눌렀을때
            im_rect.top  =  im_rect.top-1 
        if event.key == p.K_DOWN: #아래쪽 방향키를 눌렀을때
            im_rect.top = im_rect.top+1 
        if event.key == p.K_LEFT: #왼쪽 방향키를 눌렀을때
            im_rect.left = im_rect.left - 1
        if event.key == p.K_RIGHT: #오른쪽 방향키를 눌렀을때
            im_rect.left = im_rect.left+1

    im2_rect.left = im2_rect.left + s1 
    if im2_rect.left <= 0:
        s1= 3
    elif im2_rect.left >=900:
        s1 = -3
        
        
    screen.fill([255,255,255]) #창 색깔 바꾸기
    screen.blit(im,im_rect)
    screen.blit(im2,(im2_rect))

    #이미지 충돌 조건 
    if im_rect.colliderect(im2_rect):#이미지 좌표변수.colliderect(충돌할 좌표 변수) :
        p.quit()
    
    p.display.flip() #화면 업데이트 기능
    
