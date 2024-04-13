# data_utils.py

import csv
from typing import List, Dict, Any


def read_csv_data(file_path: str) -> List[Dict[str, str]]:
    """
    Reads data from a CSV file and returns it as a list of dictionaries.

    Args:
        file_path: The path to the CSV file.

    Returns:
        A list of dictionaries representing the data from the CSV file.
    """
    data = []
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def transform_data(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Transforms the data into the required format for the PowerPoint presentation.

    Args:
        data: The input data as a list of dictionaries.

    Returns:
        The transformed data as a list of dictionaries.
    """
    transformed_data = []
    for item in data:
        transformed_item = {
            "title": item["Title"],
            "date": item["Date"],
            "estimated": item["Estimated"],
            "delivered": item["Delivered"],
        }
        transformed_data.append(transformed_item)
    return transformed_data


def get_presentation_data(file_path: str) -> Dict[str, Any]:
    """
    Retrieves the data for the PowerPoint presentation from a CSV file.

    Args:
        file_path: The path to the CSV file containing the presentation data.

    Returns:
        A dictionary containing the presentation data.
    """
    csv_data = read_csv_data(file_path)
    tactics = transform_data(csv_data)
    presentation_data = {
        "Page Title": "Your Page Title Here",
        "Recommendation": [
            "- Recommendation 1",
            "- Recommendation 2",
            "- Recommendation 3",
        ],
        "Results and Learnings": [
            "- Result 1",
            "- Learning 1",
            "- Result 2",
            "- Learning 2",
        ],
        "Tactics": tactics,
    }
    return presentation_data
