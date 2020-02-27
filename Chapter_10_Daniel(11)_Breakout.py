#-----------------------------------------------------------------------
#                   Chapter 10 Lab: Create-a-Quiz
#Name:Daniel (11)                                           
#Date:24/2/20
#This lab involves making Breakout!!!
#-----------------------------------------------------------------------


import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
DARK_RED = (123, 36, 28)
YELLOW = (241, 196, 15)


#Screen Resolution
size = (950,650)
screen = pygame.display.set_mode(size)


#Functions

def paddle(x):
    pygame.draw.rect(screen, WHITE, [x, 600, 100, 10])

def ball(x,y):
    pygame.draw.ellipse(screen, YELLOW, [x, y, 15, 15])

def destructible_blocks(x,y):
    pygame.draw.rect(screen, WHITE, [x, y, 50, 40])

def texts(points,location_x,location_y,text,colour,size):
   font=pygame.font.Font(None,size)
   scoretext=font.render(text+str(points), 1,colour)
   screen.blit(scoretext, (location_x, location_y))
   

def main():
    pygame.init()
    pygame.display.set_caption("Breakout")


    done = False
    start = False
    first = False
    once = True
    hit_detection = False
    final_life = False
    win = False
    
    clock = pygame.time.Clock()

    #Lists of destructible_blocks
    block_list = []
    blocklist_y = [10,90,170,250,330,410]
    blocklist_x = [10,70,130,190,250,310,370,430,490,550,610,670,730]
    for i in blocklist_y:
        for q in blocklist_x:
            block = [q,i]
            block_list.append(block)
            

    paddle_xspeed = 0
    x_speed =  0
    y_speed = 0
     

    paddle_xcoord = 360
    x_coord = 0
    y_coord = 580
    
    lives_left = 3
    points = 0
    
    #Key bindings
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle_xspeed = -10
                elif event.key == pygame.K_RIGHT:
                    paddle_xspeed = 10

                if start == False:
                    if event.key == pygame.K_SPACE:
                        y_speed = -5
                        start = True
     
            
            elif event.type == pygame.KEYUP:
                
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    paddle_xspeed = 0

     

             
        paddle_xcoord += paddle_xspeed





                
        if start == False:
            x_coord = paddle_xcoord + 40
            y_coord = 580

        #Code for the paddle
        if paddle_xcoord <= 0:
            paddle_xcoord = 0

        elif paddle_xcoord >= 700:
            paddle_xcoord = 700

        #Code for the ball
        if y_coord <= 0:
            y_speed = -y_speed
            first = True

        elif x_coord <= 0:
            x_speed = -x_speed
            first = True
        elif x_coord+15 >= 800:
            x_speed = -x_speed
            first = True

        #Checking for defeat
        if final_life == True:
            if y_coord+15 >= 650:
                texts('',400,205,"GAME OVER",YELLOW,80)
                
                
        #Restarting and life lost
        if lives_left > 0 :   
            if y_coord+15 >= 650:
                start = False
                first = False
                once = True
                lives_left -= 1
                y_speed = 0
                x_speed = 0
                

         
        #code if the paddle is hit on the sides
        if (y_coord <= 600 + 1) and (y_coord + 15 >= 600):
            if(x_coord + 15 >= paddle_xcoord) and (x_coord <= paddle_xcoord + 100):
                y_speed = -y_speed
                first = True

        elif (y_coord <= 600 + 10) and (y_coord + 15 >= 600):
            if(x_coord + 15 >= paddle_xcoord) and (x_coord <= paddle_xcoord + 100):
                x_speed = -x_speed
                first = True
                
        


        #Hit detection
        first_fail = True
        #Bottom 
        for coord in (block_list):
            if (y_coord + 15 >= coord[1] + 40) and (y_coord <= coord[1] + 40):
                if (x_coord + 15 >= coord[0]) and (x_coord <= coord[0] + 50):
                    y_speed = -y_speed
                    first = True
                    hit_detection = True
                    block_list.remove(coord)
                    points += 5

            #Top 
            elif (y_coord <= coord[1] + 1) and (y_coord + 15 >= coord[1]):
                if (x_coord + 15 >= coord[0]) and (x_coord <= coord[0] + 50):
                    y_speed = -y_speed
                    first = True
                    hit_detection = True
                    block_list.remove(coord)
                    points += 5


            #Sides
            elif (y_coord <= coord[1] + 40) and (y_coord + 15 >= coord[1]):
                if (x_coord + 15 >= coord[0]) and (x_coord <= coord[0] + 50):
                    x_speed = -x_speed
                    first = True
                    hit_detection = True
                    block_list.remove(coord)
                    points += 5

                    
        if once == True:
            if first == True:
                x_speed = -5
                once = False
                
        x_coord += x_speed
        y_coord += y_speed
        screen.fill(BLACK)

        #drawing paddles
        paddle(paddle_xcoord)
        pygame.draw.rect(screen, DARK_RED, [800, 0, 400, 700])


            
        #Drawing destructible_blocks
        for coord in (block_list):
            destructible_blocks(coord[0],coord[1])

        #Drawing ball
        ball(x_coord,y_coord)
        texts(points,820,125,"Points: ",WHITE,30)
        texts(lives_left,820,160,"Lives: ",WHITE,30)
        texts(' ',805,90,"BREAKOUT",WHITE,35)
       

        #Checks if player lost
        if points >= 390:
            texts('',150,230,"congratulations",YELLOW,100)
            win = True
            
        elif final_life == True:
            if win == False:
                if y_coord+15 >= 650:
                    texts('',200,230,"GAME OVER",YELLOW,100)
                    

        elif lives_left == 0:
            final_life = True
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


main()

# Good job.  The display is very aesthetically pleasing and it works.
# Your screen variable should not be global - it should be passed to your
# functions.
# Score: 100

