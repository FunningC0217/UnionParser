#!/usr/bin/env python3.7
# coding: utf-8
import argparse
import json
import logging
import os
import sys
import time
from multiprocessing import cpu_count

from until.callproxy import CallProxy
from until.cxxparser import CxxParser
from until.javaparser import JavaParser
from until.pythonparser import PythonParser

log = logging.getLogger(__name__)

LOG_FORMAT = "%(asctime)s {0} - %(levelname)s - %(name)s - %(message)s".format(
    time.localtime().tm_zone)

def configure_logger(verbose=0, log_config=None, log_file=None):
    root_logger = logging.root

    if log_config:
        with open(log_config, 'r', encoding='utf-8') as f:
            logging.config.dictConfig(json.load(f))
    else:
        formatter = logging.Formatter(LOG_FORMAT)
        if log_file:
            log_handler = logging.handlers.RotatingFileHandler(
                log_file, mode='a', maxBytes=50*1024*1024,
                backupCount=10, encoding=None, delay=0
            )
        else:
            log_handler = logging.StreamHandler()
        log_handler.setFormatter(formatter)
        root_logger.addHandler(log_handler)

    if verbose == 0:
        level = logging.WARNING
    elif verbose == 1:
        level = logging.INFO
    elif verbose >= 2:
        level = logging.DEBUG

    root_logger.setLevel(level)

def add_arguments(parser, proxy):
    parser.add_argument(
        "-s", "--storage", type=str, required=True,
        help="storage path from do parse language files result saved"
    )
    parser.add_argument(
        "-w", "--workspace", type=str, default=proxy.workspace(),
        help="language source files root path, same LSP workspace, default is program path."
    )
    parser.add_argument(
        "-l", "--language", default="", choices=proxy.supportLanguages(),
        help="select workspace language type files. It is blank by default. "
             "If no language is specified, all supported languages will be processed.",
    )
    parser.add_argument(
        "-j", "--job", type=int, default=cpu_count(),
        help="The number of tasks to be started is generally not required to be specified. "
             "By default, it is consistent with the number of CPUs"
    )
    parser.add_argument(
        '-v', '--verbose', action='count', default=0,
        help="Increase verbosity of log output, overrides log config file."
    )
    log_group = parser.add_mutually_exclusive_group()
    log_group.add_argument(
        "--log-config",
        help="Path to a JSON file containing Python logging config."
    )
    log_group.add_argument(
        "--log-file",
        help="Redirect logs to the given file instead of writing to stderr."
        "Has no effect if used with --log-config."
    )
    return parser

def _stdio():
    stdin, stdout = sys.stdin.buffer, sys.stdout.buffer
    return stdin, stdout

def initProxy():
    proxy = CallProxy()
    proxy.addParser(CxxParser())
    proxy.addParser(JavaParser())
    proxy.addParser(PythonParser())
    return proxy

def getFiles(workspace):
    files = []
    for root, dirs, files in os.walk(workspace):
        root + "\\" + files
        print(root)
        print(dirs)
        print(files)

def main():
    proxy = initProxy()
    args_parser = add_arguments(argparse.ArgumentParser(), proxy)
    args_parser.description = "Union Parser"
    args = args_parser.parse_args()
    configure_logger(args.verbose, args.log_config, args.log_file)
    log.critical("started " + args_parser.description)
    proxy.setWorkspace(args.workspace)
    proxy.setStorage(args.storage)
    proxy.doParse()

if __name__ == '__main__':
    main()
