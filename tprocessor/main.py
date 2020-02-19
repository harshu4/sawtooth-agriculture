from sawtooth_sdk.processor.core import TransactionProcessor
from handler import MarketTransactionHandler

def main():
    processor = TransactionProcessor(url='tcp://validator:4004')

    handler = MarketTransactionHandler()

    processor.add_handler(handler)

    processor.start()
