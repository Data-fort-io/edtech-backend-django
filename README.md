# Dataforte Hub

**Tagline:** *"One-stop platform for all your academic needs"*

---

## Overview

Dataforte Hub is a comprehensive platform designed to streamline academic activities for students and educators. It provides a centralized hub for managing courses, accessing resources, and enhancing the learning experience.

---

## Core Features

1. **Course Dashboard**  
    - Display all available courses with filters for searching and categorization.

2. **Course Resources**  
    - Store and provide access to course materials, such as:  
      - Documents (PDF, Word, etc.)  
      - Videos (recorded classes or tutorials)  
      - Links to external resources  

3. **Course Outline**  
    - Display detailed course outlines, including:  
      - Module descriptions  
      - Learning objectives  
      - Assessment details  

4. **Class Recordings**  
    - Store and provide access to recorded classes, with features like:  
      - Video playback  
      - Timestamps for easy navigation  
      - Search functionality  

5. **User Profile**  
    - Allow students to create profiles, with features like:  
      - Course enrollment management  
      - Personalized dashboard  
      - Notification preferences  

6. **Notification System**  
    - Send notifications to students about:  
      - New course resources  
      - Upcoming classes or deadlines  
      - Changes to course schedules  

---

## Nice-to-Have Features

1. **Discussion Forum**  
    - Integrate a discussion forum for students to ask questions, share resources, and collaborate.

2. **Assignment Submission**  
    - Allow students to submit assignments through the platform, with features like file uploads and grading.

3. **Grade Tracking**  
    - Provide students with access to their grades, with features like grade history and analytics.

4. **Mobile App**  
    - Develop a mobile app for on-the-go access to the platform.

---

## Technical Requirements

1. **Front-end**  
    - Build the user interface using HTML, CSS, and JavaScript, with frameworks like React or Angular.

2. **Back-end**  
    - Use Django, a Python-based web framework, to handle server-side logic and APIs.

3. **Database**  
    - Design a database schema to store course resources, user data, and other relevant information, using databases like MySQL or PostgreSQL.

4. **Authentication**  
    - Implement authentication and authorization using Django's built-in authentication system or third-party libraries like OAuth.

---

## Getting Started

### Prerequisites
- Python 3.x
- Django
-Nest.js
- PostgreSQL or MySQL
- (for front-end development)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/dataforte-hub.git
    ```
2. Navigate to the project directory:
    ```bash
    cd dataforte-hub
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up the database:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Run the development server:
    ```bash
    python manage.py runserver
    ```

---

## Contribution Guidelines

1. Clone the repo.
2. Open your terminal & set the origin
   branch
3. Pull origin `git pull origin dev`
4. Create a new branch for the task you were assigned to,
5. After making changes, do `git add .`
6. Commit your changes with a descriptive commit message : `git commit -m "your commit message"`.
7. To make sure there are no conflicts, run `git pull origin main`.
8. Push changes to your new branch, run `git push -u origin your created new branch`.
9. Create a pull request to the `dev` branch not `main`.
10. Ensure to describe your pull request.
11. If you've added code that should be tested, add some test examples.


> _Sample Commit Messages_

- `chore: Updated README file`:= `chore` is used because the commit didn't make any changes to the
  backend or test folders in any way.
- `feat: Added plugin info endpoints`:= `feat` is used here because the feature was non-existent
  before the commit.

