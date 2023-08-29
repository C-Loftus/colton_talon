# My Talon Scripts

These are all written for my own setup but are public in case others might find them useful. All of these are supplementary to the standard knausj repo on the most recent release.




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
