# The idea of this project is to analyze a txt file with the lyrics of a song and
# create a ranking of the 10 most repeated words in the song

#---------- Thought Process ---------- #
#DONE: Read TXT
#DONE: Separate words
#DONE: Count how many times each word repeats
#DONE: Rank 'em!
#DONE: Show it on screen
#DONE: Ignore commas

import pandas as pd

words = {}
with open("music.txt", "r") as file:
    for line in file:
        for word in line.split():
            word = word.lower().strip(",.!?()[]{}\"'")
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
    ranking = pd.DataFrame(list(words.items()), columns=['word', 'count']).sort_values(by='count', ascending=False).head(10)
    print(ranking.to_string(index=False)) #hide index because since it's ordered by value the indexes are messed up
file.close()
