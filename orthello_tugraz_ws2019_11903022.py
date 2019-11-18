# Orthello - DYOA at TU Graz WS 2019
# Name:       Manuel Sammer
# Student ID: 11903022

# TODO Refactoring, Testing, Commenting

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

# TODO Constants for Max and MIN Board Length/Widht (Row/Column)

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


class Players:
    Player_1 = 1
    Player_2 = 2


class Alignment:
    Horizontal = 1
    Vertical = 2
    Diagonal = 3


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

    # A function to set a stone on the game field or change an existing stone colour
    def SetStoneToBoard(self, position, player):
        valid_move = False
        enclosed_stones = self.GetEnclosedStones(position, player)
        if len(enclosed_stones) > 0:
            row_number = int(position[0])
            col_number = int(position[1])
            self.game_field[row_number][col_number] = player
            self.TurnStones(enclosed_stones)
            valid_move = True
        return valid_move

    # A function to change an arrays of stones to the opposite colour
    def TurnStones(self, stones):
        for position in stones:
            row_number = int(position[0])
            col_number = int(position[1])
            if self.game_field[row_number][col_number] == Players.Player_1:
                self.game_field[row_number][col_number] = Players.Player_2
            else:
                self.game_field[row_number][col_number] = Players.Player_1

    # A function which returns if a field on the board is empty or not
    def IsFieldEmpty(self, position):
        try:
            row_number = int(position[0])
            col_number = int(position[1])
            return self.game_field[row_number][col_number] == 0
        except:
            print(ERROR_INVALID_INPUT)

    # A function which returns if a field is on the game_board or not
    def IsFieldValid(self, position):
        try:
            row_number = int(position[0])
            col_number = int(position[1])
            return (row_number <= 7) & (col_number <= 7) & (row_number >= 0) & (row_number >= 0)
        except:
            return False

    # A function which returns all correctly enclosed stones in a given range and alignment
    def DetectEnclosedStonesInRange(self, position, colour, matrix_range, alignment):
        row_number = int(position[0])
        col_number = int(position[1])
        row = row_number

        same_colour_stone_found = False
        enclosed_stones = []

        for x in range(matrix_range[0], matrix_range[1], matrix_range[2]):

            # Add cases for all directions so we can use 1 function to detect enclosed stone
            # TODO better comments and maybe refactor
            if alignment == Alignment.Horizontal:
                row = row_number
                col = x
            elif alignment == Alignment.Vertical:
                row = x
                col = col_number
            else:
                col = x
                row = row + matrix_range[3]
                # Exit detection if we move outside bounds
                if (row > 7) | (row < 0):
                    break

            if self.game_field[row][col] == colour:
                # If we find a same coloured stone set found = true and exit ->
                # all enclosed stone till now are returned, no empty field in between possible because we exit
                same_colour_stone_found = True
                break
            elif self.game_field[row][col] == 0:
                # Remove all found other coloured stones and exit
                enclosed_stones = []
                break
            else:
                # Always add stone -> Stones are emptied as soon as a game rule is broken
                enclosed_stones.append(str(row) + str(col))

        # No Stones are enclosed if we haven found a stone of the same colour
        if not same_colour_stone_found:
            enclosed_stones = []
        return enclosed_stones

    # A function which returns all correctly enclosed stones by a placed stone of a player
    def GetEnclosedStones(self, position, player):

        enclosed_stones = []
        row_number = int(position[0])
        col_number = int(position[1])

        # Left
        enclosed_stones.extend(
            self.DetectEnclosedStonesInRange(position, player, [col_number - 1, 0, -1], Alignment.Horizontal))
        # Right
        enclosed_stones.extend(
            self.DetectEnclosedStonesInRange(position, player, [col_number + 1, 8, +1], Alignment.Horizontal))
        # Up
        enclosed_stones.extend(
            self.DetectEnclosedStonesInRange(position, player, [row_number - 1, 0, -1], Alignment.Vertical))
        # Down
        enclosed_stones.extend(
            self.DetectEnclosedStonesInRange(position, player, [row_number + 1, 8, +1], Alignment.Vertical))
        # Left Upper
        enclosed_stones.extend(
            self.DetectEnclosedStonesInRange(position, player, [col_number - 1, 0, -1, -1], Alignment.Diagonal))
        # Right Lower
        enclosed_stones.extend(
            self.DetectEnclosedStonesInRange(position, player, [col_number + 1, 8, +1, +1], Alignment.Diagonal))
        # Left Lower
        enclosed_stones.extend(
            self.DetectEnclosedStonesInRange(position, player, [col_number - 1, 0, -1, +1], Alignment.Diagonal))
        # Right Upper
        enclosed_stones.extend(
            self.DetectEnclosedStonesInRange(position, player, [col_number + 1, 8, +1, -1], Alignment.Diagonal))

        # Return enclosed stones by placed stone
        return enclosed_stones

    # A function which returns if for a given player a valid move is possible
    def IsValidMovePossible(self, player):
        for col in range(0, 8, +1):
            for row in range(0, 8, +1):
                # Only Checks Fields if not empty, if empty then second statement is not run
                if self.IsFieldEmpty([row, col]) & len(self.GetEnclosedStones([row, col], player)) > 0:
                    return True
        return False

    def PrintStats(self):
        player_1_stones = self.CountStonesOfPlayer(Players.Player_1)
        player_2_stones = self.CountStonesOfPlayer(Players.Player_2)
        print(STATISTICS_1 + str(player_1_stones))
        print(STATISTICS_2 + str(player_2_stones))
        if player_1_stones > player_2_stones:
            print(WON_PLAYER_1)
        elif player_1_stones < player_2_stones:
            print(WON_PLAYER_2)
        else:
            print(WON_DRAW)

    def GetVictor(self):
        player_1_stones = self.CountStonesOfPlayer(Players.Player_1)
        player_2_stones = self.CountStonesOfPlayer(Players.Player_2)
        if player_1_stones > player_2_stones:
            victor = 1
        elif player_1_stones < player_2_stones:
            victor = 2
        else:
            victor = 3
        return victor

    def CountStonesOfPlayer(self, player):
        stone_count = 0
        for row in range(0, 8, +1):
            for col in range(0, 8, +1):
                if (not self.IsFieldEmpty([row, col])) & (self.game_field[row][col] == player):
                    stone_count += 1
        return stone_count

    def IsBoardFull(self):
        # Returns True if all elements have a true value -> > 0
        for x in range(len(self.game_field[0])):
            if not all(self.game_field[x]):
                return False
        return True

    def GetMoveWithMostStonesTurned(self, player):
        stones_turned = 0
        position = []

        for row in range(0, 8, +1):
            for col in range(0, 8, +1):
                if self.IsFieldEmpty([row, col]):
                    new_stones_turned = self.GetEnclosedStones([row, col], player)
                    if len(new_stones_turned) > stones_turned:
                        stones_turned = len(new_stones_turned)
                        position = [row, col]
        return position


