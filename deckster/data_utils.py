# data_utils.py

import json
from typing import List, Dict, Any


def read_json_data(file_path: str) -> Dict[str, Any]:
    """
    Reads data from a JSON file and returns it as a dictionary.

    Args:
        file_path: The path to the JSON file.

    Returns:
        A dictionary representing the data from the JSON file.
    """
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def transform_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Transforms the data into the required format for the PowerPoint presentation.

    Args:
        data: The input data as a dictionary.

    Returns:
        The transformed data as a dictionary.
    """
    transformed_data = {
        "Page Title": f"{data['campaigns'][0]['brand']} {data['campaigns'][0]['retailer']} Campaign",
        "Recommendation": data["recommendations"],
        "Results and Learnings": data["learnings"],
        "Tactics": [
            {
                "title": tactic["name"],
                "date": f"{tactic['start_date']} - {tactic['end_date']}",
                "estimated": ", ".join(tactic["estimated_results"]),
                "delivered": ", ".join(tactic["actual_results"]),
            }
            for tactic in data["tactics"]
        ],
    }
    return transformed_data


def get_presentation_data(file_path: str) -> Dict[str, Any]:
    """
    Retrieves the data for the PowerPoint presentation from a JSON file.

    Args:
        file_path: The path to the JSON file containing the presentation data.

    Returns:
        A dictionary containing the presentation data.
    """
    json_data = read_json_data(file_path)
    presentation_data = transform_data(json_data)
    return presentation_data
