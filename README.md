# My Talon Scripts

These are all written for my own setup but are public in case others might find them useful. All of these are supplementary to the standard knausj (now called the talon `community`) repo on the most recent release.

## Install Talon and My Scripts

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

- All Python files in the Talon user directory are all ran at startup
  - We do not need a central `main()` function from which to enter our scripts, thus we can more tighly scope behavior
- global variables are actually a _good_ practice for keeping state since Python files that define voice commands shouldn't be imported as modules

  - Talon provides modules, tags, and scopes for setting state that needs to be shard across voice commands.
  - The `global` keyword is a good indicator of state that is unique to one set of voice commands. So in other words, state relevant only to the commands defined in one particular Python file
