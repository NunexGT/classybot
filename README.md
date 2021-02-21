# classybot
A bot to greet your teachers in Google Classroom without having to wake up early.

<h1>Introduction:</h1>
Imagine the scenario where your area were affected by COVID lockdown and now you are at home and the governament decided to adapt your school to an online environemt. To make sure that during the class time you´re really wake up and stand by your computer, your teacher decides that you must greet them on Google Classroom, but that is just stupid or you just want to sleep, so here is the solution.
<br>
<p>Introducing the <b>ClassyBot</b></p>

A bot that will open chrome, grab the most recent teacher comment it detects and then comments with a "Good Morning" or a "Good Afternoon" (Portuguese version available) so your teacher thinks you´re there and you´ll never have to wake up early again! ;)


<h1>How to Guide:</h1>
Now I will explain how you can use this bot.
<br>
Video Tutorial May be coming soon
<br>
<h2>Prequesits</h2>
<h3>Google Chrome</h3>
<br>
So, I have decided to only support chrome on my bot because if you create a user with the account that you use to access your school classroom, the probabilities of asking the passsword after some time are lower and it works better because of the chrome driver. Also, I have to use a school email with the school´s domain, so it´s better for me to seperate from my personal things in that way. And chrome is the most used browser. I don´t like chrome too, but it´s easier. Feel free to edit the .py files to support other browsers.
<ul>
  <li><h4>Install Chrome</h4></li>
 Now, I assume you already know how to do this. But if you don´t know, just go to https://www.google.com/intl/en-US/chrome/,   click in the button that says "Download Chrome" and then follow the instructions on the screen.
  <li><h4>Create a new user with only the Google Account that you will use for Google Classroom</h4></li>
    Now that you have Chrome installed, you need to create a new chrome user. Go to the icon of your current user, select "Add", add a name and choose a picture. Then you need to enter any Google Services and login to the Google Account that you will use in Google Classroom.
  <br>
  <br>
 <b>Attention<b>:If you already add one extra user or more, you´ll need to reinstall chrome. When Uninstalling Chrome don´t forget to mark the box to delete all user data. Once it´s installed Chrome again, put all your things again on the default account (the first that will prompt after the fresh install) and then create the user by the process written above.
  <br>
  <br>
  <b>Note<b>: You can also edit the .py file in the line 50, change "profile 1" to "default" or any user with "profile (any number)". Make a trial and error when testing the bot         to see if it goes to the user of your choice. Just make sure that when the bot opens chrome, it uses the correct Google Account
    </ul>
