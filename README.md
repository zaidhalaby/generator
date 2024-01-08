# Song Generator V1
### Your group's development plan which should include milestones, individual tasks, and who is responsible for those tasks:
#### Our group split up work among us three. I worked on getting an input and creating the if statements with Hamza. Hamza created the formatting for the outputs and all of the dictionaries while Jad worked on getting all of the information for the dictionaries and assisted me and Hamza as well. Our milestone is now being able to get multiple songs and a working code but our final goal is a GUI and the ability to have one song recommended rather than all the applicable songs. Moving forward we will decide our responsibilities.
### Video of code running:
(https://drive.google.com/file/d/1tzjCQi8IO6O1uWxGVk8F38GpP3nQ_rJF/view?usp=sharing) 
### Description of the program's purpose (why does it exist and/or who is it for?)
#### It exists because we all know the common issue of taking ages to choose a song or movie based on your mood. That is why we created this code, which can be used by most people ages 10+.
### Summary of the program's functionality (what does it do?)
#### It takes a user input based on the question “Song or Movie '', and then another input that answers the style of your music/genre of movie.  After this, you get another question indicating mood then the code then runs through the dictionaries and filters by that mood and genre and gives you a song or movie that we put in and pre-categorized. 
### A description, with code segments, of a "breakthrough moment" in which you solved a particularly difficult problem, learned to do something new, or independently overcame being stuck:
#### Our breakthrough moment was when we were able to filter down the movie code  and filter songs as it was tough and it took us the most time. This was a group challenge that we all worked on overcoming.
#### filtered_songs = [song for song in longarrays if song["genre"] == user_genre] 
#### This code takes a song from the longarrays and defines it as a song that fits the genre that is the same as the user genre/input. It stores it as filtered_songs.

# Song Generator V2
### What does it do/who is it for?
#### Our updated code has the same main function as the original version- to choose a song or movie based on your mood or the genre you like. This is because a common issue we all face is wasting time trying to find something to watch or listen to. Our new code makes this even more efficient as the new implementation of a login/username and password allows the user to view their previous suggestions too.
###  A description, with code segments, of a "breakthrough moment" in which you solved a particularly difficult problem, learned to do something new or independently overcame being stuck
#### One section that we got stuck on and had a breakthrough moment for was trying to add a login. This is the code that we used: 
#### def SorL():
####  while True:
####      SorL = input("Sign Up or Log in? (respond with S or L) ").capitalize()
####      if SorL == "S" or SorL == "L":
####          return SorL
####          break  # This break statement is not needed and can be removed
####      while SorL != "S" and SorL != "L":
####          SorL = input("Sign Up or Log in? (cmon bro i said respond with S or L not that baloney) ").capitalize()
####          if SorL == "S" or SorL == "L":
####              return SorL
####              # The break statement is not needed here either

#### def log():
####  print("LOG IN")
####  username = input("Username: ").capitalize()
####  password = input("Password: ")
####  file_path = 'users.txt'
####  with open(file_path, 'r') as file:
####      for line in file:
####          if f"Username: {username}, Password: {password}" in line:
####              print(f"Welcome {username}!")
####              return username
####      else:
####          choice = "hello"
####          while choice not in ["L", "I"]:
####              choice = input("Your password or username is wrong. Input 'L' to try again or 'I' to start over the function ").capitalize()
####              if choice == "I":
####                  return identifyuser()
####              elif choice == "L":
####                  return log()


#### This code uses numerous lists, if statements and other components of code to run. It begins by asking the user whether they want to sign up or log in and using an if-else statement to work based on that input. It then stores all of the users and makes sure that the computer identifies the user when they log in, saving and showing their previous suggestions. This was a breakthrough moment as it allowed our code to be enhanced and have even more meaning in it. This code has the goal of authorizing the user and utilizing appending the text file by adding the user name and password to a text file and then prompting the user to input the same username and password in the login feature. This allows the user to conserve the user history and not get any outputs from other users. The big problem with this user identification was the storage of the information which was combatted with the usage of text lists which allowed the function to work sufficiently.

### Video of code running:
(https://drive.google.com/file/d/1FZSs_8fRkCIrFXtMCEv0C03yJ_ydGidE/view)
