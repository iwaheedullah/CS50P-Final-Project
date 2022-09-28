# import libraries and other files.
import random
import re
import requests
from prettytable import PrettyTable
from arts import logo, hanged

# Global Lists.,
names = []
regions = []
capitals = []
continents = []

# ENDPOINT of an API.
ENDPOINT = "https://restcountries.com/v3.1/all"


def main():
    # Make object of PrettyTable.
    x = PrettyTable()

    # print the logo.
    print(logo)

    # load game for first turn.
    play_game(x)


def play_game(x):
    # Declare list and variables.
    typed_characters = []
    out_of_lives = False
    lives = 6

    # Fetch data from API.
    fetch_data(ENDPOINT)

    # Get a country from names list.
    country = random.choice(names)

    # Get index of country in list.
    index = names.index(country)

    # Output Extra details for guessing.
    x.clear_rows()
    print("|+ ----- Details about the Country -----+|")
    x.field_names = ["Continents", "Regions", "Capitals"]
    x.add_row([continents[index], regions[index], capitals[index]])
    print(x)

    # Get length of country name.
    length = get_length(country)

    # Get blanks dashes.
    blanks = print_blanks(length)

    # Repeat either out_of_lives become True or lives reached to 0.
    while not out_of_lives:

        # print the dashes.
        for _ in blanks:
            print(_, end=" ")
        # print extra line at the end.
        print()

        # When guess is correct.
        if "_" not in blanks:

            print("\n+-----------+------+------------+------+")
            print(f"| CONGRATULATION! YOU GUSSED CORRECTLY |")
            print("+-----------+------+------------+-------+\n")
            x.clear_rows()
            typed_characters
            # Ask question.
            answer = input("\nDo you wanna play another guess? Type yes/no: ").lower()
            # if user wanna play again.
            if answer == "yes":
                # load game again.
                play_game(x)

            # if user don't wanna play, quit game.
            break

        # Prompt the user for guess.
        guess = input("Guess a letter: ")

        # if user type duplicate character.
        if guess in typed_characters:

            print("\n+------+------+------+------+")
            print(f"| This {guess} already typed. |")
            print("+-----+------+--------+--------+\n")


        # if character is not typed yet.
        else:
            # add in typed_characters list.
            typed_characters.append(guess)

            # if guess in country name.
            if guess in country:
                # find occurrence of single character in country name.
                results = [_.start() for _ in re.finditer(guess, country)]
                # replace character with dashes.
                for i in results:
                    blanks[int(i)] = guess
            # if guess doesn't in country name.
            else:
                # decrement lives by 1.
                lives -= 1

        # When lives reached to 0, Quit Game and print hanged ascii arts.
        if lives == 0:
            out_of_lives = True
            print(hanged)


# Return dashes
def print_blanks(length):
    dashes = ["_" for _ in range(length)]
    return dashes


def fetch_data(ENDPOINT):
    # Catch exception to HTTPErrors.
    try:
        # Get response from API.
        response = requests.get(ENDPOINT)

        # Get status code
        response.raise_for_status()

    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    # Convert to JSON format.
    content = response.json()

    # Get only 100 countries list.
    for row in content[:100]:
        names.append(row['name']['common'].lower())
        continents.append(row['continents'][0])
        capitals.append(row['capital'][0])
        regions.append(row['region'])


# Get length of country name.
def get_length(country):
    return len(country)


if __name__ == "__main__":
    main()
