HEAD
# Final-Project-ALX

# MealMaster - Backend skeleton

## Quick start

1. Create virtualenv:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # or .venv\\Scripts\\activate on Windows
   43675e4 (add accounts recipes mealplans shopping)
MealMaster - Your Meal Planning Assistant

MealMaster is a robust web application designed to simplify meal planning, recipe management, and grocery lists. It offers a user-friendly interface to organize your eating habits, discover new recipes, and optimize your culinary experience.

Key Features

•
User Account Management: Registration, login, and profile management with personalized information such as date of birth, profile photo, and bio.

•
Meal Management: Create, modify, and delete meals with details such as name, description, category, and ingredients.

•
Meal Planning: Organize your meals over a given period for efficient planning.

•
Recipe Management: Add and manage your favorite recipes with detailed ingredients and instructions.

•
Shopping Lists: Automatically generate shopping lists based on your planned meals and recipes.

•
RESTful API: All functionalities are exposed via a RESTful API, allowing easy integration with other applications.

•
JWT Authentication: Secure API endpoints with JWT tokens for robust authentication.

•
API Documentation: Interactive API documentation via Swagger/OpenAPI to facilitate integration and development.

Technologies Used

•
Backend: Django, Django REST Framework

•
Database: SQLite (default, configurable for PostgreSQL, MySQL, etc.)

•
Authentication: Django REST Framework Simple JWT

•
API Documentation: drf-spectacular, drf-yasg

•
Dependency Management: requirements.txt

Project Structure

The project is organized into several Django applications, each managing a specific aspect of the application:

•
accounts/: Manages custom user models and authentication.

•
meals/: Manages meal models and their categories.

•
mealplans/: Manages meal planning.

•
recipes/: Manages recipes and their ingredients.

•
shopping/: Manages shopping lists.

•
mealmaster/: The main Django project directory, containing global settings, URLs, and main views.

Installation and Setup

Follow these steps to set up and run the project locally:

Prerequisites

•
Python 3.x

•
pip (Python package manager)

Installation Steps

1.
Clone the repository:

2.
Create a virtual environment (recommended):

3.
Install dependencies:

4.
Apply database migrations:

5.
Create a superuser (to access the Django admin interface):

6.
Start the development server:

API Usage

The API is accessible via the following endpoints:

•
Swagger UI Documentation: http://127.0.0.1:8000/api/docs/

•
ReDoc Documentation: http://127.0.0.1:8000/redoc/

Key Endpoints

•
/api/token/: Obtain a JWT access token.

•
/api/token/refresh/: Refresh a JWT access token.

•
/api/accounts/: Manage user accounts.

•
/api/meals/: Manage meals.

•
/api/recipes/: Manage recipes.

•
/api/mealplans/: Manage meal plans.

•
/api/shopping/: Manage shopping lists.

For more details on requests and responses, please refer to the API documentation.

