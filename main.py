# Random Song Generator in Python
import csv
import sys
import random

# Define a long array with each item having "name," "genre," and "mood"
longarrays  = [
    {"name": "Lose Yourself", "genre": "Rap", "mood": "Energetic"},
    {"name": "HUMBLE.", "genre": "Rap", "mood": "Energetic"},
    {"name": "Juicy", "genre": "Rap", "mood": "Energetic"},
    {"name": "Hotline Bling", "genre": "Rap", "mood": "Energetic"},
    {"name": "99 Problems", "genre": "Rap", "mood": "Energetic"},
    {"name": "N.Y. State of Mind", "genre": "Rap", "mood": "Energetic"},
    {"name": "Gold Digger", "genre": "Rap", "mood": "Energetic"},
    {"name": "Bodak Yellow", "genre": "Rap", "mood": "Energetic"},
    {"name": "SICKO MODE", "genre": "Rap", "mood": "Energetic"},
    {"name": "Hey Ya!", "genre": "Rap", "mood": "Energetic"},
    {"name": "Take Five by Dave Brubeck Quartet", "genre": "Jazz", "mood": "Relaxed"},
    {"name": "So What by Miles Davis", "genre": "Jazz", "mood": "Relaxed"},
    {"name": "My Favorite Things by John Coltrane", "genre": "Jazz", "mood": "Relaxed"},
    {"name": "Autumn Leaves by Nat King Cole", "genre": "Jazz", "mood": "Relaxed"},
    {"name": "A Love Supreme by John Coltrane", "genre": "Jazz", "mood": "Relaxed"},
    {"name": "Sing, Sing, Sing by Benny Goodman", "genre": "Jazz", "mood": "Relaxed"},
    {"name": "Freddie Freeloader by Miles Davis", "genre": "Jazz", "mood": "Relaxed"},
    {"name": "All Blues by Miles Davis", "genre": "Jazz", "mood": "Relaxed"},
    {"name": "Round Midnight by Thelonious Monk", "genre": "Jazz", "mood": "Relaxed"},
    {"name": "Cantaloupe Island by Herbie Hancock", "genre": "Jazz", "mood": "Relaxed"},
    {"name": "Hips Dont Lie by Shakira ft. Wyclef Jean", "genre": "Pop", "mood": "Happy"},
    {"name": "Hot N Cold by Katy Perry", "genre": "Pop", "mood": "Happy"},
    {"name": "Beautiful by Christina Aguilera", "genre": "Pop", "mood": "Happy"},
    {"name": "Hey Ya! by OutKast", "genre": "Pop", "mood": "Happy"},
    {"name": "I Gotta Feeling by The Black Eyed Peas", "genre": "Pop", "mood": "Happy"},
    {"name": "Since U Been Gone by Kelly Clarkson", "genre": "Pop", "mood": "Happy"},
    {"name": "Cry Me a River by Justin Timberlake", "genre": "Pop", "mood": "Happy"},
    {"name": "Complicated by Avril Lavigne", "genre": "Pop", "mood": "Happy"},
    {"name": "Livin on a Prayer by Bon Jovi", "genre": "Pop", "mood": "Happy"},
    {"name": "Umbrella by Rihanna ft. Jay-Z", "genre": "Pop", "mood": "Happy"}
]

longarrays2 = [
    {"name": "Airplane!", "genre": "Comedy"},
    {"name": "Ferris Bueller's Day Off", "genre": "Comedy"},
    {"name": "The Big Lebowski", "genre": "Comedy"},
    {"name": "Dumb and Dumber", "genre": "Comedy"},
    {"name": "Shaun of the Dead", "genre": "Comedy"},
    {"name": "Napoleon Dynamite", "genre": "Comedy"},
    {"name": "Ghostbusters", "genre": "Comedy"},
    {"name": "Groundhog Day", "genre": "Comedy"},
    {"name": "The Princess Bride", "genre": "Comedy"},
    {"name": "Super Troopers", "genre": "Comedy"},

    {"name": "Kill Bill: Volume 1", "genre": "Action"},
    {"name": "Gladiator", "genre": "Action"},
    {"name": "The Matrix", "genre": "Action"},
    {"name": "Lethal Weapon", "genre": "Action"},
    {"name": "Mission: Impossible - Fallout", "genre": "Action"},
    {"name": "The Bourne Identity", "genre": "Action"},
    {"name": "Speed", "genre": "Action"},
    {"name": "The Raid: Redemption", "genre": "Action"},
    {"name": "Terminator 2: Judgment Day", "genre": "Action"},
    {"name": "Mad Max: The Road Warrior", "genre": "Action"},

    {"name": "The Shawshank Redemption", "genre": "Drama"},
    {"name": "The Godfather", "genre": "Drama"},
    {"name": "Forrest Gump", "genre": "Drama"},
    {"name": "Schindler's List", "genre": "Drama"},
    {"name": "The Social Network", "genre": "Drama"},
    {"name": "12 Angry Men", "genre": "Drama"},
    {"name": "A Beautiful Mind", "genre": "Drama"},
    {"name": "The Silence of the Lambs", "genre": "Drama"},
    {"name": "The Pianist", "genre": "Drama" },
    {"name": "A Few Good Men", "genre": "Drama"},
]



      # Simulate loading a large music database
def user_inputsorm():
          user_input = input("Song or movie? Type S for song or M for movie: ")
          if user_input == "M":
              user_mgenre = input("Enter the genre you are interested in (Drama, Action, Comedy): ").capitalize()
             

              # Filter songs based on user's input
              filtered_movie = [movie for movie in longarrays2 if movie["genre"] == user_mgenre]
              
              random_movie =  random.choice(longarrays2)


              # Display the filtered songs
              if filtered_movie:
                  print(f"\nHere is a {user_mgenre}  movie:")
                  for movie in filtered_movie:
                      print(f"{movie['name']} - Mood: {movie['mood']}")
              else:
                  print(f"\nSorry, no {user_mgenre} movies found in our database.")
            
              random_genre = random.choice(longarrays)
              random_song =  random.choice(longarrays)
              return(f"Here's a movie for ya!: {random_movie['name']} (Genre: {random_movie['genre']})")
          elif user_input == "S":
              user_genre = input("Enter the genre you are interested in (Rap, Jazz, Pop): ").capitalize()
              user_mood = input("Enter the mood you are interested in (Relaxed, Energetic, Pop): ").capitalize()

              # Filter songs based on user's input
              filtered_songs = [song for song in longarrays if song["genre"] == user_genre]
              filtered_songs = [song for song in longarrays if song["mood"] == user_mood]


              # Display the filtered songs
              if filtered_songs:
                  print(f"\nHere is a {user_genre} {user_mood} song:")
                  for song in filtered_songs:
                      print(f"{song['name']} - Mood: {song['mood']}")
              else:
                  print(f"\nSorry, no {user_genre} songs found in the list.")
              random_genre = random.choice(longarrays)
              random_song =  random.choice(longarrays)
              return(f"Random Song: {random_song['name']} (Genre: {random_song['genre']})")
user_inputsorm()

  


