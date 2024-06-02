# Movie Library Project

## Project Overview

The Movie Library is a web application that allows users to create and manage lists of movies. Users can view random movies on the homepage, create new movie lists, and see details of individual movies by clicking on their posters.

## Features

- **User Authentication**: Users can log in and log out.
- **Movie Lists**: Users can create and manage their own movie lists.
- **Random Movie Carousel**: The homepage features a carousel of random movies fetched from an external API.
- **Movie Details**: Clicking on a movie poster in the carousel redirects the user to a detailed view of that movie.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **HTML/CSS**: For structuring and styling the web pages.
- **Swiper.js**: For creating the movie carousel.
- **OMDb API**: The Movie Database API for fetching movie data.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/movie-library.git
   ```

2. **Navigate to the project directory**:
   ```sh
   cd movie-library
   ```

3. **Create a virtual environment**:
   ```sh
   python3 -m venv venv
   ```

4. **Activate the virtual environment**:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

5. **Install the dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

6. **Set up environment variables**:
    Copy the `example.env` file to a new file named `.env` and then edit it to include the necessary environment variables:
    ```sh
    cp example.env .env
    ```

7. **Run the application**:
   ```sh
   flask run
   ```

8. Open your web browser and navigate to `http://localhost:5000`.


## Detailed Description of Code

### app.py

- **Imports**: Imports necessary libraries and modules.
- **API Configuration**: Sets up the OMDb API URL and key.
- **Flask Routes**:
  - **Home Route**: Fetches random movies and displays them on the homepage.
  - **Movie Details Route**: Fetches and displays details of a selected movie.
  - **Create List Route**: Handles the creation of new movie lists with server-side validation.

### templates/home.html

- **Navigation Bar**: Includes links to the home page and logout, and a dark mode toggle switch.
- **Welcome Message**: Displays a welcome message.
- **Movie Lists Section**: Shows the user's movie lists.
- **Create New List Form**: Allows the user to create a new movie list with client-side validation.
- **Random Movie Carousel**: Displays random movies in a Swiper.js carousel.

### static/styles.css

- **Styling**: Contains the CSS for the entire application, including the dark mode styles.

### Client-Side Validation

- **JavaScript**: Ensures that the new list title is not empty before submitting the form.

### Server-Side Validation

- **Flask**: Checks that the new list title is not empty to prevent submission of invalid data.

## Future Scope

1. **User Registration**: Implement a user registration system to allow new users to sign up.
2. **Enhanced Movie Search**: Add a search functionality to allow users to search for movies by title, genre, or other criteria.
3. **Favorite Movies**: Allow users to mark movies as favorites and view a list of their favorite movies.
4. **Improved UI/UX**: Enhance the user interface and experience with more interactive elements and animations.
5. **Mobile Responsiveness**: Improve the mobile responsiveness of the application.
6. **Recommendations**: Implement a movie recommendation system based on user preferences and watch history.
7. **Social Sharing**: Allow users to share their movie lists on social media platforms.
