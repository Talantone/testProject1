# testProject1


This project is designed to display and edit user tasks.


# launch

There are two ways to launch an application:
Makefile and docker.
To use the Makefile, you must have a Unix system. Just write 'make' in the project folder.
The project runs in debug mode for the convenience of checking requests.

# requests and responses

The project supports Django authorization (Users are created through the admin panel).  
If the user is logged in, then when clicking on the url localhost:8000/api/v1/my_tasks/, 
a list of his tasks will be returned to him. The user can add new tasks from this url.
When navigating to the url localhost:8000/api/v1/my_tasks/"task id"/ 
The user can edit the text and status of the task, if he created this task.
