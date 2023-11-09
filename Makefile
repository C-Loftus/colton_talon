
# specify the Talon user directory depending on operating system
ifeq ($(OS),Windows_NT)
	TALON_USER_DIR = $(USERPROFILE)\AppData\Roaming\talon\user
else
	TALON_USER_DIR =  ~/.talon/user
endif


setup: 
	curl "https://talonvoice.com/dl/latest/talon-linux.tar.xz" --output talon.tar.xz
	tar -vxf talon.tar.xz
	rm -f talon.tar.xz
	mv talon/ ~/talon
	mkdir -p $(TALON_USER_DIR)   

clone:
	git clone https://github.com/C-Loftus/knausj_talon $(TALON_USER_DIR)/knausj_talon
	git clone https://github.com/C-Loftus/my_talon_scripts $(TALON_USER_DIR)/my_talon_scripts
	git clone https://github.com/paul-schaaf/talon-filetree-commands/ $(TALON_USER_DIR)/filetree
	git clone "https://github.com/wolfmanstout/talon-gaze-ocr" $(TALON_USER_DIR)/gaze-ocr
	git clone "https://github.com/C-Loftus/private-talon" $(TALON_USER_DIR)/private-talon

	# git clone https://github.com/tararoys/dense-mouse-grid $(TALON_USER_DIR)/dense-mouse-grid
	
fetch: pull
	cd $(TALON_USER_DIR)/knausj_talon; git fetch upstream main

# git -C ../private-talon pull origin master;
pull:
	bash -c 'find ../. -type d -name '*private*' -prune -o -name .git -print -execdir git pull --ff-only \;'

windows:
	# mimic xbox controller to get rid of direct input and get xinput for talon. Talon uses gilrs and needs xinput
	echo "https://github.com/csutorasa/XOutput" 
	scoop install imagemagick
	scoop install ffmpeg
	scoop install pandoc
	scoop install obs-studio
	scoop install mpv

	scoop install https://raw.githubusercontent.com/chawyehsu/dorado/master/bucket/filebrowser.json


install:
	npm run install --prefix ./browser/js-sender

build: install 
	npm run build --prefix ./browser/js-sender

config:
	bash -c "cp -r ./.vscode/  ../."	

python:
	pipx install edge-tts