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

## ssh ec2
> ssh -i ~/tmp/catan-app.pem ec2-user@44.241.255.195
 
 
# url of ec2 app
http://ec2-44-241-255-195.us-west-2.compute.amazonaws.com:5000
