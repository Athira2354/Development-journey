from csv import DictReader

class TransactionAnalyzer:

    def __init__(self):

        fr=open("python Basics\\Object Oriented programming(OOPS)\\bank analyzer\\bank_transactions_500_records.csv")

        self.transactions=list(DictReader(fr))

        print(len(self.transactions),"record found")

    def debit_transaction(self):
        for t in self.transactions:
            if t.get("type")=="debit":
                print(t)
            
    def credit_transaction(self):
        for t in self.transactions:
            if t.get("type")=="credit":
                print(t)
               


    def high_value_transaction(self):pass

    def high_value_credit_transaction(self):pass


analysis=TransactionAnalyzer()
analysis.debit_transaction()
analysis=TransactionAnalyzer()
analysis.credit_transaction()
analysis=TransactionAnalyzer()
analysis.high_value_transaction()
analysis=TransactionAnalyzer()
analysis.high_value_credit_transaction()
