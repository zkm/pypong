import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong")

# Set up game objects
paddle_width = 20
paddle_height = 100
paddle_speed = 5
paddle1_y = window_height // 2 - paddle_height // 2
paddle2_y = window_height // 2 - paddle_height // 2

ball_radius = 10
ball_speed = 3
ball_x = window_width // 2
ball_y = window_height // 2
ball_velocity_x = ball_speed
ball_velocity_y = ball_speed

# Set up AI variables
ai_paddle_speed = 3

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Function to handle paddle movement
def move_paddle(paddle_y, move_up, move_down):
    keys = pygame.key.get_pressed()
    if keys[move_up] and paddle_y > 0:
        paddle_y -= paddle_speed
    if keys[move_down] and paddle_y < window_height - paddle_height:
        paddle_y += paddle_speed
    return paddle_y

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BLACK)

    paddle1_y = move_paddle(paddle1_y, pygame.K_w, pygame.K_s)

    # AI opponent movement
    if paddle2_y + paddle_height // 2 < ball_y and paddle2_y < window_height - paddle_height:
        paddle2_y += ai_paddle_speed
    if paddle2_y + paddle_height // 2 > ball_y and paddle2_y > 0:
        paddle2_y -= ai_paddle_speed

    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Check for ball collision with paddles
    if (
        paddle1_y + paddle_height >= ball_y >= paddle1_y
        and ball_x <= paddle_width
    ) or (
        paddle2_y + paddle_height >= ball_y >= paddle2_y
        and ball_x >= window_width - paddle_width - ball_radius
    ):
        ball_velocity_x = -ball_velocity_x

    # Check for ball collision with walls
    if ball_y <= 0 or ball_y >= window_height - ball_radius:
        ball_velocity_y = -ball_velocity_y

    # Reset ball position if it goes beyond paddles' reach
    if ball_x <= 0 or ball_x >= window_width:
        ball_x = window_width // 2
        ball_y = window_height // 2

    pygame.draw.rect(window, WHITE, (0, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(window, WHITE, (window_width - paddle_width, paddle2_y, paddle_width, paddle_height))

    pygame.draw.circle(window, WHITE, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
