# keyboard-vs-mouse
Keyboard vs mouse is a game where you compete for glorious points by pressing keys.

This is the first game I have built in a really long time. I hope you enjoy.

## Get started
1. Create an account on the server
2. Download this client and install the necessary dependencies
3. Configure the client
4. Play the game!
5. Profit!

## Installation
Simply clone this repository
```
git clone https://github.com/ooreilly/keyboard-vs-mouse.git 
```
And open the directory.

You need install the following dependencies (if they are not already installed):
```
pip install pynput
pip install keyboard
pip install requests
```
* The package [pynput](https://github.com/moses-palmer/pynput) is used for listening to the mouse.
* The package [keyboard](https://github.com/boppreh/keyboard) is used for listening to the keyboard.
* The package [requests](http://docs.python-requests.org/en/master/) is used for communicating with the server.

## Configuration
Before you can being playing this **amazing** game, you must first configure the client. Open up `config.py` and follow the instructions.

## Running
To run this game, you need to have admin access. Launch by typing:
```
$ sudo python keyboardvsmouse.py
```

## How the game works
You get points for pressing keys on your keyboard. Each key press is worth one point. You lose points by pressing mouse buttons or moving the mouse. The amount of points you lose depend on how experienced you are and how long you have been playing for. Good luck!
The client application will work as long as you are connected to the server and let it run. You can focus on your regular tasks while you let it run it the background. 

### Privacy
This game will only upload the number of key and button presses, mouse motions, and the time you have played for. The actual activities you do are not recorded. Check the source of `keyboardvsmouse.py` to confirm for yourself.  

### Cheating
It is currently super-easy to cheat so please don't :). 
