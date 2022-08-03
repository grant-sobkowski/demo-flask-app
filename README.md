# Homework API

apache/flask web server running on an AWS ec2 instance.

## How It's Made

1. Create an EC2 instance with ubuntu as the base image
2. Install necessary packages with apt: apache2, python3-pip,
   libapache2-mod-wsgi-py3
3. Clone this repo in home directory
4. Create .conf file in etc/apache2/sites-available/
5. Enable file with a2ensite
6. Restart apache2 server and view flask server