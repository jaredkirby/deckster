# Deckster

Deckster is a Python package that automates the generation of PowerPoint presentations using data from JSON objects. It provides a convenient way to create professional-looking presentations with dynamic content, tables, and formatting.

## Features

- Generates PowerPoint presentations from JSON data sources
- Supports adding text, bullet points, and tables to slides
- Allows customization of font styles, colors, and sizes
- Provides error handling and logging for easy debugging
- Modular and extensible design for easy integration and customization

## Installation

To install Deckster, you need to have Python 3.x installed on your system. You can install Deckster using pip:

```
pip install deckster
```

## Usage

To use Deckster, follow these steps:

1. Prepare your JSON data source containing the content for your presentation.

2. Import the necessary functions and classes from the Deckster package:

```python
from deckster import generate_presentation
```

3. Call the `generate_presentation` function with the required arguments:

```python
generate_presentation(template_path, data_path, output_path)
```

- `template_path`: The path to the PowerPoint template file (`.pptx`).
- `data_path`: The path to the JSON file containing the presentation data.
- `output_path`: The path where the generated presentation will be saved.

4. Run your Python script, and Deckster will generate the PowerPoint presentation based on the provided template and data.

## JSON Data Format

The JSON data source should have the following structure:

```json
{
  "slides": [
    {
      "layout": "Title Slide",
      "title": "Presentation Title",
      "subtitle": "Subtitle"
    },
    {
      "layout": "Content Slide",
      "title": "Slide Title",
      "content": [
        {
          "type": "text",
          "text": "This is a text paragraph."
        },
        {
          "type": "bullet_points",
          "points": [
            "Bullet point 1",
            "Bullet point 2",
            "Bullet point 3"
          ]
        },
        {
          "type": "table",
          "data": [
            ["Header 1", "Header 2", "Header 3"],
            ["Row 1, Cell 1", "Row 1, Cell 2", "Row 1, Cell 3"],
            ["Row 2, Cell 1", "Row 2, Cell 2", "Row 2, Cell 3"]
          ]
        }
      ]
    }
  ]
}
```

- The `"slides"` array contains objects representing each slide in the presentation.
- Each slide object should have a `"layout"` property specifying the slide layout (e.g., "Title Slide", "Content Slide").
- The slide content can include text paragraphs, bullet points, and tables.
- Text paragraphs are represented by objects with a `"type"` of `"text"` and a `"text"` property containing the paragraph text.
- Bullet points are represented by objects with a `"type"` of `"bullet_points"` and a `"points"` array containing the bullet point items.
- Tables are represented by objects with a `"type"` of `"table"` and a `"data"` array containing the table data as a 2D array.

## Configuration

Deckster provides a configuration file (`config.py`) where you can customize various settings such as file paths, table dimensions, cell formats, and font styles. Modify the values in the configuration file to suit your requirements.

## Error Handling and Logging

Deckster includes error handling and logging functionality to help with debugging and troubleshooting. Errors and exceptions are logged to a log file specified in the configuration. You can customize the logging behavior by modifying the `setup_logging` function in the `error_utils.py` module.

## Contributing

Contributions to Deckster are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

Deckster is open-source software licensed under the [MIT License](https://opensource.org/licenses/MIT).