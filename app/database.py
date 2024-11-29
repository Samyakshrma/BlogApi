from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://username:key@cluster.lipgd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
client = AsyncIOMotorClient(MONGO_URI)
db = client["school_blog"]
