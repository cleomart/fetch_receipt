
from .models import Receipt
import re
import math

class ReceiptPointsCalc:
    ALPHA_NUM_PATTERN = r'[a-zA-Z0-9]'
    AFTER_2PM_MINS = (60 * 14) + 1
    BEFORE_4PM_MINS = (60 * 16) - 1

    def __init__(self, receipt_id):
        self.receipt = Receipt.objects.get(id=receipt_id)
        self.points = 0

    def generate(self):
        self.process_retailer()
        self.process_total()
        self.process_items()
        self.process_date()
        self.process_time()
        return self.points

    def process_retailer(self):
        # One point for every alphanumeric character in the retailer name
        self.points += len(re.findall(ReceiptPointsCalc.ALPHA_NUM_PATTERN, self.receipt.retailer))

    def process_total(self):
        # 50 points if the total is a round dollar amount with no cents
        if float(self.receipt.total) % 1.00 == 0:
            self.points += 50

        # 25 points if the total is a multiple of 0.25
        if float(self.receipt.total) % 0.25 == 0:
            self.points += 25

    def process_items(self):
        items = self.receipt.items.all()

        # 5 points for every two items on the receipt
        self.points += (len(items) // 2) * 5

        # If the trimmed length of the item description is a multiple of 3,
        # multiply the price by 0.2 and round up to the nearest integer.
        # The result is the number of points earned
        for item in items:
            if len(item.shortDescription.strip()) % 3 == 0:
                self.points += int(math.ceil(float(item.price) * 0.2))

    def process_date(self):
        # 6 points if the day in the purchase date is odd
        if self.receipt.purchaseDate.day % 2 == 1:
            self.points += 6

    def process_time(self):
        total_minutes = (self.receipt.purchaseTime.hour * 60) + self.receipt.purchaseTime.minute
        # 10 points if the time of purchase is after 2:00pm and before 4:00pm
        if ReceiptPointsCalc.AFTER_2PM_MINS <= total_minutes <= ReceiptPointsCalc.BEFORE_4PM_MINS:
            self.points += 10

    @staticmethod
    def does_exist(receipt_id):
        return Receipt.objects.filter(id=receipt_id).exists()