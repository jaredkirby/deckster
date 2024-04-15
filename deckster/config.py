# config.py

from pptx.util import Inches
from pptx.dml.color import RGBColor

# File paths
PPT_TEMPLATE_PATH = "CPGenius/GenerateReport/AJI-Report-Template.pptx"
DATA_FILE_PATH = "data.json"
LOG_FILE_PATH = "app.log"

# Table configuration
TABLE_LEFT = Inches(6.08)
TABLE_TOP = Inches(1.93)
TABLE_WIDTH = Inches(7.2)
TABLE_HEIGHT = Inches(4.15)
TABLE_ROW_HEIGHTS = [1, 0.5, 2, 1]

# Cell formats
CELL_FORMATS = {
    "title": {
        "background_color": RGBColor(59, 125, 35),
        "font_color": RGBColor(255, 255, 255),
        "font_size": 12,
        "bold": True,
    },
    "date": {
        "background_color": RGBColor(203, 204, 209),
        "font_color": RGBColor(0, 0, 0),
        "font_size": 10,
        "bold": False,
    },
    "estimated": {
        "background_color": RGBColor(180, 229, 162),
        "font_color": RGBColor(0, 0, 0),
        "font_size": 10,
        "bold": False,
    },
    "delivered": {
        "background_color": RGBColor(203, 204, 209),
        "font_color": RGBColor(0, 0, 0),
        "font_size": 10,
        "bold": False,
    },
}

# Font settings
DEFAULT_FONT_SIZE = 18
DEFAULT_FONT_COLOR = RGBColor(0, 0, 0)
