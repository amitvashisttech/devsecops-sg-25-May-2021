# Base Image for Custom Image
FROM ubuntu:16.04

# Owner of the Image
MAINTAINER Amit Vashist <amitvashist7@gmail.com>

# Initalize Apt-Repo 
RUN apt-get update

# Install Apache Packages
RUN apt-get install apache2 -y

# Expose the Service on Port
EXPOSE 80
EXPOSE 3306

# Custom Index Web Page 
COPY index.html /var/www/html/

# Start the Apache Service
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
