# Lohum_Assignment

# FastAPI Web Scraping

This project demonstrates a simple FastAPI application that performs web scraping on a specific URL and retrieves average data using the BeautifulSoup library.

<h3> Prerequisites</h3>

Before running the application, ensure that you have the following dependencies installed:<br>

FastAPI<br>
BeautifulSoup<br>
Requests<br>
Installation<br>

  <h3> Clone the repository:</h3>
shell <br>
Copy code <br>
$ git clone <repository_url> <br>
Navigate to the project directory: <br>
shell <br>
Copy code<br>
$ cd fastapi-web-scraping<br>
Install the required dependencies using pip:<br>
shell<br>
Copy code<br>
$ pip install -r requirements.txt<br>
Usage

<h3>Start the FastAPI server: </h3>
shell. <br> 
Copy code. <br>
$ uvicorn main:app --reload. <br>
Open your web browser and access the following URL: <br>
Copy code <br>
http://localhost:8000/ <br>
The web scraping is done using the BeautifulSoup library. The application sends a GET request to the specified URL and retrieves the content. It then parses the HTML content using BeautifulSoup and extracts the average data. The heading "Lohum Assignment" followed by "by Parthvik Ajmera" is added to the response.

<h3>Handling Invalid Links</h3>

If an invalid link is provided (i.e., it does not start with "https://"), a 400 Bad Request error will be returned with the message "Invalid link provided."

<h3>Deployment</h3>

To deploy this code using Render and access it at the link https://lohum-parhtvik.onrender.com, follow these steps:<br>

Sign up for an account on Render at https://render.com if you haven't already.<br>
Create a new web service on Render and connect it to your Git repository where the code resides.<br>
Configure the deployment settings to use the appropriate deployment command, which is typically uvicorn main:app --host 0.0.0.0 --port $PORT.<br>
Deploy the application on Render.<br>
Once the deployment is complete, you can access the application at the provided link https://lohum-parhtvik.onrender.com.<br>


