# Bug 1 : Path normalization fails for Unix absolute paths.
from game_ratings_analyzer import normalize_path
def test_bug1_path_normalization():
    fileName = "/home/user/\\data\\game_ratings.csv"
    assert "/home/user/data/game_ratings.csv" == normalize_path(fileName)



# Bug 2: is_valid_rating fails with string input.
from game_ratings_analyzer import is_valid_rating
def test_bug2_rating_validity():
    assert is_valid_rating("9")



# Bug 3: File open without try/except.
from game_ratings_analyzer import read_ratings
def test_bug3_file_not_exist():
    read_ratings("not_existing_file.csv")



# Bug 4: Non-numeric rating parsing.
from game_ratings_analyzer import read_ratings
from tempfile import NamedTemporaryFile
def test_bug4_nan_rating():
    csv_data = '''title,genre,rating,comments
Fake Game,RPG,not_a_number'''
    tmp = NamedTemporaryFile()
    with open(tmp.name, 'w') as f:
        f.write(csv_data)
    read_ratings(tmp.name)



# Bug 5: Accepting empty titles.
from game_ratings_analyzer import read_ratings
from tempfile import NamedTemporaryFile
def test_bug5_empty_title():
    csv_data = '''title,genre,rating,comments
,RPG,8'''
    tmp = NamedTemporaryFile()
    with open(tmp.name, 'w') as f:
        f.write(csv_data)
    # No empty dictionary keys should be allowed.
    assert len(read_ratings(tmp.name)) == 0



# Bug 6: Divide by zero for empty score list.
from game_ratings_analyzer import generate_report
def test_bug6_div_zero():
    ratings = {"Empty Game": []}
    # Div by zero should be avoided.
    generate_report(ratings, 1)


# Bug 7: IndexError when top_n > len(ratings)
from game_ratings_analyzer import generate_report
def test_bug7_less_ratings():
    ratings = {
        "Game A": [10],
        "Game B": [9]
    }

    # No IndexError should be raised.
    generate_report(ratings, 5)



# Bug 8: Wrong tie ditection.
from game_ratings_analyzer import is_tie
def test_bug8_wrong_tie_detection():
    ratings = [
        ("Game A", 9),
        ("Game B", 8),
        ("Game C", 9)
    ]

    assert is_tie(ratings) == False



# Bug 9: Fixed top_n too high
from game_ratings_analyzer import generate_report
def test_bug9_top_n_too_high():
    ratings = {
        "Game A": [10]
    }
    
    # No IndexError should be raised
    generate_report(ratings, 10)
