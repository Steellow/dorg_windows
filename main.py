import os

import win32file
import win32event
import win32con
import datetime

path_to_watch = os.path.abspath(r'./playground')


def move_files():
    # Creates array of files (string) in Downloads folder
    files = (file for file in os.listdir(path_to_watch)
             if os.path.isfile(os.path.join(path_to_watch, file)))

    for file in files:
        filename_split = file.split(".")
        extension = filename_split[len(filename_split) - 1]

        # Creates file extension folder if it doesn't exist already
        extension_folder_name = path_to_watch + "\\" + extension
        if not os.path.exists(extension_folder_name):
            os.makedirs(extension_folder_name)

        # Moves the file to the correct directory
        try:
            os.rename(path_to_watch + "\\" + file,
                      extension_folder_name + "\\" + file)
        except:
            # If file with same name already exists, add datetime to new files' name
            now = datetime.datetime.now()
            formatted_datetime = now.strftime("_%Y-%m-%d--%H-%M-%S")
            filename_without_extension = os.path.splitext(file)[0]
            os.rename(path_to_watch + "\\" + file, extension_folder_name +
                      "\\" + filename_without_extension + formatted_datetime + "." + extension)


#  FindFirstChangeNotification sets up a handle for watching
#  file changes. Second parameter is a boolean indicating whether the
#  directories underneath the one specified are to be watched ( 0 = no );
#  the third is a list of flags as to what kind of changes to
#  watch for. We're just looking at file additions / deletions.
change_handle = win32file.FindFirstChangeNotification(
    path_to_watch,
    0,
    win32con.FILE_NOTIFY_CHANGE_FILE_NAME
)

#  Loop forever, listing any file changes. The WaitFor... will
#  time out every half a second allowing for keyboard interrupts
#  to terminate the loop.
try:
    while 1:
        result = win32event.WaitForSingleObject(change_handle, 500)

        if result == win32con.WAIT_OBJECT_0:
            move_files()

            win32file.FindNextChangeNotification(change_handle)

finally:
    win32file.FindCloseChangeNotification(change_handle)
