from atipcore.ext import API_SUCCESS
from flask import request
import numpy as np
from .ml_model import predict_score


def calculate_score():
    answers_with_model_answers = request.validated_json
    answer_scores = [
        predict_score(
            answer_with_model_answer.get("modelAnswer"),
            answer_with_model_answer.get("answer")
        ) for answer_with_model_answer in answers_with_model_answers
    ]
    avg_score = np.average(answer_scores)
    return API_SUCCESS(payload={"score": avg_score})
