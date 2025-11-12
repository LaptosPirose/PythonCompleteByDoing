"""Simple in-memory movies store CLI.

This module provides a minimal command-line interface (CLI) to add,
list, and find movies stored in an in-memory list. It's intended as a
small learning example and does not persist data between runs.

Usage:
    Run the module and follow the prompts to add/list/find movies.
"""

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movie, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    """Prompt the user for movie details and add it to the store.

    The function requests the movie title, director and release year
    from standard input and appends a dictionary with those values to
    the module-level ``movies`` list.

    Side effects:
        Modifies the global ``movies`` list by appending a new dict.

    Returns:
        None
    """

    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show_movies():
    """Print all movies currently stored.

    Iterates over the global ``movies`` list and prints each movie using
    :func:`print_movie`.

    Returns:
        None
    """

    print("This is your movies list:")
    for movie in movies:
        print_movie(movie)


def find_movie():
    """Prompt for a title and print matching movies.

    The function asks the user for a movie title and prints any movie
    from ``movies`` whose ``title`` field exactly matches the input.

    Returns:
        None
    """

    search_title = input("Enter the movie title you're looking for: ")
    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)


def print_movie(movie):
    """Print a single movie dictionary in a readable format.

    Args:
        movie (dict): A dictionary containing at least the keys
            ``'title'``, ``'director'`` and ``'year'``.

    Returns:
        None
    """

    print(
        f"Title: {movie['title']}, Director: {movie['director']}, Release Year: {movie['year']}")


user_options = {
    'a': add_movie,
    'l': show_movies,
    'f': find_movie,
}


def menu():
    """Interactive menu loop for the movies CLI.

    The function presents the user with the options defined in
    ``MENU_PROMPT`` and dispatches to the appropriate handler in
    ``user_options``. The loop exits when the user enters ``'q'``.

    Returns:
        None
    """

    selection = input(MENU_PROMPT).lower()
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()
