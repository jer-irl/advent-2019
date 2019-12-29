from collections import defaultdict
import curses
from time import sleep

from sols.sol13a import TileType, StepResult, write_output, IntCodeComputer, OPCODES


def char_for_tile(tile: TileType):
    if tile == TileType.BALL:
        return "O"
    elif tile == TileType.BLOCK:
        return "X"
    elif tile == TileType.EMPTY:
        return " "
    elif tile == TileType.HORIZONTAL_PADDLE:
        return "-"
    elif tile == TileType.WALL:
        return "|"
    raise RuntimeError("Unexpected tile type")


def draw_board(board, screen, score):
    screen.addstr(0, 0, str(score))
    screen.clrtoeol()
    for coord, tile in board.items():
        x, y = coord
        screen.addch(y + 1, x, char_for_tile(tile))

    screen.refresh()


def run_game(computer: IntCodeComputer, screen) -> int:
    board = defaultdict(int)
    score = 0
    sleep_time = 0.2
    should_cheat = False
    while True:
        computer_result = computer.run()
        output_tuples = [tuple(computer.context.output[x:x + 3]) for x in range(0, len(computer.context.output), 3)]
        for x, y, possible_score in reversed(output_tuples):
            if x == -1 and y == 0:
                score = possible_score
                break

        output_tuples = [(x, y, tile) for (x, y, tile) in output_tuples if not (x == -1 and y == 0)]

        write_output(
            board,
            output_tuples
        )

        computer.context.output.clear()
        draw_board(board, screen, score)

        if TileType.BLOCK not in board.values():
            break

        if computer_result == StepResult.HALT:
            break
        elif computer_result == StepResult.INPUT:
            c = screen.getch()
            if c == curses.KEY_LEFT and not should_cheat:
                computer.context.input.append(-1)
            elif c == -1 and not should_cheat:
                computer.context.input.append(0)
            elif c == curses.KEY_RIGHT and not should_cheat:
                computer.context.input.append(1)
            elif c == ord("q"):
                break
            # cheat code is spacebar
            elif c == ord(" ") or should_cheat:
                should_cheat = True
                sleep_time = 0.01
                paddle_coord = None
                ball_coord = None
                for coord, tile in board.items():
                    if tile == TileType.BALL:
                        ball_coord = coord
                    elif tile == TileType.HORIZONTAL_PADDLE:
                        paddle_coord = coord

                if paddle_coord[0] > ball_coord[0]:
                    computer.context.input.append(-1)
                elif paddle_coord[0] == ball_coord[0]:
                    computer.context.input.append(0)
                elif paddle_coord[0] < ball_coord[0]:
                    computer.context.input.append(1)
                else:
                    raise RuntimeError("Weird equality class?")

            sleep(sleep_time)

    return score


def run(data):
    program = [int(x) for x in data.split(",")]
    program[0] = 2
    computer = IntCodeComputer(program, OPCODES)

    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.nodelay(True)
    screen.keypad(True)

    result = run_game(computer, screen)

    curses.endwin()

    return result
