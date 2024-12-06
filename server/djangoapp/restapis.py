"""
This module provides API interaction functions for the Django application.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url', default="http://localhost:5050/"
)


def get_request(endpoint, **kwargs):
    """
    Args:
        endpoint (str): The API endpoint to append to the backend URL.
        **kwargs: Arbitrary keyword arguments to pass as query parameters.

    Returns:
        dict: The JSON response from the GET request.
    """
    params = ""
    if kwargs:
        params = "&".join(f"{key}={value}" for key, value in kwargs.items())

    request_url = f"{backend_url}{endpoint}?{params}"

    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        return response.json()
    except requests.RequestException:
        print("Network exception occurred")
        return None


def analyze_review_sentiments(text):
    """

    Args:
        text (str): The text to analyze.

    Returns:
        dict: The JSON response from the sentiment analyzer service.
    """
    request_url = f"{sentiment_analyzer_url}analyze/{text}"
    try:
        response = requests.get(request_url)
        return response.json()
    except requests.RequestException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return None


def post_review(data_dict):
    """
    Posts a review to the backend service.

    Args:
        data_dict (dict): The review data to post.

    Returns:
        dict: The JSON response from the POST request.
    """
    request_url = f"{backend_url}/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except requests.RequestException:
        print("Network exception occurred")
        return None
