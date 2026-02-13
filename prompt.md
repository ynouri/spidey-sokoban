# Context
- We want to create a game for a 4-year-old kid, and it should be a Sokoban game on the theme of Spidey and his friends. 
- We wanna use Spidey images to make the game on the Spider-Man theme. It should be nice and look like a comic. The images should be simple. 
- We want the tiles to be pretty large.
- We want the ability to go back if one makes a wrong step.
- Ideally, we should find the levels from maybe an open source of Goban on the internet, or maybe we can generate a few levels for a start.
- We'll want to start with a very simple version and then we'll iterate. 
- We want use pygame
- Name of the game: "Spidey Sokoban"

# Notes
- The conda environment to work in is called "pygame"
- You have a git repo called "spidey-sokoban", but it has no commits yet. Work on the branch main and commit every time you complete a step

# Iteration A: Design and Plan
As the first iteration of this project, we want to work with you on the design of the game, and you should guide us through the different design decisions that we need to make to design this game. Secondly, once this is done, we should work on the plan, and we want to do something that goes step-by-step and that gives us fast results. Then, let us iterate using quick iterations. 

# Iteration B: Add Spidey Sprites
I will give you images in the assets folder. Those are images from Spidey.
We want to make the window larger, and we want to make sure the main character reflects the Spidey image. 
If you need to make changes on the image, feel free to do so by downloading any tools you might need to modify the image. 
Okay, if you look in the assets folder, there is an image called spin.jpeg. 

# Iteration C: More Levels
I want you to add more levels. 
When the game starts, the player should be able to start three levels of difficulty:
1. Easy
2. Medium
3. Hard
Some levels should have blocks within the field such that you cannot move everywhere to make things more complicated. 
I want you to come up with a system where the level maps can be saved to different files and you can organize them across the levels of difficulty and the level numbers. Come up with that system so you don't hard-code everything in the main module. 
I also want you to write unit tests. I want you to verify that all the levels can be completed successfully. 