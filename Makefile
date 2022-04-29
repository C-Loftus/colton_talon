setup: cursorless
	curl "https://talonvoice.com/dl/latest/talon-linux.tar.xz" --output talon.tar.xz
	tar -vxf talon.tar.xz
	rm -f talon.tar.xz
	mv talon/ ~/talon
	mkdir -p ~/.talon/user   

git:
	git clone https://github.com/david-tejada/rango-talon  ~/.talon/user/rango-talon
	git clone https://github.com/cursorless-dev/cursorless-talon.git ~/.talon/user/cursorless-talon
	git clone https://github.com/C-Loftus/knausj_talon ~/.talon/user/knausj_talon
	git clone https://github.com/C-Loftus/my_talon_scripts ~/.talon/user/myscripts
	git clone https://github.com/tararoys/dense-mouse-grid ~/.talon/user/dense-mouse-grid

pull:
	find ~/.talon/user -name .git -print -execdir git pull \;