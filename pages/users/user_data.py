from typing import List
from pydantic import BaseModel
from utils.make_data import make_data

class User(BaseModel):
    img: str
    name: str
    email: str
    position: str
    country: str
    status: str

# https://www.convertsimple.com/convert-javascript-to-json/

USERS = [
  {
    "img": "/static/images/users/neil-sims.png",
    "name": "Neil Sims",
    "email": "neil.sims@windster.com",
    "position": "Front-end developer",
    "country": "United States",
    "status": "Active"
  },
  {
    "img": "/static/images/users/roberta-casas.png",
    "name": "Roberta Casas",
    "email": "roberta.casas@windster.com",
    "position": "Designer",
    "country": "Spain",
    "status": "Active"
  },
  {
    "img": "/static/images/users/michael-gough.png",
    "name": "Michael Gough",
    "email": "michael.gough@windster.com",
    "position": "React developer",
    "country": "United Kingdom",
    "status": "Active"
  },
  {
    "img": "/static/images/users/jese-leos.png",
    "name": "Jese Leos",
    "email": "jese.leos@windster.com",
    "position": "Marketing",
    "country": "United States",
    "status": "Active"
  },
  {
    "img": "/static/images/users/bonnie-green.png",
    "name": "Bonnie Green",
    "email": "bonnie.green@windster.com",
    "position": "UI/UX Engineer",
    "country": "Australia",
    "status": "Offline"
  },
  {
    "img": "/static/images/users/thomas-lean.png",
    "name": "Thomas Lean",
    "email": "thomas.lean@windster.com",
    "position": "Vue developer",
    "country": "Germany",
    "status": "Active"
  },
  {
    "img": "/static/images/users/helene-engels.png",
    "name": "Helene Engels",
    "email": "helene.engels@windster.com",
    "position": "Product owner",
    "country": "Canada",
    "status": "Active"
  },
  {
    "img": "/static/images/users/lana-byrd.png",
    "name": "Lana Byrd",
    "email": "lana.byrd@windster.com",
    "position": "Designer",
    "country": "United States",
    "status": "Active"
  },
  {
    "img": "/static/images/users/leslie-livingston.png",
    "name": "Leslie Livingston",
    "email": "leslie.livingston@windster.com",
    "position": "Web developer",
    "country": "France",
    "status": "Offline"
  },
  {
    "img": "/static/images/users/robert-brown.png",
    "name": "Robert Brown",
    "email": "robert.brown@windster.com",
    "position": "Laravel developer",
    "country": "Russia",
    "status": "Active"
  }
]


def make_users(number: int) -> List[User] :
    return make_data(number, USERS, User)
