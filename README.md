# store-manage-with-database

[![Build Status](https://travis-ci.org/wandesky/store-manager.svg?branch=ft-post-sale-record-161204436)](https://travis-ci.org/wandesky/store-manager)

# Store-manager
## Introduction
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.

## Running the app locally (UI-Challenge 1)
- Clone the repo using ` git clone https://github.com/wandesky/store-manager.git `.
- Move to the application's directory using ` cd store-manager `.
- Open ` index.html` with your browser to access the homepage.

## Running the app online (UI - Challenge 1)
You can access a live version of the user interface by clicking the link below:
- [Store Manager](https://wandesky.github.io/store-manager/)

## Running the app locally (API - Challenge 2&3)
### Challenge 2
**Follow the instructions below to run a copy of the app from challenge 2 _(does not support data persistence)_**
1. Git clone the repo using `git clone https://github.com/wandesky/store-manager.git`
2. Checkout the bootcamp-week one branch using `git checkout bootcamp-week-one`
3. Switch to the project folder using `cd store-manager`
4. Create a virtual environment using `virtualenv venv`
5. Activate the virtual environment using `source venv/bin/activate` in linux or `venv/script/activate` for windows
5. Install the required dependencies using `pip install -r requirements.txt`
6. Start the server and launch the app using `python run.py`

### Challenge 3
**Follow the instructions below to run a copy of the app from challenge 3 _(supports data persistence using PostgreSQL database)_**
1. Git clone the repo using `git clone https://github.com/wandesky/store-manage-with-database.git`
2. Checkout the bootcamp-week one branch using `git checkout bootcamp-week-one`
3. Switch to the project folder using `cd store-manager`
4. Create a virtual environment using `virtualenv venv`
5. Activate the virtual environment using `source venv/bin/activate` in linux or `venv/script/activate` for windows
5. Install the required dependencies using `pip install -r requirements.txt`
6. Start the server and launch the app using `python run.py`

## Running the app online (API - Challenge 2&3)
- The API following specifications from Challenge 2 can be accessed on Heroku by [clicking here](https://wandesky-store-manager.herokuapp.com/).
- The API following specifications from Challenge 3 can be accessed on Heroku by [clicking here](https://wandesky-stg-store-manager-ch3.herokuapp.com/).


## Different Pages for Store Manager App (User Interface - Challenge 1)
### Login page
![Login Page](https://user-images.githubusercontent.com/19204205/46584874-7fdb6500-ca71-11e8-9403-b6fb3d22782e.png)

### View Sales Records page (Attendant)
![Attendee's View of Sales Record](https://user-images.githubusercontent.com/19204205/46633346-11240780-cb56-11e8-8fbc-6079395892f8.png)

### View Sales Records page (Admin)
![Admin's view of Sales Records](https://user-images.githubusercontent.com/19204205/46824614-1a9db180-cd9a-11e8-94b1-7c38318e6744.png)

### View Available Products (Attendant)
![Attendants's View of Available Products](https://user-images.githubusercontent.com/19204205/46850922-641fe800-cdfe-11e8-90d2-6c24868537fd.png)

### View Available Products (Admin)
![Update Products](https://user-images.githubusercontent.com/19204205/46852317-3e491200-ce03-11e8-9256-86f57bd79ff2.png)

### Create New Attendant (Admin)
![Add Attendant](https://user-images.githubusercontent.com/19204205/46860525-47dd7480-ce19-11e8-8f43-1ec488f21e82.png)

### Add Item to Cart (Attendant)
![Add to Cart](https://user-images.githubusercontent.com/19204205/46865106-fe932200-ce24-11e8-9bbf-3ca3985fdaf9.png)

### User Profile Page (Attendant)
![User Profile](https://user-images.githubusercontent.com/19204205/46863894-5465cb00-ce21-11e8-87b7-149bd9c049b1.png)

## How to Contribute
If you wish to contribute to this projects:
* Fork the repo
* Create a feature branch e.g. ``` git checkout -b your-proposed-feature ```
* Push the changes to your branch e.g. ``` git push origin your-proposed-feature```
* Create a pull request
