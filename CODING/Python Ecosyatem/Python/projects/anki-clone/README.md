# What is the Project?
This project is a **vocab builder / language learning app** that uses **spaced repetition** to help users learn and practice new words effectively.

---
# Instructions

* Take definitions.json, read it in as data and use a spaced repetition algorithm to create a long list where each word is encountered less and less often thus increasing the spacing between encounters as we strengthen our knowledge of word.

  * [ ] read in the definitions file and process it.
  * [ ] create a complex object that keeps track of a whole lot of properties about the word, or attributes / therefore we need to define a class for this object.
  * [ ] we are going to need to define a bunch of methods (functions specific to a class that are kind of like actions such as a method we can use to automatically handle a word encounter)
  * [ ] instantiate this class/object for every word.
  * [ ] we can create the spaced repetition algorithm that we will use to create this long list that cleverly introduces new words and tests old words at the appropriate intervals.
  * [ ] save this long list of all our words to a csv file that can later be read by our game.

---
* Create a game, where a user has to get as many items in the list (i.e. i answered them correctly), and when they ultimately fail, then they get a high score and have to start again (which also forces them to continue practicing).

  * [ ] to create the files to read both the long list of spaced-repeated words so that we can loop over them and test the user continuously until they fail, at which point we give them a score, and also the word definitions so that we may show a user a word definition if it's their first time encountering the word.
  * [ ] define a continuous while loop, that tests the user on each word in the list, one after another in the provided order, and will only exit when each word has been mastered, or the user makes a mistake.
  * [ ] print the new high score when they fail or win, and also a command to start again.

---
# Pseudo-Code
1. Apply the optimization procedures to the smallest possible items.
2. Differentiate between the items on the base of their different difficulty.


