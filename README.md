# TeamCatan
Small app to help playing team-based Catan.

## First time setup
install Flask

in the root of the project:
> python3 -m venv venv
> 
> . venv/bin/activate
> 
> pip install Flask
 
 

## To run it
in the root of the project:
> . venv/bin/activate
> 
> flask run 

## To run it on ec2
> flask run --host=0.0.0.0

## scp the zip to the ec2 host
> scp -i ~/tmp/catan-app.pem TeamCatan.tgz  ec2-user@34.222.153.242:/home/ec2-user
