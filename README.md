# YouCanWrite

## Introduction

Welcome to YouCanWrite, a dynamic platform designed to inspire and support writers at every stage of their creative journey. Whether you're an aspiring novelist, a seasoned author, or someone who enjoys writing as a hobby, YouCanWrite offers a range of features to help you improve your writing skills, connect with other writers, and stay motivated through daily challenges and tips.

At its core, YouCanWrite aims to address common challenges faced by writers, such as writer's block and lack of feedback. By providing a supportive community and a variety of writing prompts, YouCanWrite ensures that writers always have a source of inspiration and a space to share their work.

**This project combines a robust backend with a user-friendly frontend to deliver a seamless writing experience:**
Backend: The application is powered by Flask, a lightweight WSGI web application framework in Python. Flask is used to handle the application's routing, request processing, and integration with the database.
Database: We use PostgreSQL for robust and scalable data storage. This relational database system is known for its reliability and performance.
Frontend: The user interface is built using HTML, CSS, and JavaScript, with Tailwind CSS providing a utility-first approach to styling. This ensures a responsive and visually appealing design.
Daily Writing Tips and Challenges: Gemini is utilized for generating daily writing tips and challenge prompts, offering users fresh and engaging content every day.

- **Landing Page:** [Landing Page URL](https://hiba-emording.github.io/youcanwrite-landing/)
- **Blog Article:** [Blog Article](https://)

## Installation

To run the YouCanWrite project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/hiba-emording/YouCanWrite
   cd YouCanWrite
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your PostgreSQL database.

4. Configure environment variables.

5. Run the application:
   ```bash
   flask run
   ```

## Usage

Once the application is running, open your web browser and navigate to `http://localhost:5000` to access YouCanWrite.

Here are some key features:
- View posts sorted by likes or dates.
- Create, edit, and delete posts and comments.
- Participate in daily writing challenges.
- Get daily writing Tips.
- Customize user profile.

## Contributing

Contributions to improve YouCanWrite are gladly welcomed!
To contribute:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -am 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.
