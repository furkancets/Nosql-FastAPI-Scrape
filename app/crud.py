#from .db import get_session
import uuid
from .models import Product, ProductScrapeEvent
#from cassandra.cqlengine.management import sync_table
import copy

#session = get_session()

#sync_table(Product)
#sync_table(ProductScrapeEvent)

def create_entry(data:dict):
    return Product.create(**data)
    
def create_scrape_entry(data:dict):
    data['uuid'] = uuid.uuid1()
    return ProductScrapeEvent.create(**data)

def add_scrape_event(data:dict, fresh=False):
    if fresh:
        data = copy.deepcopy(data)
    product = create_entry(data)
    scrape_obj = create_scrape_entry(data)
    return product, scrape_obj
