#!/usr/bin/python3
from apscheduler.schedulers.background import BackgroundScheduler
from app import db
from app.models import Challenge, Tip
import google.generativeai as genai
from flask import current_app
import os


genai.configure(api_key=os.getenv("GENAI_API_KEY"))
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 150,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config)


def send_prompt(prompt):
    response = model.generate_content(prompt)
    return response.text


def fetch_daily_challenge():
    with current_app.app_context():
        prompt = "Give me a unique daily writing challenge that is interesting and different from the previous ones."
        challenge_text = send_prompt(prompt)
        new_challenge = Challenge(title="Daily Writing Challenge", description=challenge_text)
        db.session.add(new_challenge)
        db.session.commit()


def fetch_daily_tip():
    with current_app.app_context():
        prompt = "Give me a writing tip that will help me improve my writing skills."
        tip_text = send_prompt(prompt)
        new_tip = Tip(content=tip_text)
        db.session.add(new_tip)
        db.session.commit()


def start_scheduler(app):
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_daily_challenge, 'cron', hour=21)
    scheduler.add_job(fetch_daily_tip, 'cron', hour=21)
    scheduler.start()
