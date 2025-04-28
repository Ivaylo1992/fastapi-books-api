# 📚 FastAPI Books API

A simple, lightweight REST API for managing a collection of books — built using **FastAPI**.

---

## 🚀 Features

- Create, retrieve, update, and delete books
- Fully documented automatic OpenAPI (Swagger UI)
- Fast performance using ASGI server
- Clean Python code structure

---

## 🛠️ Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) — modern, fast (high-performance) web framework for APIs
- [Uvicorn](https://www.uvicorn.org/) — lightning-fast ASGI server
- [Pydantic](https://docs.pydantic.dev/latest/) — data validation and settings management
- [Python 3.8+](https://www.python.org/)

---

## 📂 Project Structure

```bash
fastapi-books-api/
├── main.py           # Main entry point
├── models.py         # Pydantic models (schemas)
├── routers/          
│   └── book_router.py  # API endpoints for books
├── database.py       # Fake in-memory database
└── requirements.txt  # Python dependencies
```

---

## ⚡ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Ivaylo1992/fastapi-books-api.git
cd fastapi-books-api
```

## 2 Install Dependencies
It's recommended to use a virtual environment:
``` bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 3 Run the Server
``` bash
uvicorn main:app --reload
```

The app will be available at: http://127.0.0.1:8000

### 4. Explore the API Docs

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📖 Example API Endpoints

| Method | Endpoint         | Description                |
|--------|------------------|-----------------------------|
| GET    | `/books/`         | Retrieve all books          |
| POST   | `/books/`         | Create a new book           |
| GET    | `/books/{id}`     | Retrieve a specific book    |
| PUT    | `/books/{id}`     | Update a book               |
| DELETE | `/books/{id}`     | Delete a book               |

### 📦 Example Book JSON Structure

```json
{
  "id": "uuid",
  "title": "Book Title",
  "author": "Author Name",
  "description": "Short description",
  "rating": 5
}
```

## 📦 Requirements

- Python 3.8 or newer
- FastAPI
- Uvicorn
- Pydantic

You can install all dependencies by running:

```bash
pip install -r requirements.txt
```

## 💬 License

This project is licensed under the [MIT License](LICENSE).

## 🤝 Contributions

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate for any changes made.



