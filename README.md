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
Copy code
http://localhost:8000/
This will perform web scraping on the provided URL (https://www.metal.com/Lithium-ion-Battery/202303240001) and return the average data along with the assigned heading by Parthvik Ajmera.
To retrieve data from a specific link, append the link ID to the base URL. For example, to retrieve data from "https://example.com", access the following URL: <br>

Copy code
http://localhost:8000/https://example.com <br>
Ensure that the link starts with "https://" to avoid receiving an error response.

<h3>Handling Invalid Links</h3>

If an invalid link is provided (i.e., it does not start with "https://"), a 400 Bad Request error will be returned with the message "Invalid link provided."
