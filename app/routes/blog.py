from fastapi import APIRouter, HTTPException
from app.database import db
from app.models import BlogPost
from bson import ObjectId

router = APIRouter()

# Utility function to serialize MongoDB documents
def serialize_blog(blog):
    """Convert MongoDB document to a JSON-serializable format."""
    if blog and "_id" in blog:
        blog["_id"] = str(blog["_id"])
    return blog

# POST: Create a new blog
@router.post("/")
async def create_blog(blog: BlogPost):
    result = await db.blogs.insert_one(blog.dict())
    return {"id": str(result.inserted_id)}

# GET: List all blogs
@router.get("/")
async def list_blogs():
    blogs = await db.blogs.find().to_list(100)
    return [serialize_blog(blog) for blog in blogs]

# GET: Get a specific blog by ID
@router.get("/{blog_id}")
async def get_blog(blog_id: str):
    if not ObjectId.is_valid(blog_id):
        raise HTTPException(status_code=400, detail="Invalid blog ID")
    blog = await db.blogs.find_one({"_id": ObjectId(blog_id)})
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return serialize_blog(blog)

# PUT: Update a specific blog by ID
@router.put("/{blog_id}")
async def update_blog(blog_id: str, blog: BlogPost):
    if not ObjectId.is_valid(blog_id):
        raise HTTPException(status_code=400, detail="Invalid blog ID")
    update_result = await db.blogs.update_one(
        {"_id": ObjectId(blog_id)}, {"$set": blog.dict()}
    )
    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"message": "Blog updated successfully"}

# DELETE: Delete a specific blog by ID
@router.delete("/{blog_id}")
async def delete_blog(blog_id: str):
    if not ObjectId.is_valid(blog_id):
        raise HTTPException(status_code=400, detail="Invalid blog ID")
    delete_result = await db.blogs.delete_one({"_id": ObjectId(blog_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"message": "Blog deleted successfully"}
