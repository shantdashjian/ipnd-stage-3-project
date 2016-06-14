# Concept: Separatin of concerns
import media
import fresh_tomatoes

# Concept: Creating an instance of a class
# Concept: Sending arguments to the class __init__ method
casino_royale = media.Movie("Casino Royale",
                            "James Bond must win a grand poker game with $10 million a piece.", "https://upload.wikimedia.org/wikipedia/en/1/15/Casino_Royale_2_-_UK_cinema_poster.jpg", "https://youtu.be/xK7PbujRUOk")  # noqa

quantum_of_solace = media.Movie("Quantum of Solace",
                        "Bond interrogates Mr. White regarding his organization, Quantum. Through a chase that starts in South America and ends in Russia, Bond finds Vesper's former lover, a member of Quantum who seduces women with valuable connections.", "https://upload.wikimedia.org/wikipedia/en/2/2d/Quantum_of_Solace_-_UK_cinema_poster.jpg",
                        "https://youtu.be/kasyk4rtQ2U")  # noqa

skyfall = media.Movie("Skyfall",
                        "An ex-MI6 agent driven by revenge plans to kill M. Bond takes her to Skyfall, an old mansion where he grew up, to protect her.", "https://upload.wikimedia.org/wikipedia/en/a/a7/Skyfall_poster.jpg",
                        "https://youtu.be/6kw1UVovByw")  # noqa

spectre = media.Movie("Spectre",
                        "After M's death, James Bond is on a mission to uncover and destroy a global criminal organization that is trying to control the world.", "https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg",
                        "https://youtu.be/z4UDNzXD3qA")  # noqa

# Concept: Creating a list of items
movies = [casino_royale, quantum_of_solace, skyfall, spectre]

# Concept: Calling a method from code imported and sending a list of items its way as argument
fresh_tomatoes.open_movies_page(movies)
