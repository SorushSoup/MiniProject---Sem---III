import pygame
import sys
 
# Initialize Pygame
pygame.init()
 
# Constants
WIDTH, HEIGHT = 800, 600
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 
# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong Game')
 
# Function to display text
def draw_text(text, size, color, surface, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))
 
# Main menu function
def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text("Pong Game", 64, WHITE, screen, WIDTH // 2 - 150, HEIGHT // 4)
        draw_text("Press SPACE to Start", 36, WHITE, screen, WIDTH // 2 - 150, HEIGHT // 2)
        draw_text("Press ESC to Exit", 36, WHITE, screen, WIDTH // 2 - 150, HEIGHT // 2 + 50)
        pygame.display.flip()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
 
# Game loop
def game_loop():
    left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
 
    ball_speed = [5, 5]
    left_score, right_score = 0, 0
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
 
        # Move paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0: left_paddle.y -= 5
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT: left_paddle.y += 5
        if keys[pygame.K_UP] and right_paddle.top > 0: right_paddle.y -= 5
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT: right_paddle.y += 5
 
        # Move the ball
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]
 
        # Ball collision
        if ball.top <= 0 or ball.bottom >= HEIGHT: ball_speed[1] = -ball_speed[1]
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle): ball_speed[0] = -ball_speed[0]
 
        # Update score
        if ball.left <= 0:
            right_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
        if ball.right >= WIDTH:
            left_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
 
        # Draw everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
 
        # Draw scores
        draw_text(str(left_score), 50, WHITE, screen, WIDTH // 4, 20)
        draw_text(str(right_score), 50, WHITE, screen, WIDTH * 3 // 4 - 50, 20)
 
        pygame.display.flip()
        pygame.time.Clock().tick(60)
 
# Start the game
main_menu()