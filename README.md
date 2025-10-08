Django To-Do List Application
A simple, elegant web application built with Django that helps you manage your daily tasks. Add new to-do items and keep track of what needs to be done.

📋 Table of Contents

Features

Screenshots

Prerequisites

Installation

Usage

Future Enhancements

Contact

✨ Features

Add Tasks: Quickly add new to-do items to your list
View Tasks: See all your pending tasks in one place
Clean UI: Simple and intuitive user interface
Persistent Storage: All tasks are saved in a SQLite database
Responsive Design: Works well on desktop and mobile devices
Timestamp Tracking: Automatically records when each task was created

🔧 Prerequisites

Before you begin, ensure you have the following installed on your system:

Python 3.8 or higher - Download Python
pip (Python package installer) - Usually comes with Python
Git (optional, for cloning the repository) - Download Git

🚀 Installation
Follow these steps to get your development environment set up:
1. Clone the Repository
git clone https://github.com/yourusername/django-todo-list.git
cd django-todo-list
BASH
Or download the ZIP file and extract it.
2. Create a Virtual Environment (Recommended)
Windows:
python -m venv venv
venv\Scripts\activate
BASH
macOS/Linux:
python3 -m venv venv
source venv/bin/activate
BASH
3. Install Dependencies
pip install django
BASH
If you have a requirements.txt file:
pip install -r requirements.txt
BASH
4. Apply Database Migrations
python manage.py migrate
BASH
5. (Optional) Create a Superuser
To access the Django admin panel:
python manage.py createsuperuser
BASH
Follow the prompts to set up your admin account.
6. Run the Development Server
python manage.py runserver
BASH
7. Access the Application
Open your web browser and navigate to:
http://127.0.0.1:8000/
CPP
To access the admin panel (if you created a superuser):
http://127.0.0.1:8000/admin/
BASH
📖 Usage
Adding a Task
On the home page, you'll see an input field at the top
Type your task description in the text box
Click the "Add" button or press Enter
📸 Screenshots
<img width="1919" height="1017" alt="Screenshot 2025-10-08 124939" src="https://github.com/user-attachments/assets/41939010-ae24-4bb4-854e-7065f16c149c" />
🔮 Future Enhancements
Here are some features planned for future versions:

 Mark as Complete: Add ability to mark tasks as done
 Delete Tasks: Remove tasks from the list
 Edit Tasks: Modify existing task descriptions
 Due Dates: Add deadlines to tasks
 Categories: Organize tasks into different categories
 Priority Levels: Mark tasks as high, medium, or low priority
 Search Functionality: Search through your tasks
 User Authentication: Multiple users with separate task lists
 Export/Import: Save and load task lists
 Dark Mode: Toggle between light and dark themes
 📧 Contact
Vaishnavi Ayyappan- vaishnaviayyappan16@gmail.com

Project Link: https://github.com/Vaishnaviayyappan/Personal-To-do-app
🐛 Troubleshooting
Common Issues
Issue: ModuleNotFoundError: No module named 'django'

Solution: Make sure you've activated your virtual environment and installed Django
pip install django
BASH
Issue: favicon.ico not appearing

Solution: Clear your browser cache (Ctrl+Shift+R or Cmd+Shift+R) and ensure the favicon file is in the correct directory (todo/static/todo/favicon.ico)
Issue: Database errors after making changes to models

Solution: Run migrations
python manage.py makemigrations
python manage.py migrate
BASH
Issue: Port 8000 already in use

Solution: Use a different port
python manage.py runserver 8080
🙏 Acknowledgments
Thanks to the Django community for excellent documentation
Inspired by various to-do list applications
Built as a learning project for understanding Django fundamentals
Made with ❤️ using Django
