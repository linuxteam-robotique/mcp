#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.WARNING,
                    format="%(levelname)-8s|%(asctime)s.%(msecs)03d|%(thread)5d-%(threadName)-15s|%(name)-15s|%(message)s",
                    datefmt='%H:%M:%S',
                    )

from match import Match

if __name__ == "__main__":
    match = Match()
    try:
        match.deroulement_match()
    except KeyboardInterrupt:
        pass

    print "bye bye !"
