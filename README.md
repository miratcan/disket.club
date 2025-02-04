# disket.club

Prototip
disket.club is a web application that allows users to upload and share browser-based apps, demos, or games that do not exceed the size of a floppy disk. The platform supports multiple categories such as games, apps, tools, and others.

### Features

- **User Authentication**: Users can sign up, log in, and manage their profiles.
- **Upload and Share**: Users can upload their projects and share them with others.
- **Categorization**: Projects can be categorized into games, apps, tools, and others.
- **Localization**: The application supports multiple languages, including English and Turkish.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/disket.club.git
   cd disket.club
   ```

2. Install the dependencies:

   ```bash
   poetry install
   ```

3. Apply migrations:

   ```bash
   poetry run python manage.py migrate
   ```

4. Create a superuser:

   ```bash
   poetry run python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   poetry run python manage.py runserver

   ```

6. Access the application at `http://127.0.0.1:8000/`.

### Usage

- **Homepage**: The homepage displays a list of available projects categorized into games, apps, tools, and others.
- **Upload**: Authenticated users can upload their projects using the upload page.
- **Profile**: Users can view and edit their profiles.
- **Localization**: Users can switch between supported languages (English and Turkish).

### Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Description of your changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Create a pull request.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgements

- Django: The web framework used for this project.
- Poedit: Used for localization.
- All contributors and users for their support and feedback.
