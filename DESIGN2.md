__screens__
__/login__
![image login](/img/login.png)
route: (/login)
on this screen the user can login. when clicked on login the user is redirected to /controller
the user can also click on register and is then redirected to /register
pages: layoutlogin.html, login.html
![image register](/img/register.png)
route: (/register)
on this screen the user can register.  when  clicked on submit a new account is being made and the user is redirected to /controller
pages: layoutlogin.html, register.html

![image controller](/img/controller.png)
route: (/controller)
on this page the user sees the controllers and can interact with them.
when  clicked on the (+) icon the user is redirected to /addcontroller
when clicked on the garbage bin, a form is submitted to the same route  where the controller item is deleted from the databaseand the page is reloaded
pages:  controller.html, template.html

![image addcontroller](/img/addcontroller.png)
route: (/addcontroller)
On this page the user can add controllers. when pressing "add controller" the user is redirected to /controller, and a form is submitted to the database 
pages: addcontroller.html, template.html

![image measurement](/img/measurement.png)
route: (/measurement)
on this page the user can see the measurements. 
when clicking (+) icon the user is redirected to /addmeasurement.
when clicked on the garbage bin, a form is submitted to the same route  where the measurement item is deleted from the database and the page is reloaded
when clicking on the record button, the incoming data is written in a csv file untill pressed again. then the user will be redirected to /download/filename through javascript, then the file is return and the user is redirected to the same page. 
pages:  measurement.html, template.html

![image addmeasurement](/img/addmeasurement.png)
route: (/addmeasurement)
On this page the user can add measurements. when pressing "add measurement" the user is redirected to /measurement, and a form is submitted to the database 

pages: addmeasurement.html, template.html

![image setup](/img/setup.png)
route: (/setup)
on this page the user gets instructions on how to setup the raspberry pi. 
pages: setup.html, template.html

route(/download/filename.cs)

