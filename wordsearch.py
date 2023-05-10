def wordsearch(puzzle: list, wordlist: list) -> None:
    positions = []
    for word in wordlist:
        positions.append(get_positions(puzzle, word))
    coloured_display(puzzle, positions)


def valid_puzzle(puzzle: list) -> bool:
    for i in range(len(puzzle)):
        if type(puzzle[i]) != str:
            return False
        elif len(puzzle[i]) != len(puzzle[0]):
            return False
    return True


def valid_wordlist(wordlist: list) -> bool:
    if type(wordlist) != list:
        return False
    for i in range(len(wordlist)):
        if type(wordlist[i]) != str:
            return False
    return True


def basic_display(grid: list) -> None:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=' ')
        print()


def coloured_display(grid: list, positions: list) -> None:
    print("Before", positions)
    positions = [item for sublist in positions for item in sublist]
    print("After", positions)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in positions:
                print("\033[42m", grid[i][j], "\033[0m", end=' ')
            else:
                print(grid[i][j], end=' ')
        print()


def get_positions(grid: list, word: str) -> list:
    positions = []
    word = word.upper()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Get Position of Each Letter in the Word
            if grid[i][j] == word[0]:
                # check right direction
                if check_right(grid, i, j, word):
                    for k in range(len(word)):
                        positions.append((i, j + k))
                    return positions
                #  check down direction
                elif check_down(grid, i, j, word):
                    for k in range(len(word)):
                        positions.append((i + k, j))
                    return positions
                #  check left direction
                elif check_left(grid, i, j, word):
                    for k in range(len(word)):
                        positions.append((i, j - k))
                    return positions
                #   check up direction
                elif check_up(grid, i, j, word):
                    for k in range(len(word)):
                        positions.append((i - k, j))
                    return positions
                #  check right down direction
                elif check_right_down(grid, i, j, word):
                    for k in range(len(word)):
                        positions.append((i + k, j + k))
                    return positions
                #  check left down direction
                elif check_right_up(grid, i, j, word):
                    for k in range(len(word)):
                        positions.append((i - k, j + k))
                    return positions
                # check left up direction
                elif check_left_down(grid, i, j, word):
                    for k in range(len(word)):
                        positions.append((i + k, j - k))
                    return positions
                #  check left up direction
                elif check_left_up(grid, i, j, word):
                    for k in range(len(word)):
                        positions.append((i - k, j - k))
                    return positions
    if positions:
        print("Word found:", word)
        return positions
    else:
        return None


def check_right(grid: list, i: int, j: int, word: str) -> bool:
    if j + len(word) > len(grid[i]):
        return False
    for k in range(len(word)):
        if grid[i][j + k] != word[k]:
            return False
    return True


def check_down(grid: list, i: int, j: int, word: str) -> bool:
    if i + len(word) > len(grid):
        return False
    for k in range(len(word)):
        if grid[i + k][j] != word[k]:
            return False
    return True


def check_left(grid: list, i: int, j: int, word: str) -> bool:
    if j - len(word) < -1:
        return False
    for k in range(len(word)):
        if grid[i][j - k] != word[k]:
            return False
    return True


def check_up(grid: list, i: int, j: int, word: str) -> bool:
    if i - len(word) < -1:
        return False
    for k in range(len(word)):
        if grid[i - k][j] != word[k]:
            return False
    return True


def check_right_down(grid: list, i: int, j: int, word: str) -> bool:
    if i + len(word) > len(grid) or j + len(word) > len(grid[i]):
        return False
    for k in range(len(word)):
        if grid[i + k][j + k] != word[k]:
            return False
    return True


def check_right_up(grid: list, i: int, j: int, word: str) -> bool:
    if i - len(word) < -1 or j + len(word) > len(grid[i]):
        return False
    for k in range(len(word)):
        if grid[i - k][j + k] != word[k]:
            return False
    return True


def check_left_down(grid: list, i: int, j: int, word: str) -> bool:
    if i + len(word) > len(grid) or j - len(word) < -1:
        return False
    for k in range(len(word)):
        if grid[i + k][j - k] != word[k]:
            return False
    return True


def check_left_up(grid: list, i: int, j: int, word: str) -> bool:
    if i - len(word) < -1 or j - len(word) < -1:
        return False
    for k in range(len(word)):
        if grid[i - k][j - k] != word[k]:
            return False
    return True


def test_valid_wordlist():
    """
    Test function valid_wordlist()
    """
    good_wordlist = ["scalar", "tray", "blew", "sevruc", "testing"]
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    bad_wordlist2 = ["scalar", "tray", "blew", "sevruc", 59]

    print("wordlist is", valid_wordlist(good_wordlist))
    print("wordlist is", valid_wordlist(good_wordlist2))
    print("wordlist is", valid_wordlist(bad_wordlist2))


def test_valid_puzzle():
    good_puzzle = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle1 = ['RUNAROUNDDL', 'EDCITOAHC', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle2 = ['RUNAROUNDDL', ['EDCITOAHCYV'], ('ZYUWSWEDZYA'),
                   'AKOTCONVOYV', 'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL',
                   'ISTREWZLCGY', 'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    print("puzzle is", valid_puzzle(good_puzzle))
    print("puzzle is", valid_puzzle(bad_puzzle1))
    print("puzzle is", valid_puzzle(bad_puzzle2))


def test_basic_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    basic_display(puzzle1)
    basic_display([['a', 'b', 'c', 'd', 'e'], ['h', 'l', 'j', 'k', 'l']])


def test_get_positions():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    get_positions(puzzle1, "TESTING")
    print(get_positions(puzzle1, "TRAY"))


def test_coloured_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    final_list = []
    for word in good_wordlist2:
        temp = get_positions(puzzle1, word)
        if temp is not None:
            final_list.append(temp)
    coloured_display(puzzle1, final_list)


def test_wordsearch():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc", ]
    wordsearch(puzzle1, good_wordlist2)


if __name__ == "__main__":
    # # uncomment the test function individually
    # # basic solution
    # test_valid_puzzle()
    # test_valid_wordlist()
    # test_basic_display()

    # # full solution
    # test_coloured_display()
    # test_get_positions()
    test_wordsearch()