class ArtificialIntelligence:
    @staticmethod
    def ProcessAIInput(game_board, valid_move_possible, player):
        if valid_move_possible:
            position_best_move = ArtificialIntelligence.CalculateBestMove(game_board, player)
            print(PROMPT_AI + " " + str(position_best_move))
            game_board.SetStoneToBoard(position_best_move, player)

    @staticmethod
    def CalculateBestMove(game_board, player):
        # Placeholder Method for eventual better ai routine
        return game_board.GetMoveWithMostStonesTurned(player)


class PlayerInput:

    @staticmethod
    def PromptAndProcessPlayerInput(player, game_board, valid_move_possible):
        input_not_validated = True
        while input_not_validated:
            player_input = PlayerInput.PromptPlayerForInput(player)
            if player_input == INPUT_QUIT:
                exit(0)
            elif (player_input == INPUT_SKIP) & valid_move_possible:
                print(ERROR_INVALID_INPUT)
            elif player_input != INPUT_SKIP:
                player_input = PlayerInput.ConvertRowLetterToRowNumber(player_input)
                if len(player_input) == 0:
                    print(ERROR_INVALID_INPUT)
                elif not game_board.IsFieldValid(player_input):
                    print(ERROR_INVALID_INPUT)
                elif not game_board.IsFieldEmpty(player_input):
                    print(ERROR_OCCUPIED)
                else:
                    if game_board.SetStoneToBoard(player_input, player):
                        input_not_validated = False
                    else:
                        print(ERROR_NOT_ALLOWED)
            else:
                break

    @staticmethod
    def PromptPlayerForInput(player):
        if player == Players.Player_1:
            player_input = input(PROMPT_PLAYER_1)
        else:
            player_input = input(PROMPT_PLAYER_2)
        return player_input

    @staticmethod
    def PromptPlayerForOpponent():
        enemy_choice = input(PROMPT_HUMAN_AI)
        while (enemy_choice != OpponentTypes.Human) & (enemy_choice != OpponentTypes.AI):
            print(ERROR_INVALID_INPUT)
            enemy_choice = input(PROMPT_HUMAN_AI)
        else:
            return enemy_choice

    @staticmethod
    def ConvertRowLetterToRowNumber(player_input):
        converted_player_input = []
        try:
            converted_player_input = str(RowConverterDictionary[player_input[0]]) + player_input[1]
        except:
            converted_player_input = []
        finally:
            return converted_player_input


class Game:
    def __init__(self):
        self.game_board = GameBoard()
        self.current_player = Players.Player_1
        self.game_running = False
        self.player_input = PlayerInput()
        self.OpponentType = ""
        self.valid_move_possible = True

    def RotatePlayer(self):
        if self.current_player == Players.Player_1:
            self.current_player = Players.Player_2
        else:
            self.current_player = Players.Player_1

    def StartGame(self):
        if not self.game_running:
            self.game_running = True
            self.OpponentType = self.player_input.PromptPlayerForOpponent()
            self.valid_move_possible = True

            # Main Game Loop
            while self.game_running:
                self.game_board.PrintBoard()
                was_previous_turn_possible = self.valid_move_possible
                if self.game_board.IsBoardFull():
                    self.StopGame()
                self.valid_move_possible = self.game_board.IsValidMovePossible(self.current_player)
                if (self.current_player == Players.Player_2) & (self.OpponentType == OpponentTypes.AI):
                    ArtificialIntelligence.ProcessAIInput(self.game_board, self.valid_move_possible,
                                                          self.current_player)
                else:
                    self.player_input.PromptAndProcessPlayerInput(self.current_player, self.game_board,
                                                                  self.valid_move_possible)
                if (not self.valid_move_possible) & (not was_previous_turn_possible):
                    self.StopGame()
                self.RotatePlayer()
        else:
            print("Error: Game already running")

    def StopGame(self):
        if self.game_running:
            self.game_running = False
            self.game_board.PrintStats()
            victor = self.game_board.GetVictor()
            if victor == 1:
                exit(1)
            elif victor == 2:
                exit(2)
            else:
                exit(3)
        else:
            print("Error: Game is currently not running")


def main():
    print('\x1b[0;30;41m' + "Welcome to othello by Manuel Sammer" + '\x1b[0m')
    current_game = Game()
    current_game.StartGame()


if __name__ == "__main__":
    main()
