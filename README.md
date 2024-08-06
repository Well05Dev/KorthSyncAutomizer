# KorthSyncAutomizer
Using PyAutoGui to automate a repetitive process in business.

The executable is located in the path: "C:\Users\integracao\Documents\SyncKorth\dist\SyncKorth".

The parameters used only work for monitors with 1366 x 768 resolution.

To find the right parameters for other resolutions, you must use the "searchcursor.py" file found in the "cfg" folder.
You must position the cursor/mouse in the position to be discovered and then execute the file.
Thus, the X and Y parameters will be returned in the terminal.
After that, use the returned values ​​to parameterize the "SyncKorth.py" file according to the comments made in it.

In case of changes, another .exe must be generated
Follow the step by step:

1- Open CMD;
2- "cd C:\Users\integracao\Documents\SyncKorth\cfg";
3- pyinstaller -w SyncKorth.py

An executable will be generated which will be found in the "dist" folder.

*IMPORTANT: Korth only allows automatic access if there are administrator permissions when running.
Therefore, it is important that to run, cmd is opened as an administrator.

In the task scheduler, the "Run with higher privileges" option must also be enabled.
