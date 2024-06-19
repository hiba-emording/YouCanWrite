#!/usr/bin/python3
"""Fetches daily writing challenges & tips"""
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import logging
from .models import Tip, Challenge
from datetime import datetime

logging.basicConfig(level=logging.INFO)

scheduler = BackgroundScheduler()

def fetch_and_print_tip():
    tip = Tip.query.order_by(Tip.created_at.desc()).first()
    if tip:
        logging.info(f"Daily Writing Tip: {tip.tip}")

def fetch_and_print_challenge():
    challenge = Challenge.query.order_by(Challenge.created_at.desc()).first()
    if challenge:
        logging.info(f"Daily Writing Challenge: {challenge.title}\n{challenge.description}")

scheduler.add_job(fetch_and_print_tip, CronTrigger(hour=8, minute=0))
scheduler.add_job(fetch_and_print_challenge, CronTrigger(hour=8, minute=1))

scheduler.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    scheduler.shutdown()
