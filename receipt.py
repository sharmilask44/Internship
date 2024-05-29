class TransReceipt:
    def __init__(self, trans_id, sender, recipient, amount, timestamp):
        self.trans_id = trans_id
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = timestamp

    def gen_receipt(self):
        receipt = f"Transaction ID: {self.trans_id}\n"
        receipt += f"Sender: {self.sender}\n"
        receipt += f"Recipient: {self.recipient}\n"
        receipt += f"Amount: {self.amount}\n"
        receipt += f"Timestamp: {self.timestamp}\n"
        return receipt


trans_id = "196a1056"
sender = "Laxman"
recipient = "Groceries"
amount = 2500
timestamp = "2023-10-25 10:30:00"

trans_id = "196a1078"
sender = "Vasu"
recipient = "Books"
amount = 1300
timestamp = "2019-04-00 07:45:00"

receipt_data = TransReceipt(trans_id, sender, recipient, amount, timestamp)
receipt = receipt_data.gen_receipt()
print(receipt)
