# Guess the Country
## Video Demo: <https://www.youtube.com/watch?v=_X9UmmSwqA0&t=35s>
## Description:
Guess the Country is a sort of fun game project, in this game a user has to guess a country word by word unless the user guessed all characters in a country name or the user run out of lives.

### Let go in details how does the project work.
Intially, I got countries information form an
API (restcountries.com), and then stored that data in different lists. In addition to,the particular information that I got from an API are names, regions, continents and capitals of countries and save them in lists respectively.

Afterwards, with the help of random library I pick up a country name, and then I got index of
that country name in list, since all the lists are equal in length. So, with the help of that index I shown other information like continent, region and capital of that country for a user as hints which are gonna make it easy for a user to guess the country correctly.

Another custom function is going to get me length of country name, and with that length I am gonna
print as many dashes as length of country name.

The user has 6 lives in total, if the user guess incorrectly, hence, a live would be decremented.
Unfortunately, if the lives reaches to 0, so therefore, hanged ascii arts would be shown and exit.

On the other hand, if user guess correctly, dashes would be replaced with that character in appropiated indexes.
When the user guessed country name completely correct, a question would be asked, whether the user wants to play again.