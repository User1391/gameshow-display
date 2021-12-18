# The Hoo's Smarter Quiz Show Display
Using a question and answer list, creates a display to play a quiz game.

## Use
To use, make sure to put a questions.txt file into the same folder as the main.py file.

As for the layout of the questions.txt, this should be the order:
QUESTION; CATEGORY; ANSWER
QUESTION; CATEGORY; ANSWER
etc.

Ensure that there is always a space between the ; and the next part (except after the answer), and that each group is on a new line.
BE CAREFUL… If you misspell a category, then a new category will be created for the game, causing problems. 

Buttons:
Clear - Clears the text from the screen. Will clear a question if currently up, so use with caution.
Topic Button - There are many of these, one for each topic, regardless of if any questions remain from that topic. If there are questions remaining for the topic, this button will populate the text box with a random question from the ones remaining for the topic. Will overwrite a question previously on the screen, so use with caution.
Answer - For the last question existing on the screen (meaning it will still act if the topic was cleared), the answer will be displayed and the question (or another one, oddly) will be deleted, such that it cannot be randomly chosen again. Use with extreme caution.

