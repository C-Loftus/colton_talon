setup: cursorless
	curl "https://talonvoice.com/dl/latest/talon-linux.tar.xz" --output talon.tar.xz
	tar -vxf talon.tar.xz
	rm -f talon.tar.xz
	mv talon/ ~/talon
	mkdir -p ~/.talon/user   
	mkdir -p ~/.talon/user/knausj_talon/settings
	cp -f websites.csv ~/.talon/user/knausj_talon/settings/websites.csv

cursorless:
	git clone https://github.com/cursorless-dev/cursorless-talon ~/.talon/user/cursorless-talon

pull:
	@ readlink -f ~/.talon/user/* | xargs -I{} git -C {} pull 2> /dev/null