<h3>Python</h3>
    <ul>
      <li><h4>Install Python</h4></li>
        Python it´s not really hard to install. If you could install Chrome, you probably will be able to install Python with no problems.
      <br>
      <b>Just make sure it´s version 3.9</b>
      <ol>
        <li>Go to https://www.python.org/downloads/, and press the Download Python 3.9.1 button</li>
        <li>Open the Downloaded File</li>
        <li>Select costum installation</li>
        <li>Mark the box that says "pip" and leave the rest as it is.</li>
        <li>Follow the instructions that appear</li>
      </ol>
      You can also watch this tutorial by <i>Amit Thinks</i> on YouTube:https://www.youtube.com/watch?v=IDo_Gsv3KVk
      <li><h4>Install needed dependencies</h4></li>
    Once Python and pip are installed. Do the following so the bot can execute correctly:
      <ol>
        <li>Prees Win+R buttons at the same time</li>
        <li>Write "cmd" on the text field</li>
        <li>Press the cntrl and shift button at the same time you press "OK"</li>
        <li>Press the Yes button</li>
        <li>Come back to this repo and download the "requirement.txt" file</li>
        <li>Write cd (path to "requirement.txt" file) on the cmd window. Probable example:cd C:\Users\(Your Username)\Downloads</li>
        <li>write "pip install -r requirement.txt"</li>
        <li>Wait and when it doesn´t happen nothing in the screen for a while. It probably worked. If it´s happearing too many red caracters, probably you didn´t enter the cmd as admin (press shift when pressing ok on the run window).</li>
      </ol>
      If cmd presents an error like "'pip' is not recognized as an internal or external command, operable program or batch file.", please follow the instructions on this video: https://youtu.be/zYdHr-LxsJ0. Make sure that you are using the same Python path installation as the installer used when you installed Python.
    </ul>
    <h3>chromedriver</h3>
    <ol>
      <li>Go to https://chromedriver.chromium.org/downloads</li
      <li>Download the version that matches your browser and your OS(Probably the latest)</li>
      <li>Unzip the file</li>
      <li>Create a folder in "C:\" with the name "chromedriver" and paste the chromedrive.exe</li>
    </ol>
 Attention:After the browser updates, the chromedriver will became obsolete and you´ll not be able to use the bot unless you update it. You can disable Chrome updates to prevent it, but maybe you can find some script to auto updat eit. Just make sure that the chromedriver is in that location unless you change it in the .py file
    <br>
    <h2>Using the Bot</h2>
    Now the worst part is gone. You just have to do this and the bot is prepared
    <ol>
      <li>Click on the green button that says "code" on this repo and click "Download as zip"</li>
      <li>Unzip It</li>
      <li>Open the folder and change the schedule.csv to schedule.txt (Make sure that Windows as that option enabled, if you try to change the name of the file but you don´t see the ".csv" in the final of the file name, do as this tutorial says: https://vtcri.kayako.com/article/296-view-file-extensions-windows-10)</li>
      <li>You will now see the example that I put. Don´t delete the first line, only the second. Write everything as it apppears, with no space and only seperated by ",". In the link space you will copy and paste the site link for the Google Classroom of that Class (something like: https://classroom.google.com(...))</li>
      <li>Now open the .py file corresponding to your language and wait until class starts. The bot will verify if it´s the hour every 40 seconds</li>
    </ol>
      
 <h1>Tips and Tricks</h1>
 Here are some things to make this bot work better.
 <ul>
  <li><h3>Auto start the bot with Windows</h3></li>
  So, for the bot to work the window of the bot must be open at the time at the class, but there is the chance that you will forget to open the bot. So to solve this:
  <ol>
    <li>Go to the bot location, click with the right button of your mouse, go to "Send to" section and select "Send to Desktop (Create Shortcut)</li>
    <li>Press Win+R and write "shell:startup" and copy the shortcut</li>
    <li><i>To start it minimized:</i>Right click the shortcut, go to properties, click in the "Execute" box and select "Minimized"</li>
  </ol>
  <li><h3>Use a virtual machine or other PC</h3></li>
  Now, probably you will want to play videogames during the class, but the thing is when the time arrives, the control of you PC will be taken from you (and if it doesn´t I don´t recommend you to use the PC while the bot is executing) or you are just viweing a YouTube video. So, to make sure that the bot doesn´t ruin your fun, try to create a Virtual Machine, do everything in there and then you just leave it running with your PC so it will never ruin your Gaming Experinece. If your PC is not so great, try to find another PC and leave the bot running there.
  <li><h3>Give a delay on the schedule.csv file, to make sure that your teacher writes the comment were do you need to greet</h3></li>
</ul>
  <h1>Notes</h1>
  <ul>
  <li>This bot was made to run on Windows and Chrome, so please, understand that it´s not optimized to other scenarios. Feel free to edit the bot so more people can use it</li>
  <li>The bot window must be running at the time of your class to work, so your PC also needs to be working at the time. What I´m saying is, if you want to sleep until late, you need to live your PC turned on</li>
  </ul>
  
  <h1>Changelog</h1>
  <h3>V1.0=Bot´s launch</h3>
  <h3>V1.1=Added a feature where it´s not needed for the user to configure the path to the chrome user files. The bot will detect the Windows's user name and it will do it by itself</h3>
  
  <h1>Check this out</h1>
  This bot was partially inspired by the Gmeet bot created by <i>Sheen Santos D. Capadngan</i> on GitHub:https://github.com/sheensantoscapadngan/gmeetbot
  <br>
  Also check his youtube video (it´s really great):
  <br>
  https://www.youtube.com/watch?v=UpDkXaEmHAs
  
  <h1>Legal</h1>
  I´m not responsible if you get any trouble using this bot
  <br>
  This bot is for Educational Porpuses
  <br>
  <br>
  <br>
  Bot created by SuperX-dev on GitHub
  
    
      
      
        
    
  

