# My Talon Scripts

All of these are supplementary to the standard knausj (now called the talon `community`) repo on the most recent release.

- I have my own fork of `community` and use this for any personal code

# Functionality

- Send custom JS/TS to the browser from within Talon
- Operate a pedal with custom overrides and multiple presses at once
- Pandoc via voice for office use (converting between word docs/slides/etc.)
- Various config and helper actions
- Voice commands for git pulling
- and more!

GPT and AI functionality has been moved into a separate repo [https://github.com/C-Loftus/colton_talon](https://github.com/C-Loftus/colton_talon) for easier usability.

## Git Helpers

### Install Just One Script Directory from this Repo

[https://download-directory.github.io/](https://download-directory.github.io/)

### View History of a Given File

[https://github.githistory.xyz](https://github.githistory.xyz)

## Install Talon and All My Scripts

(Script below assumes fish, change the set command for bash)

```sh
set URL "https://talonvoice.com/dl/latest/talon-linux.tar.xz"
curl $URL --output talon.tar.xz
tar -vxf talon.tar.xz
rm -f talon.tar.xz
mv talon/ ~/talon
mkdir -p ~/.talon/user
git clone https://github.com/C-Loftus/my_talon_scripts ~/.talon/user/myscripts
```

# Notes

Talon is not like a traditional Python environment. Stylization and code choices in this repo reflect that

- When Talon is loaded, all Python files in the Talon user directory are all ran at startup.
- We do not have an exposed central `main()` function from which to enter our scripts
- Python scripts which define voice commands are _not_ intended to be exported to other Python functions through `import`.
  - Any shared Python code is defined in specific helper modules and separated from voice command definitions.
- `global` variables are actually a _good_ practice for keeping state in Talon becuase of the fact each file defines voice commands that are only called from `.talon` scripts which don't have access to these `global` variables.
  - `global` is a simple way of sharing state across all related functions in one particular file, since we don't want to have to manually pass in state arguments through voice each time. It is easier to simply set it for an entire group of related commands.
  - For more complicated state that can be shared across many voice commands, Talon provides modules, tags, and scopes, all of which expose state to `.talon` scripts.

# Acknowledgements

[https://github.com/AndreasArvidsson/andreas-talon/](https://github.com/AndreasArvidsson/andreas-talon/)
