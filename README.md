# My Talon Scripts
These are all written for my own setup but are public in case others might find them useful. All of these are supplementary to  the standard knausj repo  on the most recent release.

To set up talon and this repo, simply paste the following into a terminal. The first line is fish shell syntax for the url variable. Change this if you have a private beta url or you use a shell with different syntax
```
set URL "https://talonvoice.com/dl/latest/talon-linux.tar.xz"
echo "curl $URL --output talon.tar.xz; tar -vxf talon.tar.xz; rm -f talon.tar.xz; mv talon/ ~/talon; mkdir -p ~/.talon/user  ; git clone https://github.com/C-Loftus/my_talon_scripts ~/.talon/user/myscripts" | sh
```
