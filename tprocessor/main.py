import argparse
import sys
import logging
from sawtooth_sdk.processor.core import TransactionProcessor
from sawtooth_sdk.processor.log import init_console_logging

from handler import MarketTransactionHandler
LOGGER = logging.getLogger(__name__)

def parse_args(args):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)


    parser.add_argument(
        '-C', '--connect',
        default='tcp://localhost:4004',
        help='Endpoint for the validator connection')

    parser.add_argument(
        '-v', '--verbose',
        action='count',
        default=0,
        help='Increase output sent to stderr')

    return parser.parse_args(args)

def setup_loggers():
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

def main(args=None):
    setup_loggers()
    if args is None:
        args = sys.argv[1:]
    opts = parse_args(args)

    processor = None
    try:

        init_console_logging(verbose_level=opts.verbose)
        processor = TransactionProcessor(url=opts.connect)
        handler = MarketTransactionHandler()
        processor.add_handler(handler)
        processor.start()
    except KeyboardInterrupt:
        pass
    except Exception as err:  # pylint: disable=broad-except
        print("Error: {}".format(err))
    finally:
        if processor is not None:

            processor.stop()
main()
