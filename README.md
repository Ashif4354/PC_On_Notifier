# PC ON Notifier  

PC ON Notifier is a simple yet powerful utility that notifies you via Discord whenever your Windows PC is switched on. This tool ensures you stay informed about your system's status with ease.  

## Use Case
This can be used to monitor if someone signs in to your PC without your knowledge. By receiving a Discord notification each time your PC starts, you can stay informed about any unauthorized access or suspicious activity on your system.

## Key Features  
- **Built with Python**: The entire project is developed using Python, showcasing the flexibility and power of the language.  
- **Discord Notifications**: Sends a custom notification to your Discord webhook when the PC starts.  
- **Windows Compatibility**: Works exclusively on Windows operating systems.  
- **Startup Notification**: Automatically runs the program when your PC starts.

## Prerequisites  
* No need to install Python or worry about dependencies. Everything is handled seamlessly for you.  
* You only need to install UV

### Step 1: Install UV  
1. Open PowerShell.  
2. Run the following command:  
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
Other installation methods are available on the [official UV website](https://docs.astral.sh/uv/getting-started/installation/).

### Step 2: Clone the Repository 
Make sure you have Git installed on your system. If not, you can download it from [here](https://git-scm.com/downloads).
```
git clone https://github.com/Ashif4354/PC_On_Notifier
```
or download the ZIP file and extract it to a directory of your choice.

### Step 3: Set Up Discord Webhook
* Obtain a Discord webhook URL
    * Select the Server
    * Under the desired text channel, select Edit Channel (gear icon) 
    * Select Integrations
    * Select Webhooks and click New Webhook. 
    * Edit the webhook data if you want & Copy the Webhook URL

* Open the main.py file in a text editor.
* Paste the webhook URL between the double quotes in the designated section of the code. You can also customize the title, description, and color of the Discord embed if desired.

* After editing the main.py file, save and close it.

### Step 4: Build the Executable
* After editing the main.py file, double-click the `BUILD EXE.bat` file. This will generate an executable file named PC_ON_NOTIFIER.exe in the same directory.

### Step 5: Enable Startup Notification
* Place the PC_ON_NOTIFIER.exe file in the Startup folder to ensure it runs automatically when your PC starts.
    * Press `Win + R` to open the Run dialog box.
    * Type `shell:startup` and press Enter.
    * Place the PC_ON_NOTIFIER.exe file in the Startup folder.
    * Restart your PC.

* The path to the Startup folder is typically `C:\Users\<user-name>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`


## Usage
* This application requires internet access to send notifications to Discord.
* Sometimes you may need to configure the firewall to not block this application.
* Now, every time your PC is switched on, the PC_ON_NOTIFIER.exe will execute, and you’ll receive a Discord notification!
  #### Hiding the Application in the Startup Menu (Optional)
  * When the application is in the Startup folder, it will appear in the Startup tab of the Task Manager or the Startup Apps menu in system settings.
  * To prevent suspicion, simply rename the generated `PC_ON_NOTIFIER.exe` file to a commonly used system app name before placing it in the Startup folder.
  * Some suggested names include `SystemUpdate.exe`, `DriverUtility.exe`, etc.
  * After renaming the file, place it in the Startup folder as described in the installation steps. This will help ensure it blends seamlessly with other startup entries.


## Contribution
Contributions are welcome! Feel free to fork this repository and submit a pull request with your enhancements.

## License
This project is licensed under MIT License.

## Contact
* For questions or feedback, feel free to reach out.<br>
* I am always ready to help.<br>
* Contact details are available on my GitHub profile.