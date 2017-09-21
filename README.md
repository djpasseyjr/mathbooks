# MathBooks
# README #
  
### What is this repository for? ###

* This is a project for the BYU Math department. It streamlines textbook checkout.  
* Version 1.0  
  
### How do I get set up? ###
  
* Dependencies:  
  This program requres Python 2 and the following libraries: mysquite3, web, validate_email.  
  This program requires PHP  
  This program requires Apache2  
  
 * Copy the mathbooks folder to the /Library/WebServer/Documents folder.  
   
 * Move the index.php file from mathbooks to the /Library/WebServer/Documents folder  
   
 * Run Apache by entering the following into the terminal:  
    sudo apachectl start  
   
 * Make a change to permissions in the mathbooks folder by entering the following in the terminal:  
    sudo chmod 777 /Library/WebServer/Documents/mathbooks 
   
 * Make the following changes to your apache httpd.conf file  
   	Navigate to /etc/apache2 and edit the httpd.conf file  
 	Locate the following line and remove the comment (#) from the beginning:    
	LoadModule php5_module libexec/apache2/libphp5.so  
	Change the line: "DirectoryIndex index.html" to "DirectoryIndex index.php"  
	Then restart apache with: sudo apachectl restart  
   
 * Test that everything is working by navigating to 'localhost' in your browser  
 

### Who do I talk to? ###

* Email djpasseyjr@gmail.com with any questions