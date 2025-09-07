# RojgarPatra - Resume Builder App

A Django-based resume builder application that allows users to create, manage, and export professional resumes as PDFs.

## Features

- User registration and authentication with email verification
- Dynamic resume builder with customizable sections
- PDF export functionality
- User dashboard for managing multiple resumes
- Responsive design with TailwindCSS

## Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/sudip6164/rojgarpatra.git
   cd rojgarpatra
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**
   Create a `.env` file in the root directory:
   ```
   # Generate a new secret key
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   
   SECRET_KEY=your-secret-key-here
   DEBUG=True

   # For Gmail:
   # 1. Enable 2-factor authentication on your Google account
   # 2. Generate an App Password: https://myaccount.google.com/apppasswords
   # 3. Update .env file with your email and app password
   
   EMAIL_HOST_USER=your-gmail@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   DEFAULT_FROM_EMAIL=noreply@rojgarpatra.com
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

## Environment Variables

- `SECRET_KEY`: Django secret key for security
- `DEBUG`: Set to False in production
- `EMAIL_HOST_USER`: Gmail address for sending emails
- `EMAIL_HOST_PASSWORD`: Gmail app password
- `DEFAULT_FROM_EMAIL`: Default sender email address

## Project Structure

```
rojgarpatra/
├── rojgarpatra/          # Main project settings
├── accounts/             # User authentication app
├── resumes/              # Resume management app
├── core/                 # Core pages and dashboard
├── templates/            # HTML templates
├── static/               # Static files (CSS, JS, images)
└── requirements.txt      # Python dependencies
```

## License

This project is licensed under the MIT License.
