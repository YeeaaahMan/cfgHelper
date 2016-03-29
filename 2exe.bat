pyinstaller --workpath=%TEMP%/pyinst ^
            --distpath=exe ^
            --onefile --noconsole ^
            --icon=cfg.ico  ^
            --name=cfgHelper  ^
            --version-file=v3.txt window.py