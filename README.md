# Todo App - Django

## Description
A simple **Todo App** built using the **Django** web framework. This app allows users to create an account, log in, manage personal tasks, mark them as completed, and delete them. The app leverages Django’s built-in authentication system and ORM to manage user data and tasks.

## Features
- **User Registration and Login**: Users can register and log in to manage their tasks.
- **Add Tasks**: Users can add new tasks to their Todo list.
- **Complete Tasks**: Users can mark tasks as completed. Completed tasks are visually distinguished with a strikethrough and green background.
- **Delete Tasks**: Users can delete tasks from their list.
- **Task Management**: Users can toggle task completion and organize their tasks effectively.

## Requirements
- Python 3.x
- Django 3.x or later

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/todo-app-django.git
    cd todo-app-django
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply the database migrations:
    ```bash
    python manage.py migrate
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Visit the app in your browser at `http://127.0.0.1:8000/`.





## Screenshots
![Screenshot 2025-01-04 153811](https://github.com/user-attachments/assets/0adf7ae1-7b6c-47e4-98f8-f2ca2a0021d8)
![Screenshot 2025-01-04 153754](https://github.com/user-attachments/assets/51ee12ee-dd78-4f1b-9140-96bd09780d18)
![Screenshot 2025-01-04 153729](https://github.com/user-attachments/assets/c7b76d32-fa7a-4546-8765-ddcfc4a80305)

## Usage

1. **Register a new account**: Navigate to the registration page to create an account.
2. **Log in**: Use the credentials created to log in.
3. **Manage Tasks**: Add new tasks, toggle their completion, or delete them.

