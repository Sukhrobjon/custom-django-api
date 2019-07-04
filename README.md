# Profiles-Rest-API
This api can be usefull as it uses the very common architecture in social media, or any other platform where user has profile and status. This can be used as an api of the users' dashboard
You can find the more in [Proposal](https://github.com/Sukhrobjon/predict-movie-genre/blob/master/proposal.md)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Make sure you have `Python3` installed in your machine.

### Installing

A step by step series of examples that tell you how to get a development env running

1. Clone the repo `git clone https://github.com/Sukhrobjon/profiles-rest-api.git`

2. Go to folder `cd profiles-rest-api`

1. Now Install `venv` inside root of project folder `virtualenv -p python3 venv` 

1. activate venv  `source venv\bin\activate`

1. pip install the dependencies in `requierements.txt` file `pip install -r requirements.txt`

## Deployment
The app is live on following servers:

- [Heroku](#)
- [AWS](http://ec2-13-59-212-52.us-east-2.compute.amazonaws.com/api/)


### Available Endpoints
### Base URL: http://ec2-13-59-212-52.us-east-2.compute.amazonaws.com/api/

|       Method        |      Resources     |      Return Object                         
| -------------       |--------------------| ------------------------------------------
| GET                 | /profile                       | All Users         
| GET                 | /profile/:id             | Specific user   
| GET                 | /feed               | All feeds 
| GET                 | /feed/:id           | Specific feed 


## Built With

* [Django](https://www.djangoproject.com/) - Python Web framework
* [Django Rest Framework](https://www.django-rest-framework.org/) - Tool for Web APIs 
* [AWS](https://rometools.github.io/rome/) - Amazon Web Services, Cloud computing platforms
* [Heroku](https://heroku.com) - Cloud Platform



