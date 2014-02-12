Hello world with Node using Vagrant
===================================



###Setting up Vagrant

If you yet have downloaded vagrant and downloaded the precise32 box, you can skip this part.

Make sure you have virtual box instaleed and then install vagrant 1.4.3 from here http://www.vagrantup.com/downloads.html

Then run

    $ vagrant init precise32 http://files.vagrantup.com/precise32.box
    $ vagrant up
    $ vagrant destroy
    
It will download the virtual machine. 
    

###Configure Vagrant box

    $ git clone https://github.com/gambettinha/hello-world-django.git
    $ cd hello-world-django
    $ vagrant up
    
It will set up your environment. Let's connect into it

    $ vagrant ssh
    $ cd /vagrant/hello_world
   
    
###Running the application
    
Just run with the command

    $ python manage.py runserver 0.0.0.0:8000
    
Go in your browser to http://127.0.0.1:9000/example


Once you are done coding and playing. You can exit from the server with
    
    $ exit
    $ vagrant suspend
