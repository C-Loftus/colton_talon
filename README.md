# My Talon Scripts

All of these are supplementary to the standard knausj (now called the talon `community`) repo on the most recent release.

I don't use a fork of community. This contains all talon configuration.

# Functionality

- Send custom JS/TS to the browser from within Talon
- Operate a pedal with custom overrides and multiple presses at once
- Pandoc via voice for office use (converting between word docs/slides/etc.)
- Various config and helper actions
- Voice commands for updating the entire Talon user directory
- and more!

## Git Helpers for Extracting Specific Code from this Repo

### Install Just One Directory

[https://download-directory.github.io/](https://download-directory.github.io/)

### View History of a Given File

[https://github.githistory.xyz](https://github.githistory.xyz)

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
