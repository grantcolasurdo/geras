# Geras
A Fantasy Age Management Tool

## Purpose
The idea behind this project is to provide a tool that can be used to track all the small details and interactions in a Fantasy Age roll playing game. Keeping track of a character's focuses, weapon groups, talents, abilities, items, health, calculated stats, etc.. is all a pain and the time spend managing all of these parameters is time spent not on the roll playing itself.
This project is still early Alpha.

## Long term Goals
I would like this program to be able to act as a tool for DM's to easily keep track of everyone's actions and stats by communicating with other instances over tcp/ip. It should be sufficiently advanced that it can handle combat interactions, store inventory and arbetrary manipulation of stats by the DM / player depending on a trust / strictness setting. This project should always be a tool though, and not take over every aspect of the roll playing
### Meta
Code is released under GPLv2 and can be found at https://github.com/grantcolasurdo/geras/

[link](https://github.com/grantcolasurdo/geras/ "Link")
## Structure

### Character
A character object acts as a root for a whole host of attributes, There are separate management interfaces for each of Abilities, Focuses, Taletns, Specializations, Arcana, Weapon Groups, Background information and Items. Items currently needs the most work and any input on how to manage items in the game would be appreciated.

### GUI
The gui currently is created using Tkinter. It's simple and I don't see that changing any time soon.

### Static Values
Object properties are saved in csv files and are accessed internally using the csv internal module.  


## TODO
### Character
* Figure out a way to track and manage equipment and inventory
* Make changes to a character's attributes transaction based
* Figure out a way to save and load a character
* Create a way to alter attributes on the fly

### Importing Data
* Figure out a way to make it modular, and allow outside data sources to be included easily

### Items
* The database needs a lot of work. Descriptions are missing, weights and sizes need to be figured out.
* Clothing in general is not robustly described, and an interface that allows for alterations would be nice

### GUI
* We need to be able to level up a character through the interface
* Input response dialog needs to be more descriptive
* A place for weapon group knowledge needs to be created
* A place for acquired focuses needs to be created
* A place for specialization information needs to be created
* A more spell management interface needs to be created
* A character's status (prone, stealth, standing, hexed, buffed) need to be displayed somewhere
* A character's worn items need to be displayed

### Networking
* Everything. We can worry about it when we have a functioning stand alone project
