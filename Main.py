from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()


# @app.get("/")
# async def write_assignment_heading():
    
#     return heading

@app.get("/")
def read_root():
        url = "https://www.metal.com/Lithium-ion-Battery/202303240001"
        heading = " by Parthvik Ajmera"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        avg=soup.find('span','strong___1JlBD priceDown___2TbRQ')
        return {"Lohum Assignment ":heading,"Average:":avg.text}
@app.get("/{link_id}")
async def read_link(link_id: str):
    # Check if the link is valid (e.g., starts with "https://")
    if not link_id.startswith("https://"):
        raise HTTPException(status_code=400, detail="Invalid link provided.")

    # Your logic for handling valid links goes here
    return {"link_id": link_id}
