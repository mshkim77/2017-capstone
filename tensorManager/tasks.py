from capstone2017.celery import app as celery_app

import tensorflow as tf
import numpy as np


def learn_emotion_from_words(words, emotions):
    print("Hello!")