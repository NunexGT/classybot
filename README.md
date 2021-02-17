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
        <li>Press the shift button at the same time you press "OK"</li>
        <li>Press the Yes button</li>
        <li>Come back to this repo and download the "requirement.txt" file</li>
        <li>Write cd (path to "requirement.txt" file) on the cmd window. Probable example:cd C:\Users\(Your Username)\Downloads</li>
        <li>write "pip install -r requirement.txt"</li>
        <li>Wait and when it doesn´t happen nothing in the screen for a while. It probably worked</li>
        
      
        
    
  
!Description and how to use guide coming soon!
