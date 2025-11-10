# Wiki Project

A Wikipedia-like online encyclopedia built with Django. This project allows users to create, edit, and search for encyclopedia entries using Markdown syntax.

## Features

- View encyclopedia entries
- Create new encyclopedia entries
- Edit existing entries
- Search functionality
  - Direct match redirects to entry
  - Partial matches show a list of results
- Random page feature
- Markdown support for entry content

## Technology Stack

- Python
- Django
- Markdown2
- HTML/CSS

## Installation

1. Make sure you have Python installed on your system
2. Clone this repository
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Run the migrations:
   ```
   python manage.py migrate
   ```
   
  **Note:** The database file (`db.sqlite3`) is **not included** in this repository. It will be created when you run the `migrate` command above. If you need to create migrations     for model changes, use:

  ```powershell
  python manage.py makemigrations
  ```
5. Start the development server:
   ```
   python manage.py runserver
   ```

## Project Structure

- `/encyclopedia` - Main application directory
  - `/templates/encyclopedia` - HTML templates
  - `/static/encyclopedia` - Static files (CSS)
  - `views.py` - View functions
  - `util.py` - Utility functions
- `/entries` - Markdown files for encyclopedia entries
- `/wiki` - Project configuration directory

## Usage

- **Home Page**: Lists all available encyclopedia entries
- **Entry Page**: View specific encyclopedia entries
- **Create New Page**: Create a new encyclopedia entry
- **Edit Page**: Modify existing encyclopedia entries
- **Search**: Look up specific entries
- **Random Page**: Navigate to a random encyclopedia entry

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project.

## License

This project is part of CS50's Web Programming with Python and JavaScript course.
