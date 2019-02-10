# Django Boilerplate

A simple Django project boilerplate with Sass 7-1 architecture, compiler and live reload via BrowserSync

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* [Python 3.6](https://www.python.org/downloads/release/python-360/)
* [NodeJS](https://nodejs.org/en/)
* [MySQL](https://www.mysql.com/downloads/)
* [VirtualEnv](https://virtualenv.pypa.io/en/latest/installation/)


### Project Setup
Create a django ready virtual environment with mySQL database ready
```
pip install virtualenv env
source env/bin/activate
pip install mysqlclient
pip install django
```
Clone this repo
```
git clone https://github.com/MikeBlakeway/django-boilerplate.git
```

### Installing

Simply run an npm install

```
npm install
```

Then start a server to enable sass watch and live reload

```
npm run start
```

## Authors

* **Mike Blakeway** - *Technical Director* - [Blue Moon](https://github.com/MikeBlakeway)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Keith Dechant - https://www.metaltoad.com/blog/instant-reload-django-npm-and-browsersync
* Sass Architecture - https://sass-guidelin.es/#architecture
