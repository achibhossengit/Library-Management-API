# Library Management System

## Overview
The Library Management System is a comprehensive RESTful API designed to facilitate the management of library resources, including books, authors, categories, and borrowing records. Built using Django Rest Framework (DRF), this project provides robust functionality with fine-grained permission control and efficient data handling.

## Features
- **Book Management**: CRUD operations for books.
- **Category Management**: Manage book categories.
- **Author Management**: CRUD operations for authors and their associated books.
- **Borrowing System**: Manage borrowing and returning of books with user-specific access.
- **User Roles**:
  - Admin: Full access to all resources.
  - Librarian: Full access to manage resources.
  - Member: Limited to personal borrowing records and read-only access to library resources.
- **Authentication**: Secure access control using JWT token-based authentication.
- **API Documentation**: Interactive API documentation provided via Swagger.

## Technology Stack
- **Backend**: Django Rest Framework (DRF)
- **Authentication**: JWT Token based Authentication System
- **API Documentation**: Swagger (via `drf-yasg`)
- **Database**: SQLite (default, replaceable with PostgreSQL, MySQL, etc.)

## Endpoints
### Books
- `GET /books/`: List all books.
- `POST /books/`: Add a new book.
- `GET /books/{id}/`: Retrieve book details by ID.
- `PUT /books/{id}/`: Update book details.
- `DELETE /books/{id}/`: Delete a book.

### Categories
- `GET /categories/`: List all categories.
- `POST /categories/`: Add a new category.
- `GET /categories/{id}/`: Retrieve category details by ID.
- `PUT /categories/{id}/`: Update category details.
- `DELETE /categories/{id}/`: Delete a category.

### Authors
- `GET /authors/`: List all authors.
- `POST /authors/`: Add a new author.
- `GET /authors/{id}/`: Retrieve author details by ID.
- `PUT /authors/{id}/`: Update author details.
- `DELETE /authors/{id}/`: Delete an author.
- `GET /authors/{author_pk}/books/`: List books by a specific author.

### Borrow Records
- `GET /borrows/`: View borrowing records (filtered by user permissions).
- `POST /borrows/`: Create a new borrowing record.
- `PUT /borrows/{id}/`: Update a borrowing record (e.g., returning a book).
- `DELETE /borrows/{id}/`: Delete a borrowing record.

### Members
- `GET /members/`: View library members (Admins/Librarians only).

## Installation
### Prerequisites
- Python 3.9+
- pip (Python package manager)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/achibhossengit/Library-Management-API
   cd Library_manager
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Accessing the Application
- **API Root**: `http://127.0.0.1:8000/`
- **Swagger Documentation**: `http://127.0.0.1:8000/swagger/`

## Usage
### Permissions
- **Admins**: Full access to all endpoints.
- **Librarians**: Similar to admins but without user management.
- **Members**: Read-only access to books and categories, and manage their own borrowing records.

## Contribution Guidelines
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Create a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any queries or issues, please contact:
- **Developer**: Achib Hossen
- **Email**: [mail.achibhossen@gmail.com](mailto:mail.achibhossen@gmail.com)

