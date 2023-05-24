# Lohum_Assignment

FastAPI Web Scraping

This project demonstrates a simple FastAPI application that performs web scraping on a specific URL and retrieves average data using the BeautifulSoup library.

Prerequisites

Before running the application, ensure that you have the following dependencies installed:

FastAPI
BeautifulSoup
Requests
Installation

Clone the repository:
shell
Copy code
$ git clone <repository_url>
Navigate to the project directory:
shell
Copy code
$ cd fastapi-web-scraping
Install the required dependencies using pip:
shell
Copy code
$ pip install -r requirements.txt
Usage

Start the FastAPI server:
shell
Copy code
$ uvicorn main:app --reload
Open your web browser and access the following URL:
arduino
Copy code
http://localhost:8000/
This will perform web scraping on the provided URL (https://www.metal.com/Lithium-ion-Battery/202303240001) and return the average data along with the assigned heading by Parthvik Ajmera.
To retrieve data from a specific link, append the link ID to the base URL. For example, to retrieve data from "https://example.com", access the following URL:
ruby
Copy code
http://localhost:8000/https://example.com
Ensure that the link starts with "https://" to avoid receiving an error response.
Handling Invalid Links

If an invalid link is provided (i.e., it does not start with "https://"), a 400 Bad Request error will be returned with the message "Invalid link provided."
