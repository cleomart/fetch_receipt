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


def check_unknown_fields(obj):
    """ Check fields that are not required to have """
    if hasattr(obj, 'initial_data'):
            #print("initial ", obj.initial_data)
            unknown_fields = list(set(obj.initial_data.keys()) - set(obj.fields.keys()))
            if unknown_fields:
                raise ValidationError(f"Received unknowm fields={unknown_fields} in {obj.initial_data}")

def check_items_min_count(obj):
    """ Check the length of items is at least 1 """
    if hasattr(obj, 'initial_data'):
        if len(obj.initial_data["items"]) < 1:
            raise ValidationError(f"Items field should have at least 1 item")

def check_date_and_time_format(obj):
     """ Check the format of time and date """
     if hasattr(obj, 'initial_data'):
        time_validator(obj.initial_data["purchaseTime"])
        date_validator(obj.initial_data["purchaseDate"])

def price_validator_serializer(obj):
     """ Check the price and total format """
     if hasattr(obj, 'initial_data'):
           price_validator(obj.initial_data["price" if "price" in obj.initial_data else "total"])