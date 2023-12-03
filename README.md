# generator
### Description of the program's purpose (why does it exist and/or who is it for?)
#### It exists because we all know the common issue of taking ages to choose a song or movie based on your mood. That is why we created this code, which can be used by most people ages 10+.
### Summary of the program's functionality (what does it do?)
#### It takes a user input based on the question “Song or Movie '', and then another input that answers the style of your music/genre of movie.  After this, you get another question indicating mood then the code then runs through the dictionaries and filters by that mood and genre and gives you a song or movie that we put in and pre-categorized. 
### A description, with code segments, of a "breakthrough moment" in which you solved a particularly difficult problem, learned to do something new, or independently overcame being stuck:
#### Our breakthrough moment was when we were able to filter down the movie code  and filter songs as it was tough and it took us the most time. This was a group challenge that we all worked on overcoming.
#### filtered_songs = [song for song in longarrays if song["genre"] == user_genre] 
#### This code takes a song from the longarrays and defines it as a song that fits the genre that is the same as the user genre/input. It stores it as filtered_songs.
