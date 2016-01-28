__author__ = 'becca.elenzil'

"""
Use sprites to collect blocks.

Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Explanation video: http://youtu.be/4W2AqUetBi4
"""
import random

from classes import *
from ProgrammingAppsCourse.Becca_PA.constants import *



# Initialize Pygame
pygame.init()


imageOne = pygame.image.load('clouds.png')
imageTwo = imageOne

speed = 2

# Set the height and width of the screen
w1 = imageOne.get_width()
h1 = imageOne.get_height()
w2 = imageTwo.get_width()
h2 = imageOne.get_height()

x1 = 0
x2 = w1

#screen_width = 700
#screen_height = 400
#screen = pygame.display.set_mode([screen_width, screen_height])


screen = pygame.display.set_mode((w1,h1))

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()
kill_block_list = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()


for i in range(200):
    # This represents a block
    block = Block(GREEN, 10, 10)

    # Set a random location for the block
    block.rect.x = random.randrange(w1)
    block.rect.y = random.randrange(h1)

    # Add the block to the list of objects
    good_block_list.add(block)
    all_sprites_list.add(block)

for i in range(100):
    # This represents a block
    block = Block(RED, 10, 10)

    # Set a random location for the block
    block.rect.x = random.randrange(w1)
    block.rect.y = random.randrange(h1)

    # Add the block to the list of objects
    bad_block_list.add(block)
    all_sprites_list.add(block)

for i in range(10):
    # This represents a block
    block = Block(BLACK, 20, 20)

    # Set a random location for the block
    block.rect.x = random.randrange(w1)
    block.rect.y = random.randrange(h1)

    # Add the block to the list of objects
    kill_block_list.add(block)
    all_sprites_list.add(block)

# Create a RED player block
player = Block(ORANGE, 15, 15)
player2 = Block(YELLOW, 15, 15)
all_sprites_list.add(player)
all_sprites_list.add(player2)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.

            if event.key == pygame.K_a:
                x_speed = -3
            elif event.key == pygame.K_d:
                x_speed = 3
            elif event.key == pygame.K_w:
                y_speed = -3
            elif event.key == pygame.K_s:
                y_speed = 3

            if event.key == pygame.K_j:
                x_speed2 = -3
            elif event.key == pygame.K_l:
                x_speed2 = 3
            elif event.key == pygame.K_i:
                y_speed2 = -3
            elif event.key == pygame.K_k:
                y_speed2 = 3

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_speed = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                y_speed = 0

            if event.key == pygame.K_j or event.key == pygame.K_l:
                x_speed2 = 0
            elif event.key == pygame.K_i or event.key == pygame.K_k:
                y_speed2 = 0
            #"""

    for block in kill_block_list:
        block.rect.x -= 2
        if block.rect.x <= 0:
            block.rect.x = w1

    for block in good_block_list:
        block.rect.y += 2
        if block.rect.y >= h1:
            block.rect.y = 0

    for block in bad_block_list:
        block.rect.y -= 2
        if block.rect.y <= 0:
            block.rect.y = h1

    x_coord += x_speed
    y_coord += y_speed
    x_coord2 += x_speed2
    y_coord2 += y_speed2

    # Clear the screen
    x1 -= speed
    x2 -= speed

    print x1,x2

    if x1 <= -1*w1:
        x1 = x2 + w2
    elif x2 <= -1*w2:
        x2 = x1 + w1

    # Set the player object to the mouse location
    player.rect.x = x_coord#pos[0]
    player.rect.y = y_coord#pos[1]

    player2.rect.x = x_coord2#pos[0]
    player2.rect.y = y_coord2#pos[1]

    # See if the player block has collided with anything.
    good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
    kill_blocks_hit_list= pygame.sprite.spritecollide(player, kill_block_list, True)

    good_blocks_hit_list2 = pygame.sprite.spritecollide(player2, good_block_list, True)
    bad_blocks_hit_list2 = pygame.sprite.spritecollide(player2, bad_block_list, True)
    kill_blocks_hit_list2= pygame.sprite.spritecollide(player2, kill_block_list, True)

    # Check the list of collisions.
    for block in good_blocks_hit_list:
        score += 1
        print(score)

    for block in bad_blocks_hit_list:
        score -= 1
        print(score)

    for block in kill_blocks_hit_list:
        score -= score
        print(score)

    for block in good_blocks_hit_list2:
        score2 += 1
        print(score2)

    for block in bad_blocks_hit_list2:
        score2 -= 1
        print(score2)

    for block in kill_blocks_hit_list2:
        score2 -= score2
        print(score2)

    #draw background
    screen.blit(imageOne, (x1, 0))
    screen.blit(imageTwo, (x2, 0))

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = font.render("Score: " + str(score),True, BLACK)
    text2 = font.render("Score: " + str(score),True, BLUE)

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [50, h1-100])
    screen.blit(text2, [w1-100, h1-100])


    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()



