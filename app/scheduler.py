#!/usr/bin/python3
from app import db
from app.models import Challenge, Tip
import google.generativeai as genai
from flask_apscheduler import APScheduler
import os

genai.configure(api_key=os.getenv("GENAI_API_KEY"))
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 150,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                              generation_config=generation_config)


def send_prompt(prompt):
    response = model.generate_content(prompt)
    return response.text

scheduler = APScheduler()


def init_scheduler(app):
    scheduler.init_app(app)
    scheduler.start()

    @scheduler.task("interval", id="fetch_daily_challenge", hours=24)
    def fetch_daily_challenge():
        with app.app_context():
            prompt = "Give me a unique daily writing challenge that is interesting and different from the previous ones."
            challenge_text = send_prompt(prompt)
            new_challenge = Challenge(title="Daily Writing Challenge",
                                      description=challenge_text)
            db.session.add(new_challenge)
            db.session.commit()

    @scheduler.task("interval", id="fetch_and_print_challenge", hours=24)
    def fetch_daily_tip():
        with app.app_context():
            prompt = "Give me a writing tip that will help me improve my writing skills."
            tip_text = send_prompt(prompt)
            new_tip = Tip(tip=tip_text)
            db.session.add(new_tip)
            db.session.commit()
