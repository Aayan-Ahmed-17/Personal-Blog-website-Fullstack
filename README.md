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


## Deploy FastAPI Backend on Railway

### Prerequisites

- A [Railway](https://railway.com/) account (GitHub login recommended).
- A MongoDB Atlas cluster and database user credentials.
- Your backend code pushed to GitHub.

> **Free plan note (as of April 15, 2026):** Railway pricing and trial/free allowances can change. Check your Railway dashboard pricing page before deploying.

### One-time project prep

This repository now includes:

- `railway.json` with a production start command (`uvicorn app.main:app --host 0.0.0.0 --port $PORT`) and healthcheck path `/health`.
- `.env.example` showing required environment variables.

### Steps to deploy

1. **Push your latest code to GitHub**
   ```bash
   git add .
   git commit -m "Prepare Railway deployment"
   git push
   ```

2. **Create a new Railway project**
   - Go to Railway dashboard.
   - Click **New Project** → **Deploy from GitHub repo**.
   - Select this repository.

3. **Set environment variables in Railway**
   In your Railway service, open **Variables** and add:

   - `USERNAME` = your Atlas DB username
   - `PASSWORD` = your Atlas DB password
   - `DB_NAME` = `blog_fullstack` (or your preferred DB name)
   - `URL` = any URL you want the scraper route to use

4. **Deploy**
   - Railway auto-builds with Nixpacks and runs the start command from `railway.json`.
   - Wait until deployment status is **Success**.

5. **Verify health**
   Open:
   - `https://<your-railway-domain>/health`
   - `https://<your-railway-domain>/docs`

6. **Attach a custom domain (optional)**
   - Service → **Settings** → **Domains** → add custom domain and update DNS records.

### Common issues and fixes

- **App crashes on startup with env error**
  - Ensure `USERNAME` and `PASSWORD` are set exactly (uppercase).
- **Mongo connection/auth error**
  - Confirm Atlas user has proper permissions and password is correct.
  - Ensure Atlas network access allows connections from anywhere (`0.0.0.0/0`) or Railway egress range as needed.
- **Build succeeds but app not reachable**
  - Confirm service uses port from `$PORT` (already configured in `railway.json`).

### Recommended next steps

- Add a stricter CORS allowlist for production instead of `"*"`.
- Add structured logging and request metrics.
- Set up separate Railway environments (staging/production).

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
