# dorg_windows

Simple app to automatically organize your downloads folder. **dorg_windows** creates directory for each new filetype and moves new files into correct directories.

I'm running the script simply with pythonw (simply type `pythonw main.py` in cmd, you have it if you have python installed). This makes the script run in background, and you can kill it from task manager.

## Good to know

- If you try to manually create file inside Downloads folder, it might look like it disappears. dorg_windows acts instantly and the moment you create new file it moves it to its correct folder
- If file with same name already exists, dorg_windows adds current date and time to the new files name.
- dorg_windows doesn't affect regular folders, only files

## to-do

- [] Proper launcher (with system tray icon?)


## Stuff

[Watch a Directory for Changes](http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html) script by [Tim Golden](http://timgolden.me.uk/index.html)