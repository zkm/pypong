# PyPong

PyPong is a simple implementation of the classic Pong game using Pygame.

![PyPong Demo](demo.gif)

## Prerequisites

- Python 3.x
- Pygame

## Getting Started

1. Clone the repository:

   ```bash
   git clone git@github.com:zkm/pypong.git

2. Change into the project directory:

   ```bash
   cd pypong

3. Install the required dependencies:

   ```bash
   pip install pygame

4. Run the game:

   ```bash
   python pypong.py

## How to Play
- Player 1 (left paddle) controls:
  - Move up: <kbd>W</kbd>
  - Move down: <kbd>S</kbd>
- Player 2 (right paddle) is controlled by the computer.
- The objective is to hit the ball with your paddle and prevent it from going past your paddle.
- The ball will bounce off the paddles and the top/bottom walls.
- If the ball goes beyond the paddles' reach, it will reset to the center.
- The game ends when one player reaches a certain score (not implemented in this version).

## Customization
Feel free to customize the game by modifying the code:

- Adjust paddle speed: Modify the paddle_speed variable.
- Change window size: Update window_width and window_height.
- Modify ball speed: Adjust the ball_speed variable.
- Customize colors: Update the color constants (BLACK, WHITE, BLUE, RED) with RGB values.
- Add additional features and game rules as desired.

## Acknowledgements
- Pygame: https://www.pygame.org/

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE)  file for details.
