
from bs4 import BeautifulSoup
import requests


no_frills_database = { 
    "price_match": True,
    "butter": 5.98,
    "white sugar": 4.89,
    "brown sugar": 3.29,
    "eggs": 3.59,
    "vanilla extract": 4.79,
    "baking soda": 1.69,
    "salt": 1.29,
    "all-purpose flour": 5.99,
    "semisweet chocolate chips": 3.79,
    "chopped walnuts": 3.29
}

walmart_database = { 
    "price_match": True,
    "butter": 5.98,
    "white sugar": 7.48,
    "brown sugar": 2.49,
    "eggs": 5.98,
    "vanilla extract": 5.84,
    "baking soda": 0.72,
    "salt": 1.17,
    "all-purpose flour": 3.97,
    "semisweet chocolate chips": 8.97,
    "chopped walnuts": 2.97
}
freshco_database = { 
    "price_match": True,
    "butter": 8.99,
    "white sugar": 8.99,
    "brown sugar": 8.99,
    "eggs": 8.99,
    "vanilla extract": 8.99,
    "baking soda": 8.99,
    "salt": 8.99,
    "all-purpose flour": 8.99,
    "semisweet chocolate chips": 8.99,
    "chopped walnuts": 8.99
}
t_and_t_database = { 
    "price_match": False,
    "butter": 8.24,
    "white sugar": 3.49,
    "brown sugar": 4.17,
    "eggs": 4.72,
    "vanilla extract": 8.99,
    "baking soda": 4.39,
    "salt": 1.59,
    "all-purpose flour": 7.69,
    "semisweet chocolate chips": 8.99,
    "chopped walnuts": 9.98
}