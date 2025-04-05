# Neo Launcher

Neo Launcher is a lightweight Windows utility that automatically closes all the uncompatible apps and keeps the backround processes of those apps blocked so that neo Broser can be runned smoothly without needing to manualling uninstalling or closing the application from task manager.


-  Automatically closes apps like Brave, Edge, WhatsApp, etc.
-  Configure which apps to block via a simple text file.
-  Designed to run silently in the background.
-  Blocks even crash handler processes for stricter lockdown.
-  Dynamic support for custom browser paths (Neo Browser etc.).

## How to Use

### Step 1: Clone the repo
Clone the project using git clone https://github.com/Aditya0o7/neoLauncher.git or download the zip and extract the project

### Step 2: Install Required packages
In terminal run pip install -r requirements.txt

### Step 2: Configure the Neo Browser path
In neo_path.txt add Neo Browser's path no need to add quotes around.
(to find out the path of neo browser type dir /s /b "Neo Browser.exe" in command prompt and copy the path from there to paste in the txt)

### Step 3: Configure the blocked_processes.txt
- To configure the blocked processes first run the neo browser and look for the apps it mentioned which needs to be closed
- Now open task manager and search for each of the apps -> open file location -> and note that exe file name
- Copy paste that .exe name in the txt ensure that the name must be in lower case even when the actual exe name is not in lower case
(ensure you put all the sub process of the app as well from the task manager for eg lets say for brave search brave in taskmanager and put all exe names which was shown in task manager i.e. related to brave)
- By default brave.exe and all its sub processes are added along with msedge.exe and whatsapp.exe

### Step 4: Run the .py file
- Open Command prompt with admin privilages
- cd to the the neoLauncher project
- run neoLauncher.py 

By following these steps the script will runs without any issues and it will automatically close all the apps and processes and then open up the Neo Browser without needing to manually do it everytime. Once the Neo Browser is closed the script will automatically close all the apps and processes can be started again.

### So by setting up all paths once there is no need to uninstall/end task everytime you want to use Neo Browser.
