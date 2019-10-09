# Orthello - DYOA at TU Graz WS 2019
# Name:       Manuel Sammer
# Student ID: 11903022

# STATIC STRINGS - DO NOT CHANGE

TERMINAL_COLOR_NC = '\033[0m'
TERMINAL_COLOR_1 = '\033[94m'
TERMINAL_COLOR_2 = '\033[92m'
TERMINAL_COLOR_EMPTY = '\033[93m'
TERMINAL_COLOR_ERROR = '\033[91m'

ERROR_INVALID_INPUT = TERMINAL_COLOR_ERROR + "[ERROR]" + TERMINAL_COLOR_NC + " Invalid Input"
ERROR_NOT_ALLOWED = TERMINAL_COLOR_ERROR + "[ERROR]" + TERMINAL_COLOR_NC + " Stone is not allowed to be placed here"
ERROR_OCCUPIED = TERMINAL_COLOR_ERROR + "[ERROR]" + TERMINAL_COLOR_NC + " Field already occupied"

PROMPT_HUMAN_AI = "Play against a [human] or an [ai]? "

PROMPT_PLAYER_1 = TERMINAL_COLOR_1 + "player1>" + TERMINAL_COLOR_NC + " "
PROMPT_PLAYER_2 = TERMINAL_COLOR_2 + "player2>" + TERMINAL_COLOR_NC + " "
PROMPT_AI = TERMINAL_COLOR_2 + "ai plays>" + TERMINAL_COLOR_NC + " "

WON_PLAYER_1 = TERMINAL_COLOR_1 + "[player1]" + TERMINAL_COLOR_NC + " has won!"
WON_PLAYER_2 = TERMINAL_COLOR_2 + "[player2]" + TERMINAL_COLOR_NC + " has won!"
WON_DRAW = "It's a " + TERMINAL_COLOR_EMPTY + "[DRAW]" + TERMINAL_COLOR_NC

STATISTICS_1 = "[STATS]" + TERMINAL_COLOR_1 + "[player1]=" + TERMINAL_COLOR_NC
STATISTICS_2 = "[STATS]" + TERMINAL_COLOR_2 + "[player2]=" + TERMINAL_COLOR_NC

INPUT_HUMAN = "human"
INPUT_COMPUTER = "ai"
INPUT_SKIP = "skip"
INPUT_QUIT = "quit"

# END OF STATIC STRINGS

RowConverterDictionary = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7
}


class StoneColours:
    Black = 1
    White = 2


class Players:
    Player_1 = 1
    Player_2 = 2


class OpponentTypes:
    Human = "human"
    AI = "ai"


class GameBoard:

    # Constructor
    def __init__(self):
        # Instance Members
        self.game_field = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

    # A function to print the game field (provided by the assignment).
    def PrintBoard(self):
        print("\n   ┌───┬───┬───┬───┬───┬───┬───┬───┐")

        row_keys = ["A", "B", "C", "D", "E", "F", "G", "H"]

        row_count = 0

        for row in self.game_field:
            column_string = " " + row_keys[row_count] + " │";
            for column in row:
                if column == 1:
                    column_text = TERMINAL_COLOR_1 + "1" + TERMINAL_COLOR_NC
                elif column == 2:
                    column_text = TERMINAL_COLOR_2 + "2" + TERMINAL_COLOR_NC
                else:
                    column_text = TERMINAL_COLOR_EMPTY + "0" + TERMINAL_COLOR_NC

                column_string += " " + column_text + " │"
            print(column_string)

            row_count = row_count + 1
            if (row_count < len(self.game_field)):
                print("   ├───┼───┼───┼───┼───┼───┼───┼───┤")

        print("   └───┴───┴───┴───┴───┴───┴───┴───┘")
        print("     0   1   2   3   4   5   6   7  ")

    # A function to set a stone on the game field
    def SetStoneToBoard(self, position, colour):
        try:
            if (colour != StoneColours.Black & colour != StoneColours.White):
                raise
            self.game_field[position[0]][position[1]] = colour
        except:
            print(ERROR_INVALID_INPUT)

class PlayerInput:
  def  __init__(self):
    self.input = ""

class Game:

    def __init__(self):
        self.game_board = GameBoard()
        self.current_player = Players.Player_1
        self.game_running = False

    def StartGame(self):
        if not self.game_running:
            self.game_running = True
            enemy_choice = input(PROMPT_HUMAN_AI)
            while (enemy_choice != OpponentTypes.Human) & (enemy_choice != OpponentTypes.AI):
                print(ERROR_INVALID_INPUT)
                enemy_choice = input(PROMPT_HUMAN_AI)
            else:
                while self.game_running:
                  player_input = PlayerInput()
                  while(True):
                    if self.current_player == Players.Player_1:
                        player_input.input = input(PROMPT_PLAYER_1)

                    else:
                        player_input.input = input(PROMPT_PLAYER_2)
                    #TODO: Add Check for PlayerInput in PlayerInput Class
                    break
        else:
            print("Error: Game already running")


def StopGame(self):
    if self.game_running:
        self.game_running = False
    else:
        print("Error: Game is currently not running")


def main():
    print('\x1b[0;30;41m' + "Welcome to othello by Manuel Sammer" + '\x1b[0m')
    current_game = Game()
    current_game.StartGame()


if __name__ == "__main__":
    main()
