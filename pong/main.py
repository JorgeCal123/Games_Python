import pygame



#Lista de colores
#Lista de colores

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)   
GREEN = (0,255,0)
BLUE = (0,0,255)

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

x1 = 50
y1 = 300

x2 = 700
y2 = 300

ball_x = 400
ball_y = 300


speed_1 = 0
speed_2 = 0
speed_ball_x = 3
speed_ball_y = 3
if __name__=="__main__":
    pygame.init()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            # Precionas una tecla
            if event.type == pygame.KEYDOWN:
                print(y1)
                if event.key == pygame.K_DOWN:
                        speed_2 = 3
                if event.key == pygame.K_UP:
                        speed_2 = -3
                if event.key == pygame.K_w:
                        speed_1 = -3
                if event.key == pygame.K_s:
                        speed_1 = 3

            # Soltar la tecla presionada
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    speed_2 = 0
                if event.key == pygame.K_UP:
                    speed_2 = 0
                if event.key == pygame.K_w:
                    speed_1 = 0
                if event.key == pygame.K_s:
                    speed_1 = -0


        # movimiento y colision con los bordes del PLAYER 1
        if y1 <= 50:
            y1 = 50
        else:
            y1 += speed_1
        
        if y1 >= 550:
            y1 = 550
        else:
            y1 += speed_1

        # movimiento y colision con los bordes del PLAYER 2
        if y2 <= 50:
            y2 = 50
        else:
            y2 += speed_2
        
        if y2 >= 550:
            y2 = 550
        else:
            y2 += speed_2

        #movimiento de la pelota
        if ball_x > 790 or ball_x < 0:
            speed_ball_x *= -1
        if ball_y > 590 or ball_y< 0:
            speed_ball_y *= -1
        ball_x += speed_ball_x
        ball_y += speed_ball_y

        screen.fill(BLACK)
        player1 = pygame.draw.rect(screen, RED, (x1, y1 -45, 15, 90))
        player2 = pygame.draw.rect(screen, BLUE, (x2, y2 -45, 15, 90))

        ball = pygame.draw.circle(screen, WHITE,(ball_x, ball_y), 10)

        if ball.colliderect(player1) or ball.colliderect(player2):
            speed_ball_x *= -1

        pygame.display.flip()

        clock.tick(60)

