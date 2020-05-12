import os

import win32file
import win32event
import win32con

path_to_watch = os.path.abspath (r'./playground')

#  FindFirstChangeNotification sets up a handle for watching
#  file changes. Second parameter is a boolean indicating whether the
#  directories underneath the one specified are to be watched ( 0 = no );
#  the third is a list of flags as to what kind of changes to
#  watch for. We're just looking at file additions / deletions.
change_handle = win32file.FindFirstChangeNotification (
  path_to_watch,
  0,
  win32con.FILE_NOTIFY_CHANGE_FILE_NAME
)

#
# Loop forever, listing any file changes. The WaitFor... will
#  time out every half a second allowing for keyboard interrupts
#  to terminate the loop.
#
try:
  while 1:
    result = win32event.WaitForSingleObject (change_handle, 500)

    #
    # If the WaitFor... returned because of a notification (as
    #  opposed to timing out or some error) then look for the
    #  changes in the directory contents.
    #
    if result == win32con.WAIT_OBJECT_0:
      print("LMFAO")

      win32file.FindNextChangeNotification (change_handle)

finally:
  win32file.FindCloseChangeNotification (change_handle)