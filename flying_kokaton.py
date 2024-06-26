import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png") #練習２
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0
    dx,dy = 0,0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            dx,dy = 0,-1
        elif key_lst[pg.K_DOWN]:
            dx,dy = 0,1
        elif key_lst[pg.K_LEFT]:
            dx,dy = 0,0
        elif key_lst[pg.K_RIGHT]:
            dx,dy = 3,0
        else:
            dx,dy = 0,0
        kk_rct.move_ip([dx-1,dy])


        screen.blit(bg_img, [-(tmr%3200), 0]) #練習６
        screen.blit(bg_img2, [1600 - (tmr%3200), 0])
        screen.blit(bg_img, [3200 - (tmr%3200), 0]) #練習６
        screen.blit(bg_img2, [4800 - (tmr%3200), 0])
        screen.blit(kk_img, kk_rct) #練習４
        pg.display.update()
        tmr += 1        
        clock.tick(200)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()