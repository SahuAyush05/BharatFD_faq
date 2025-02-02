# Multilingual FAQ API

This is a Django-based REST API for managing Frequently Asked Questions (FAQs) with multilingual support. The API allows storing and retrieving FAQs in multiple languages, supports language selection via query parameters, and efficiently caches translations.

---

## Features
- Store FAQs with multilingual support.
- Retrieve FAQs in a specific language using `?lang=` query parameter.
- WYSIWYG editor for rich-text answers (using `django-ckeditor`).
- Automatic translation using Google Translate API.
- Redis caching for optimized performance.
- REST API endpoints for CRUD operations.
- Docker support for easy deployment.

---

## Installation Steps

### 1. Clone the Repository
```sh
git clone https://github.com/your-repo/multilingual-faq.git
cd multilingual-faq
```

### 2. Create and Activate Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file and configure the following:
```
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://localhost:6379/0
```

### 5. Run Database Migrations
```sh
python manage.py migrate
```

### 6. Start Redis Server (for caching)
```sh
redis-server
```

### 7. Start the Development Server
```sh
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000/api/faqs/`.

---

## API Usage

### 1. Get All FAQs (default in English)
```http
GET /api/faqs/
```
#### Response:
```json
[
    {
        "id": 1,
        "question": "What is Django?",
        "answer": "Django is a Python web framework."
    }
]
```

### 2. Get FAQs in a Specific Language
```http
GET /api/faqs/?lang=hi  # Hindi
GET /api/faqs/?lang=bn  # Bengali
```
#### Response:
```json
[
    {
        "id": 1,
        "question": "डिजैंगो क्या है?",
        "answer": "डिजैंगो एक पायथन वेब फ्रेमवर्क है।"
    }
]
```

### 3. Create a New FAQ
```http
POST /api/faqs/
Content-Type: application/json
```
#### Request Body:
```json
{
    "question": "What is REST API?",
    "answer": "REST API allows communication over HTTP."
}
```

### 4. Update an FAQ
```http
PUT /api/faqs/1/
Content-Type: application/json
```
#### Request Body:
```json
{
    "question": "What is a REST API?",
    "answer": "A REST API allows applications to communicate over HTTP."
}
```

### 5. Delete an FAQ
```http
DELETE /api/faqs/1/
```

---

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch for your feature:
   ```sh
   git checkout -b feature-new-feature
   ```
3. Make your changes and commit:
   ```sh
   git commit -m "feat: Add support for Spanish translations"
   ```
4. Push the changes:
   ```sh
   git push origin feature-new-feature
   ```
5. Open a Pull Request.

---

## Code Formatting
- Follow PEP8 guidelines.
- Use `flake8` for linting:
  ```sh
  flake8 .
  ```
- Write unit tests using `pytest` or Django’s built-in `unittest`.

---

## Docker Setup

### 1. Build and Run the Application
```sh
docker-compose up --build
```

### 2. Run Migrations Inside the Container
```sh
docker-compose exec web python manage.py migrate
```

---

## Deployment (Optional)
You can deploy this application to **Heroku** or **AWS** using Docker. Configure the necessary environment variables before deployment.

---

## License
This project is licensed under the MIT License.

---

## Contact
For any issues or suggestions, feel free to create an issue or reach out at [your-email@example.com](mailto:your-email@example.com).

