# Position Key: Relax your fingers
PositionKey is a multi-platform python package for mapping key strokes to mouse clicks.

## Installation

### Install with pip
PositionKey is available on PyPI as ```positionkey```. 
1. Install PositionKey:
```
pip install positionkey
```
For positionkey for function properly, some dependencies will automatically be installed.

### Local Installation
PositionKey is compatible with Linux and Windows systems. To install a local version:

1. Install dependencies:
```
pip install -r requirements.txt
```
2. Run installation command from the root directory:
```
python setup.py --install
```

## Why use PositionKey?

## Usage Demo

## Licence
[MIT Licence](https://github.com/niteshctrl/positionkey/blob/main/LICENSE)

## Mouse clicks(GUI) mapped to keypresses

Positionkey is a python library for mapping keystrokes to mouse clicks. Currently, there are four keys mapped: **D, V, L and C** which stands for words Dismiss, Verify, Long and Cancel respectively. These four keystrokes can store and hit four positions on the GUI screen. 
Usage: Say if we need to alternately click on two buttons on the computer's screen, just map the click to any two of the mentioned keys and hit the keys alternately on the keyboard as per need.

We can record the pixel positions of keys D, V, L, C via the numeric keys 1, 2, 3, 4 respectively. 
The current position of the mouse pointer will be recorded whenever the above numeric keys are pressed while the script is running. 

The four (x, y) positions will be stored in a CSV file named 'click_positions.csv' in the current directory for resuming the same positions on succesive runs.
The four positions defaults to (700, 0) pixel of the screen where 700 is the X-coordinate and 0 is the Y-coordinate.

There is a partition function which will virtually divide the computer screen into two halves: Left and Right. The script will only run when the mouse pointer is on the left of the partition line(vertical) while won't work if the mouse pointer is on the right side of the partition line(Vertical). The partition line can be recorded by hitting the key "P" on the keyboard.
