# AVD Taps

Easily configure keybinds to send tap inputs to an Android Virtual Device (AVD).

> [!NOTE]
> The script currently only works on macOS. Support for other operating systems
> may be added in the future.

## Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [Android SDK](https://developer.android.com/studio/releases/platform-tools)
  (for `adb`)

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
- `preset_name`: An optional name that will be displayed in the command line.
- `keybinds`: A dictionary containing the keybinds. See the
  [Keybind object](#keybind-object) section for more information.

## Keybind object

A Keybind object defines the coordinates and behavior of a keybind. The object
contains the following fields:

- `x`: The x-coordinate of the tap. This is always required.
- `y`: The y-coordinate of the tap. This is always required.
- `keybind_type`: The type of the keybind. Defaults to `single`. Possible values
  are:
  - `single`: Sends a single tap on the specified coordinates. Holding the key
    will not repeat the tap.
  - `hold`: Sends a tap on the specified coordinates and repeats the tap as long
    as the key is held.
  - `swipe`: Sends a swipe gesture from the specified coordinates. If you use
    this type, you must also specify the `distance` and `angle` parameters.
  - `swipe_hold`: Sends a swipe gesture from the specified coordinates and holds
    the swipe as long as the key is held. If you use this type, you must also
    specify the `distance` and `angle` parameters.
- `distance`: The distance of the swipe gesture in pixels. Has no effect if the
  `keybind_type` is not set to `swipe` or `swipe_hold`.
- `angle`: The angle of the swipe gesture in degrees. Has no effect if the
  `keybind_type` is not set to `swipe` or `swipe_hold`.
- `ignore_modifiers`: Whether or not the input shouldn't be sent if any modifier
  key is pressed. Defaults to `true`.

> [!NOTE]
> The script doesn't currently support simultaneous swipes.

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
