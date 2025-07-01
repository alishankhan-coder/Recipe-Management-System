# Recipe Management System 🍳

A comprehensive Django-based web application for managing recipes with full user authentication and CRUD operations.

## Features 🚀

### User Authentication
- **User Registration**: Create new accounts with username, first name, last name, and password
- **User Login**: Secure authentication with username and password
- **User Logout**: Safe session termination
- **Login Protection**: Protected routes requiring authentication for recipe management

### Recipe Management (Full CRUD)
- **Create Recipes**: Add new recipes with name, description, and image upload
- **Read Recipes**: Browse all recipes with search functionality
- **Update Recipes**: Edit existing recipes (name, description, image)
- **Delete Recipes**: Remove recipes with confirmation dialogs

### Additional Features
- **Search Functionality**: Search recipes by name
- **Recipe Details**: Individual recipe pages with full information
- **Image Upload**: Support for recipe images with media handling
- **View Counter**: Track recipe popularity with view counts
- **Responsive Design**: Modern, user-friendly interface
- **Flash Messages**: Success/error notifications for user actions
- **Admin Panel**: Enhanced Django admin with custom display and image previews

## Technology Stack 💻

- **Backend**: Django 5.0.4
- **Database**: SQLite (default)
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Django's built-in authentication system
- **File Upload**: Django's file handling for recipe images
- **Admin Interface**: Custom Django admin with enhanced features

## Project Structure 📁

```
Recipe Site/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── media/                   # Uploaded recipe images
│   └── Recipe_pictures/
├── reciepe/                 # Main project directory
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── reciepe_app/            # Main application
│   ├── models.py           # Recipe model definition
│   ├── views.py            # View functions
│   ├── urls.py             # App URL patterns
│   ├── admin.py            # Admin configuration
│   ├── templates/          # HTML templates
│   │   ├── index.html      # Homepage with recipe list
│   │   ├── login.html      # Login page
│   │   ├── register.html   # Registration page
│   │   ├── details.html    # Recipe details page
│   │   ├── update_recipe.html # Recipe creation/editing
│   │   ├── delete.html     # Recipe deletion confirmation
│   │   └── logout.html     # Logout confirmation
│   └── static/             # Static files
│       ├── css/
│       └── js/
└── static/                 # Collected static files
```

## Installation & Setup 🛠️

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/alishankhan-coder/Recipe-Management-System.git
   cd "Recipe Site"
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   pip install Pillow  # For image handling
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage Guide 📖

### For Users

1. **Registration**: Visit the registration page to create a new account
2. **Login**: Use your credentials to log into the system
3. **Browse Recipes**: View all recipes on the homepage
4. **Search**: Use the search bar to find specific recipes
5. **View Details**: Click on any recipe to see full details
6. **Create Recipe**: (Requires login) Add new recipes with images
7. **Edit Recipe**: (Requires login) Update your existing recipes
8. **Delete Recipe**: (Requires login) Remove recipes with confirmation

### For Administrators

1. **Access Admin Panel**: Login at `/admin/` with superuser credentials
2. **Manage Users**: View and manage user accounts
3. **Manage Recipes**: Advanced recipe management with image previews
4. **View Statistics**: Monitor recipe creation and user activity

## Key Models 🗄️

### Recipe Model
- `recipe_name`: Unique recipe name (max 40 characters)
- `recipe_disc`: Recipe description (text field)
- `recipe_img`: Recipe image upload
- `user`: Foreign key to User model
- `slug`: Auto-generated URL slug
- `recipe_created_at`: Timestamp of creation
- `recipe_view_count`: Number of views

## URL Patterns 🌐

- `/` - Homepage (recipe list)
- `/create/` - Create new recipe (login required)
- `/login/` - User login
- `/register/` - User registration
- `/logout/` - User logout
- `/details/<slug>/` - Recipe details
- `/update_recipe/<slug>/` - Edit recipe (login required)
- `/delete/<slug>/` - Delete confirmation
- `/delete_recipe/<slug>/` - Delete recipe (login required)

## Security Features 🔒

- **CSRF Protection**: Built-in Django CSRF protection
- **Authentication Required**: Protected routes for recipe management
- **User-based Access**: Users can only edit/delete their own recipes
- **Password Validation**: Django's built-in password validators
- **Secure File Upload**: Proper handling of uploaded images

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is open source and available under the [MIT License](LICENSE).

## Contact 📧

- **Developer**: Alishan Khan
- **GitHub**: [@alishankhan-coder](https://github.com/alishankhan-coder)
- **Repository**: [Recipe-Management-System](https://github.com/alishankhan-coder/Recipe-Management-System)

## Screenshots 📸

*Add screenshots of your application here to showcase the UI*

## Future Enhancements 🚀

- Recipe categories and tags
- Recipe rating and reviews
- Favorite recipes functionality
- Recipe sharing via social media
- Advanced search filters
- Email notifications
- Recipe print functionality
- Mobile app development

---

**Happy Cooking! 👨‍🍳👩‍🍳**

