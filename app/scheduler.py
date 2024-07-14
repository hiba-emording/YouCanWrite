#!/usr/bin/python3
from app import db
from app.models import Challenge, Tip
import google.generativeai as genai
from flask_apscheduler import APScheduler
import os

genai.configure(api_key='AIzaSyDxax_5OB-GYTJ2cCsUUWrIFtBP1ILspY8')
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": None,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                              generation_config=generation_config)


def send_prompt(prompt):
    response = model.generate_content(prompt)
    return response.text.strip() if hasattr(response, 'text') else response

scheduler = APScheduler()


def init_scheduler(app):
    scheduler.init_app(app)
    scheduler.start()

    @scheduler.task("interval", id="fetch_daily_challenge", hours=24)
    def fetch_daily_challenge():
        with app.app_context():
            description_prompt = "Generate a new and unique writing challenge that is interesting and different from the previous ones. Explain the challenge in a short paragraph suitable for an HTML snippet. Your response MUST NOT contain any special characters, only letters, numbers and new lines."

            # Generate description first
            challenge_description = send_prompt(description_prompt)

            # Generate title based on the description
            title_prompt = f"Generate a creative and unique title for the following writing challenge: {challenge_description}. Your response MUST NOT contain any special characters, only the title in letters."
            challenge_title = send_prompt(title_prompt)

            new_challenge = Challenge(title=challenge_title, description=challenge_description)
            db.session.add(new_challenge)
            db.session.commit()

    @scheduler.task("interval", id="fetch_and_print_challenge", hours=24)
    def fetch_daily_tip():
        with app.app_context():
            prompt = "Give me a new and unique writing tip to improve my writing skills, that is different from the ones I've generated before. Explain the tip in a short paragraph suitable for an HTML snippet. Your response MUST NOT contain any special characters, only letters, numbers and new lines."
            tip_text = send_prompt(prompt)
            new_tip = Tip(tip=tip_text)
            db.session.add(new_tip)
            db.session.commit()
