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

game_field = [
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 2, 0, 0, 0],
  [0, 0, 0, 2, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
]


# A function to print boardData provided.
def printBoard(boardData):
  print("\n   ┌───┬───┬───┬───┬───┬───┬───┬───┐")

  row_keys = ["A", "B", "C", "D", "E", "F", "G", "H"]

  row_count = 0

  for row in boardData:
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
    if (row_count < len(boardData)):
      print("   ├───┼───┼───┼───┼───┼───┼───┼───┤")

  print("   └───┴───┴───┴───┴───┴───┴───┴───┘")
  print("     0   1   2   3   4   5   6   7  ")


def main():
  printBoard(game_field)
  print(ERROR_INVALID_INPUT)


if __name__ == "__main__":
  main()
