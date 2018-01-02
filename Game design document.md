# TextRPG

## Game loop overview
In the game, the player takes the role of a lonely adventurer, spelunking in search for treasures. He needs to explore dangerous environs, overcome deadly monsters and traps through battle, trickery and magic.

The main game loop is  **Exploration**, in which the character walks through a series of *rooms* that have various content. In this mode, a description of all content is provided:
* The room itself
* Visible *exits*
* *Objects* with which the character can interact or pick up
* *Creatures* which are visible

The character can then choose which of the present areas he wants to examine closer. Depending on the type of feature, different options/sub-screens will be available. In addition to that, the character will always have the opportunity to examine his inventory, spells, and status.

For this, I will create a list of potential options, like this:

> <Player>, what do you want to do?

> Go somewhere else - (1) Northern door, (2) Western passage

> Examine - (3) Altar, (4) Broken remains, (5) Wooden chest

> Interact - (6) Goblin priest, 3 Goblin warriors

Based on the choice, the game will switch into another game mode. In each of the game modes, the option *0* means "go back to the previous screen"

## Visible exits
The character will be asked which exits he wants to take. If it is open, he will move directly into the next area. If the exit for some reason is not accessible, the character will be asked to open, force open, or lockpick the exit.

## Objects
The game displays a more detailed description of the object and potential choices for the player. Depending on the object, the player can
* Take
* Manipulate

the object or go back to the room.

## Creatures
The game displays a more detailed description of the creature and potential choices. Those choices are:
* Talk
* Attack
* Steal

Talking to a creature might lead to a *Dialogue* game state, attacking a creature will lead to the *Battle* game mode.
