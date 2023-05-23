from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

data = {
    "asin": "testeee",
    "title": "BBABA"
}

class Product(Model):
    __keyspace__ = "scrapper_app"
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()
    price_str = columns.Text(default="-1")

class ProductScrapeEvent(Model): # -> table
    __keyspace__ = "scrapper_app" #
    uuid = columns.UUID(primary_key=True)
    asin = columns.Text(index=True)
    title = columns.Text()
    price_str = columns.Text(default="-100")
    