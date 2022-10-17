#!/usr/bin/env python3.7
# coding: utf-8

import sys
import time
import logging
import logging.config
import argparse
import json

log = logging.getLogger(__name__)
SUPPORT_LANGUAGES = ['Java', 'Python', 'C/C++']
LOG_FORMAT = "%(asctime)s {0} - %(levelname)s - %(name)s - %(message)s".format(
    time.localtime().tm_zone)

def add_arguments(parser):
    parser.description = "Union Parser"

    parser.add_argument(
        "-s", "--storage", action="store_true",
        help="AST files storage path"
    )
    parser.add_argument(
        "-w", "--workspace", action="store_true",
        help="language source files work path, same LSP workspace"
    )
    parser.add_argument(
        "-l",
        "--language",
        default="",
        choices=SUPPORT_LANGUAGES,
        help="select workspace language type files",
    )
    parser.add_argument(
        '-v', '--verbose', action='count', default=0,
        help="Increase verbosity of log output, overrides log config file"
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

def _stdio():
    stdin, stdout = sys.stdin.buffer, sys.stdout.buffer
    return stdin, stdout

def _configure_logger(verbose=0, log_config=None, log_file=None):
    root_logger = logging.root

    if log_config:
        with open(log_config, 'r', encoding='utf-8') as f:
            logging.config.dictConfig(json.load(f))
    else:
        formatter = logging.Formatter(LOG_FORMAT)
        if log_file:
            log_handler = logging.handlers.RotatingFileHandler(
                log_file, mode='a', maxBytes=50 * 1024 * 1024,
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    add_arguments(parser)
    args = parser.parse_args()
    _configure_logger(args.verbose, args.log_config, args.log_file)
    log.debug("debug")
    log.info("info")
    log.warning("warning")
    log.error("error")
    log.critical("critical")
