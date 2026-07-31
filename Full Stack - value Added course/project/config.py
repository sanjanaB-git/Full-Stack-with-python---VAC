from pymongo import MongoClient

# Connect to MongoDB Local Server
client = MongoClient("mongodb://localhost:27017/")

# Create / Connect to Database
db = client["HelpDeskTicketingSystem"]

# Create / Connect to Collection
tickets_collection = db["tickets"]