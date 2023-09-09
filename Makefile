setup: 
	curl "https://talonvoice.com/dl/latest/talon-linux.tar.xz" --output talon.tar.xz
	tar -vxf talon.tar.xz
	rm -f talon.tar.xz
	mv talon/ ~/talon
	mkdir -p ~/.talon/user   

clone:
	git clone https://github.com/C-Loftus/knausj_talon ~/.talon/user/knausj_talon
	git clone https://github.com/C-Loftus/my_talon_scripts ~/.talon/user/myscripts
	git clone https://github.com/paul-schaaf/talon-filetree-commands/blob/master/tree.talon
	# git clone https://github.com/tararoys/dense-mouse-grid ~/.talon/user/dense-mouse-grid

fetch: pull
	cd ~/.talon/user/knausj_talon; git fetch upstream main
pull:
	find ~/.talon/user -name .git -print -execdir git pull --ff-only \;

windows:
	# mimic xbox controller to get rid of direct input and get xinput for talon. Talon uses gilrs and needs xinput
	echo "https://github.com/csutorasa/XOutput"

build: 