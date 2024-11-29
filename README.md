# Database connect with MongoDB Atlas
Add in your database connection url in app/routes/database.py


# Blog API with FastAPI and MongoDB

This is a simple blog API built using **FastAPI** and **MongoDB** for storing and managing blog posts. It provides basic CRUD (Create, Read, Update, Delete) operations and allows for data validation using **Pydantic** models.

---

## Features
- Create a new blog post
- Retrieve all blog posts
- Retrieve a specific blog post by ID
- Update a blog post by ID
- Delete a blog post by ID

---

## Requirements

- Python 3.8+
- MongoDB (locally or using a cloud instance like MongoDB Atlas)
- FastAPI
- Uvicorn
- Motor (as the MongoDB driver)

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/blog-api.git
   cd blog-api
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Mac/Linux
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Setup MongoDB:**
   - If you're running MongoDB locally, ensure it is installed and running.
   - If you're using MongoDB Atlas or another cloud instance, update the MongoDB URI in the `app/database.py` file.

---

## Running the Application

To start the FastAPI server, run:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

---

## API Endpoints

### 1. **Create a New Blog Post (POST /blogs/)**

**URL:** `/blogs/`  
**Method:** `POST`  
**Request Body:**

```json
{
  "title": "Blog Post Title",
  "content": "This is the content of the blog post.",
  "author": "Author Name",
  "tags": ["tag1", "tag2"],
  "published": true
}
```

**Response:**

```json
{
  "id": "64b8f2f5d4e6e2b8277c"
}
```

**Description:**  
Creates a new blog post. Returns the ID of the newly created blog.

---

### 2. **Get All Blog Posts (GET /blogs/)**

**URL:** `/blogs/`  
**Method:** `GET`

**Response:**

```json
[
  {
    "id": "64b8f2f5d4e6e2b8277c",
    "title": "Blog Post Title",
    "content": "This is the content of the blog post.",
    "author": "Author Name",
    "tags": ["tag1", "tag2"],
    "published": true
  }
]
```

**Description:**  
Retrieves a list of all blog posts.

---

### 3. **Get a Specific Blog Post (GET /blogs/{blog_id})**

**URL:** `/blogs/{blog_id}`  
**Method:** `GET`  
**Path Parameter:** `blog_id` (string) - The ID of the blog post.

**Response:**

```json
{
  "id": "64b8f2f5d4e6e2b8277c",
  "title": "Blog Post Title",
  "content": "This is the content of the blog post.",
  "author": "Author Name",
  "tags": ["tag1", "tag2"],
  "published": true
}
```

**Description:**  
Retrieves a specific blog post by its ID. Returns a 404 error if the blog is not found.

---

### 4. **Update a Blog Post (PUT /blogs/{blog_id})**

**URL:** `/blogs/{blog_id}`  
**Method:** `PUT`  
**Path Parameter:** `blog_id` (string) - The ID of the blog post.

**Request Body:**

```json
{
  "title": "Updated Blog Post Title",
  "content": "Updated content of the blog post.",
  "author": "Updated Author",
  "tags": ["updated", "tag"],
  "published": false
}
```

**Response:**

```json
{
  "message": "Blog updated successfully"
}
```

**Description:**  
Updates the content of a specific blog post by its ID. Returns a 404 error if the blog post is not found.

---

### 5. **Delete a Blog Post (DELETE /blogs/{blog_id})**

**URL:** `/blogs/{blog_id}`  
**Method:** `DELETE`  
**Path Parameter:** `blog_id` (string) - The ID of the blog post.

**Response:**

```json
{
  "message": "Blog deleted successfully"
}
```

**Description:**  
Deletes a blog post by its ID. Returns a 404 error if the blog post is not found.

---

## Example Requests Using Postman

### **Create Blog (POST)**
- URL: `http://127.0.0.1:8000/blogs/`
- Method: `POST`
- Body: (Raw JSON)
  ```json
  {
    "title": "New Blog",
    "content": "This is the content of the blog.",
    "author": "John Doe",
    "tags": ["tech", "education"],
    "published": true
  }
  ```

### **Update Blog (PUT)**
- URL: `http://127.0.0.1:8000/blogs/{blog_id}`
- Method: `PUT`
- Body: (Raw JSON)
  ```json
  {
    "title": "Updated Blog",
    "content": "Updated content",
    "author": "John Doe",
    "tags": ["education", "tutorial"],
    "published": true
  }
  ```

### **Delete Blog (DELETE)**
- URL: `http://127.0.0.1:8000/blogs/{blog_id}`
- Method: `DELETE`

---

## Troubleshooting

1. **Invalid `blog_id`**: Ensure the `blog_id` provided in the URL is a valid MongoDB ObjectId format.
2. **Database Connection**: Verify that MongoDB is running locally or use a cloud instance like MongoDB Atlas and update the connection string in the `app/database.py` file.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

---

### Instructions:
- Copy all the content above and paste it into your `README.md` file in the root directory of your project.
- Make sure to update the `git clone` URL and MongoDB connection settings as needed.

Now you have a ready-to-use `README.md` with all the details you need to share or deploy your project.
