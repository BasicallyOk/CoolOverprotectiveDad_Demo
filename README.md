# Cool Overprotective Dad
A fun visual novel about a cool dad, who happens to be quite overprotective. Only chapter 1 is currently available, but expect more to come as our Writer pumps out the rest. Uses Lifelike's Sequence Tree system to determine how the story progresses given the player's response.

Join us at https://discord.gg/GPrBT9RzEn to give us feedback, get help making your own game with Lifelike Toolkit, or see our progress on the Lifelike Toolkit and Cool Overprotective Dad.

The visual aspect of the visual novel does not have much going for it right now as we are focusing on developing Lifelike. So if you want to take over the demo's development and work on finishing the game's frontend, contact me at dangkhoa81122@gmail.com, on Discord at BasicallyOK#3279 or join the Discord server.

Currently, we are making use of a simple sentiment analysis model. Unfortunately, this model does not recognize contextual clues, but we plan to fix this with a Lifelike feature that's coming later down the line. For now, make sure that **your sentiment can be understood when taken out of context**.

# Play Demo
Since I am still figuring out how to best deploy this, you can run the game locally by following a few steps on your terminal. All you need is Python, PIP and npm on your system.
1. Clone this repository to your computer using `git clone` with the `--recursive` flag at the end. You should see the lifelike folder with everything inside
2. Navigate to the root folder of the repository
3. Run `pip install -r requirements.txt`. This may take a minute
4. Navigate to the `client` folder in root
5. Run `npm install`. This may take a minute
6. Run `npm start`. This will start the client in the browser, but it won't be playable just yet. We're close
7. In a different terminal, navigate to the `server` folder in root
8. Run `flask --app server run`. This may take a second, but once it's done, the game will be playable on the website that the browser open up. The default should be http://localhost:3000 but this may depend on the system. You can look at the terminal where you have the client running to see the actually link to use.

# Credits
**Director and Programmer**: Khoa Nguyen\
**Writer and Creative Director**: Connor Killingbeck