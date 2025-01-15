# Pythonando Project: URL Shortener

This is a URL shortener project built with Django and Django Ninja. It allows users to create short URLs that redirect to longer URLs, track clicks, and generate QR codes for the short URLs.

## Features

- Create short URLs with optional custom tokens
- Redirect to the original URL using the short URL
- Track unique and total clicks
- Generate QR codes for short URLs
- API endpoints for managing short URLs

## Project Structure


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/url-shortener.git
    cd url-shortener
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install django
    pip install pillow
    pip install django-ninja
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

## API Endpoints

- `POST /api/` - Create a new short URL
- `GET /api/{token}` - Redirect to the original URL
- `PUT /api/{link_id}` - Update an existing short URL
- `GET /api/statistics/{link_id}/` - Get statistics for a short URL
- `GET /api/qrcode/{link_id}/` - Get a QR code for a short URL

## Configuration

- The project settings are located in [settings.py](http://_vscodecontentref_/20).
- The API routes are defined in [api.py](http://_vscodecontentref_/21) and registered in [api.py](http://_vscodecontentref_/22).

## Usage

- Navigate to `http://127.0.0.1:8000/` to view the home page.
- Use the navigation bar to access different sections of the diary.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Acknowledgements

- Developed by [@nichollasj](https://github.com/josephcavalcante)


## About Pythonando

**Pythonando** is an educational platform dedicated to training developers to become Python specialists, enabling them to create robust and scalable web applications. The platform offers comprehensive courses, such as Python Full, covering everything from programming fundamentals to advanced topics in Python and Django.

### Pythonando Resources
- **Meetings with Professors**: Schedule one-on-one sessions to clarify doubts.
- **Code Reviews**: Evaluate students' projects, highlighting strengths and areas for improvement.
- **Student Events**: Practical activities simulating real-world work experiences, such as coding challenges and hackathons.

### Online Presence
- [YouTube](#)
- [Instagram](#)
- [GitHub](#)
- [Facebook](#)
- [Official Website](#)


