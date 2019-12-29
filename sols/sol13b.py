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

        if computer_result == StepResult.HALT:
            break
        elif computer_result == StepResult.INPUT:
            c = screen.getch()
            if c == curses.KEY_LEFT:
                computer.context.input.append(-1)
            elif c == -1:
                computer.context.input.append(0)
            elif c == curses.KEY_RIGHT:
                computer.context.input.append(1)
            elif c == ord("q"):
                break
            sleep(1)

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
