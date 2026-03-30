# Personal-Blog-website-Fullstack

This is a fullstack blog website built with FastAPI, MongoDB, and web scraping capabilities using Requests and Beautiful Soup. The project is for educational purposes to practice backend development with FastAPI and MongoDB integration, as well as web scraping techniques.

## Features

- **Blog Management**: Create, read, update, and delete blog posts.
- **Web Scraping**: Scrape blog articles from external sources.
- **MongoDB Integration**: Persistent storage for blog data.
- **FastAPI**: Modern, fast web framework for building APIs.

## Tech Stack

- **Backend**: FastAPI
- **Database**: MongoDB (Atlas)
- **Web Scraping**: Requests, Beautiful Soup
- **Environment**: Python 3.8+

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Personal-Blog-website-Fullstack
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with:
   ```
   USERNAME=your_mongodb_username
   PASSWORD=your_mongodb_password
   DB_NAME=blog_fullstack
   URL=https://example.com/blog  # URL to scrape
   ```

5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

6. Access the API documentation at `http://localhost:8000/docs`

## API Endpoints

### Blogs
- `GET /api/v1/` - Health check
- `GET /api/v1/health` - Health check
- `POST /api/v1/blogs/` - Create a new blog post
- `GET /api/v1/blogs/` - Get all blog posts
- `GET /api/v1/blogs/{id}` - Get a specific blog post
- `PUT /api/v1/blogs/{id}` - Update a blog post
- `DELETE /api/v1/blogs/{id}` - Delete a blog post

### Scraped Data
- `GET /api/v1/scraped/` - Get scraped blog articles

## Improvements Made

- Added proper error handling with HTTP status codes
- Implemented delete functionality for blogs
- Fixed endpoint naming and response consistency
- Added validation for blog IDs
- Improved scraper error handling
- Corrected schema naming from user to blog
- Enhanced README with setup instructions and API documentation
