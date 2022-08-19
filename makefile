PYINSTALLER_PATH=/usr/local/bin/pyinstaller

binout2h5: binout2h5.py
	 $(PYINSTALLER_PATH) --onefile ./binout2h5.py
