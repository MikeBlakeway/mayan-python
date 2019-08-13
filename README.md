# Mayan Web Studio

A simple Django project boilerplate with Sass 7-1 architecture, compiler and live reload via BrowserSync

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Project Setup
Create a django ready virtual environment with mySQL database ready
```
virtualenv .env
source .env/bin/activate
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

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Keith Dechant - https://www.metaltoad.com/blog/instant-reload-django-npm-and-browsersync
* Sass Architecture - https://sass-guidelin.es/#architecture
