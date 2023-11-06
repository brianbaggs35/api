Brian's Web Security Assignment File Structure
This should work if you extract all files to C:\Flask\brian or wherever your Flask directory is located
If this does not run, copy the files inside the folder brian to your flask directory which is C:\flask by default

I have also provided an SQL query to setup the database. All you need to do is create a schema named api and then run the query and
that will setup the database.

Note - I had some issues with doing consecutive actions like submitting the form with the fields filled out, then going back and
trying to submit it empty. It returned a cursor not connected error. I am out of time so all you have to do is reload the main
page or just restart your flask server and then perform one action at a time. I suspect it's something with the way I'm closing
my connections but I am out of time so I will submit it as is. I already spent way too much time on this assignment.

C:\FLASK\BRIAN
├───Include
├───Lib
├───Scripts
├───static - folder for static files
│   ├───favicon.ico
│   ├───mainpage.css
│   ├───success.css
├───templates - folder for HTML files
│   ├───index.html
│   ├───signup.html
│   ├───success.html
│   ├───empty.html
├───app.py
├───pyvenv.cfg
├───README.txt
├───setup database.sql