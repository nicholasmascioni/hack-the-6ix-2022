
from bs4 import BeautifulSoup
import requests


no_frills_database = { 
    "price_match": True,
    "butter": 2.05,
    "white sugar": 8.99,
    "brown sugar": 8.99,
    "eggs": 8.99,
    "vanilla extract": 8.99,
    "baking soda": 8.99,
    "salt": 8.99,
    "all-purpose flour": 8.99,
    "white sugar": 8.99,
    "semisweet chocolate chips": 8.99,
    "chopped walnuts": 8.99
}

walmart_database = { 
    "price_match": True,
    "butter": 2.05,
    "white sugar": 8.99,
    "brown sugar": 8.99,
    "eggs": 8.99,
    "vanilla extract": 8.99,
    "baking soda": 8.99,
    "salt": 8.99,
    "all-purpose flour": 8.99,
    "white sugar": 8.99,
    "semisweet chocolate chips": 8.99,
    "chopped walnuts": 8.99
}
freshco_database = { 
    "price_match": True,
    "butter": 2.05,
    "white sugar": 8.99,
    "brown sugar": 8.99,
    "eggs": 8.99,
    "vanilla extract": 8.99,
    "baking soda": 8.99,
    "salt": 8.99,
    "all-purpose flour": 8.99,
    "white sugar": 8.99,
    "semisweet chocolate chips": 8.99,
    "chopped walnuts": 8.99
}
t_and_t_database = { 
    "price_match": False,
    "butter": 2.05,
    "white sugar": 8.99,
    "brown sugar": 8.99,
    "eggs": 8.99,
    "vanilla extract": 8.99,
    "baking soda": 8.99,
    "salt": 8.99,
    "all-purpose flour": 8.99,
    "white sugar": 8.99,
    "semisweet chocolate chips": 8.99,
    "chopped walnuts": 8.99
}