import fresh_tomatoes #import must be in the same folder as .py file
import media

#movie titles, stroyline, poster and trailer
baseketball = media.Movie("Baseketball",
                          "A comedy about 2 friends who create their own national sport",
                          "https://en.wikipedia.org/wiki/File:Baseketball.jpg#/media/File:Baseketball.jpg"
                          "https://www.youtube.com/watch?v=GHQrDlhnl_I")

dont_be_a_menace = media.Movie("Don't Be a Menace to South Central While Drinking Your Juice in the Hood",
                               "Parody movie about life in the hood"
                               "https://en.wikipedia.org/wiki/File:Dontbeamenace.jpg#/media/File:Dontbeamenace.jpg"
                               "https://www.youtube.com/watch?v=JAAhQwcJ20U"

the_departed = media.Movie("The Departed",
                           "Gangster film about an undercover agent and a mob boss",
                           "https://en.wikipedia.org/wiki/File:Departed234.jpg#/media/File:Departed234.jpg"
                           "https://www.youtube.com/watch?v=SGWvwjZ0eDc"

chopper = media.Movie("Chopper",
                      "Notorious Australian criminal Mark 'Chopper' Reids' biography"
                      "https://en.wikipedia.org/wiki/File:Choppermovie.jpg#/media/File:Choppermovie.jpg"
                      "https://www.youtube.com/watch?v=rnLlHDpRvxQ"

gladiator = media.Movie("Gladiator",
                        "Roman gladiator who fights in the Colloseum",
                        "https://en.wikipedia.org/wiki/File:Gladiator_ver1.jpg#/media/File:Gladiator_ver1.jpg"
                        "https://www.youtube.com/watch?v=ol67qo3WhJk"

he_got_game = media.Movie("He Got Game",
                          "Star basketball player who is about to get drafted and his estranged father",
                          "https://en.wikipedia.org/wiki/File:He_got_game_poster.jpg#/media/File:He_got_game_poster.jpg"
                          "https://www.youtube.com/watch?v=yIhthvNiPR4"

#list of the movies                          
movies = [baseketball, dont_be_a_menace, the_departed, chopper, gladiator, he_got_game]

fresh_tomatoes.open_movies_page(movies)
