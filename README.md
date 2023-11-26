# AVD Taps

Easily configure keybinds to send tap inputs to an Android Virtual Device (AVD).

> [!NOTE]
> The script currently only works on macOS. Support for other operating systems
> may be added in the future.

## Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [Android SDK](https://developer.android.com/studio/releases/platform-tools) (for `adb`)

## Installation

**Clone the repository:**

```sh
git clone git@github.com:jozsefsallai/avd-taps.git
cd avd-taps
```

**Create a virtual environment:**

```sh
python3 -m venv .venv
source .venv/bin/activate
```

**Install the dependencies:**

```sh
pip install -r requirements.txt
```

**Create a config file:**

```sh
cp config.example.json config.json
```

**Run the script:**

```sh
python3 main.py
```

## Configuration Reference

- `debug`: If set to true, will print debug logs.
- `window_title`: The title of the window that the keybinds will be sent to. No
  other window will be affected and the keybinds only be sent to the window if
  it's in focus.
- `keybinds`: A dictionary containing the keybinds. The key of the dictionary is
  the name of the key in all lowercase. The value is an array containing the
  coordinates of the tap. You can find these coordinates by enabling the
  "Pointer location" option in the "Developer options" menu of your Android
  device. The coordinates are relative to the top-left corner of the screen.

## Notice

> [!WARNING]
> This script was originally written to enable BlueStacks-like keyboard controls
> for Android Studio's AVD on macOS. While pretty harmless on its own, depending
> on the game you're playing, it might be considered cheating/third-party
> tooling and might get you banned from the game. Use at your own risk and read
> the terms of service of the game you're playing before using this script.

> [!CAUTION]
> Do not, under any circumstances, use this script to automate any kind of
> interaction with the game.
