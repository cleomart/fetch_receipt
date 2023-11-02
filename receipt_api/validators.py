from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

retailer_validator = \
    RegexValidator("^\\S+$",
                   message="The name of the retailer should be non-whitespace at the beginnng and at the end. Example: target")

price_validator =  \
    RegexValidator("^\\d+\\.\\d{2}$",
                   message="The price amount should be written whole digits followed by 2 decimal places. Example: 6.49")

short_desc_validator = \
    RegexValidator("^[\\w\\s\\-]+$",
                    message="Short description can only have word characters such as letters (a-z, A-Z), digits (0-9),underscores (_), whitespace, and hyphens")

time_validator = \
    RegexValidator("^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$",
                    message="Purchase time should have a format HH:MM")

date_validator = \
    RegexValidator("^\\d{4}-\\d{2}-\\d{2}$",
                    message="Purchase date should have a format YYYY-MM-DD")