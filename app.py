import os
import time
import random
import msvcrt  # Works on Windows. For Mac/Linux, use 'readchar' library.

def play_game():
    # Game Settings
    width = 20
    height = 15
    player_pos = width // 2
    asteroids = []
    score = 0
    game_speed = 0.1

    print("CONTROLS: 'a' for Left, 'd' for Right. Press any key to start!")
    msvcrt.getch()

    try:
        while True:
            # 1. Generate new asteroids at the top
            if random.random() < 0.3:
                asteroids.append([random.randint(0, width - 1), 0])

            # 2. Handle Input
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8').lower()
                if key == 'a' and player_pos > 0:
                    player_pos -= 1
                elif key == 'd' and player_pos < width - 1:
                    player_pos += 1

            # 3. Update Asteroid Positions
            for ast in asteroids:
                ast[1] += 1
            
            # Remove off-screen asteroids
            asteroids = [ast for ast in asteroids if ast[1] < height]

            # 4. Check Collision
            for ast in asteroids:
                if ast[0] == player_pos and ast[1] == height - 1:
                    print(f"\n💥 CRASH! Final Score: {score}")
                    return

            # 5. Draw the Frame
            os.system('cls' if os.name == 'nt' else 'clear')
            for y in range(height):
                line = ""
                for x in range(width):
                    if x == player_pos and y == height - 1:
                        line += "^"  # Your Ship
                    else:
                        is_asteroid = False
                        for ast in asteroids:
                            if ast[0] == x and ast[1] == y:
                                line += "*"
                                is_asteroid = True
                                break
                        if not is_asteroid:
                            line += "."
                print(line)
            
            score += 1
            time.sleep(game_speed)

    except KeyboardInterrupt:
        print("\nMission Aborted.")

if __name__ == "__main__":
    play_game()