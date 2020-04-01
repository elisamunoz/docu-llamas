# Stitching Life

This website is a dedicated to people that enjoy crocheting, knitting and sewing as hobby or way of life.  The purpose of the app is to aggregate different patterns and articles related to the theme. The user is able to create, read, update and delete (CRUD) entries.

![](https://github.com/elisamunoz/docu-llamas/blob/master/doc/Multidevice%20mockup.png)

## UX
My goal is to create a user-friendly interactive Data-Centric Development project. The color scheme was taken from the predominant colours of the picture in the Home section.

### User Stories
"As a user, I want:"
* To visit a website where I can get patterns, ideas and articles regarding crochet, knitting and sewing.
* To view the website in different devices (mobile, tablet and laptop).
* To add new patterns and articles.
* To edit existent patterns and articles.
* To delete existent patterns and articles.

### Design
I used Moqups to do the previous design of this project. [Here](https://github.com/elisamunoz/docu-llamas/tree/master/doc) is the link for the mockups. The sections of the website are:

#### Home:
For this section I wanted to create a simple landing page, with a picture and a fixed navbar with links to the diferent sections.

#### About:
This sections contains a brief description for whom is the website and what the user can find on it.

#### Patterns:
In here you can find cards with differents patterns and articles available in the database, they have only little information such as, name of the pattern, the creator of the pattern or article, difficulty and an icon showing the category.

#### Pattern page:
In this site the user can see all the information available about that pattern or article, with a bigger image and a link were to download or see the full pattern in the site of the owner. This site also has a button to edit the content.

#### Edit or Add Pattern/Article
Add and Edit sites are worked under the same template but they have different urls. 
##### Edit Pattern/Article
The user gets to this site when clicking on the "Edit" button on the Pattern page. It has a form filled with all the information available from MongoDB regarding to that pattern in particular, the user is able to edit the text and either Update the info, Delete the entry or Cancel the action and go back to the Pattern page.
##### Add Pattern/Article
The link to this page is on the Navbar as "Add Pattern", this page renders the same form as in the Edit page but empty with all categories available to fill up. There are 4 category options and different fills available appear or dissappear according to what information is needed in each category.

#### Error page
This page is to tell the user that the link she or he wants to visit is not available and there is a button available to go to the landing page.

## Technologies Used

### 
* HTML
* CSS
* Javascript
* JQuery
* Python
* MongoDB
* Flask
* Bootstrap (4.3.1)
* Font Awesome (5.11.2)
* Google Fonts

## Features
* Connect to MongoDB 
* CRUD functionality
* Field validation
* Pagination
* Deep linking
* Handling 404 error
* Parallax effect

## Testing
* [W3C HTML Validator](https://validator.w3.org/) to validate HTML but it does not recognize Junja templating language.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

## Deployment
### Local Deployment:
To run the project locally, you need an Integrated development environment and have installed:
* PIP
* Git
* Python
* Mongo DB

After installing these you need to:
1. Download this repository clicking in ‘Clone or Dowload’ on top of this page, then click on ‘Download ZIP’ and extract the files in the folder you will be working on.
2. Open the folder where you download the repository in your code editor
3. Create a `.env` file containing your MongoDB credentials
`MONGO_URI='mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority'`
4. Install the required modules using this command:
`pip -r requirements.txt`
5. Create a new MongoDB database and name it ‘stitching’, then create these three collections:
* patterns	
* pattern_category			
* categories
5. Set port to the following in the app.py file:	
```
if __name__ == '__main__': 		
    app.run(
        port=8080,
        debug=True	
    )
```
You can run the app by running: `python app.py`
The project will run at `http://127.0.0.1:5000`

### Remote Deployment
The application can be deploying using Heroku. Before, you need to:
* Create a requirements.txt file in the terminal, running the command `pip freeze > requirements.txt`
* Create a Procfile running the command `echo web: python app.py > Procfile`
* Commit and Push these files to the GitHub repository
* Create a new app at the Heroku dashboard.
* Link the app in Heroku to your GitHub respository
* Go to settings then to Reveal Config Vars and set to this:
KEY | VALUE 
---------- | ------------------------------------------------------------------------------------------------------------------
IP | 0.0.0.0 
PORT | 5000  
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority` 
SECRET_KEY | `<your_secret_key>`
DEBUG | FALSE

MONGO URI AND SECRET_KEY should match the key and values from your .env file
Set host and Port to the following in your app.py file
```
if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=False
    )
```
* Push your code to GithHub and Heroku
* Your app will be hosted at `http://<your_app_name>.herokuapp.com/`

## Credits
All the pictures were taken from [Pixabay](https://pixabay.com/), [Unplash](https://unsplash.com/), and from the onwners of the patterns and articles aggregated. 
The Icons for the different categories were taken from [Flaticon](https://www.flaticon.com/).
