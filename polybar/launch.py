#!/usr/bin/python
from subprocess import Popen
from subprocess import DEVNULL
from subprocess import call
from signal import SIGILL
from Xlib import display
import os
import sys
import logging

pid = os.path.realpath('pid')
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def recursive_nodes(node, term):
    '''traverses all open windows until polybar got found.
    returns the polybar window'''

    for child in node.query_tree().children:
        try:
            if(term in child.get_wm_class()):
                return child
            res = recursive_nodes(child, term)
            if(term in res.get_wm_class()):
                return res
        except:
            pass


def is_visible(node):
    '''Checks wether polybar is mapped to X'''
    try:
        if(node.get_attributes()._data['map_state'] > 0):
            return True
        return False
    except:
        return None


def toggle():
    '''toggles the mapped status of polybar window'''

    d = display.Display()
    root = d.screen().root
    poly = recursive_nodes(root, 'polybar')

    if(is_visible(poly)):
        call(["xdo", "hide", "-N", "Polybar"])
    else:
        call(["xdo", "show", "-N", "Polybar"])


def run():
    '''start polybar'''
    proc = Popen(["/bin/polybar", "top"], stdout=DEVNULL, stderr=DEVNULL)
    print('open polybar: pid: %s' % proc.pid)
    try:
        open(pid, 'w').write(str(proc.pid))
    except Exception as e:
        logger.error(e)

    return proc

# def is_running(pid):
#    '''check if polybar is already running'''
#    try:
#        p = Process(pid = pid)
#        if p.name() is 'polybar' and p.is_running():
#            return True
#        return False
#    except Exception:
#        logger.info('pid is not assigned currently')
#        return False
#
#
# def get_pid():
#    '''retrieves the pid from local file'''
#    if(os.path.isfile(pid)):
#        logger.debug('pid exists')
#        try:
#            p_id = open(pid, 'rb').readline().decode('UTF-8')
#            return p_id
#        except Exception as e:
#            logger.error(e)
#    else:
#        return None


def is_running():

    isRunning = False
    if(os.path.isfile(pid)):
        logger.debug('pid exists')
        try:
            p_id = open(pid, 'rb').readline().decode('UTF-8')
            isRunning = os.path.isdir('/proc/' + str(p_id))
        except Exception as e:
            logger.error(e)

        if(isRunning):
            logger.info('process still running')
            sys.exit(0)

    return isRunning


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", help="toggle polybar: show/hide", action="store_true")
    args = parser.parse_args()

    if(args.t):
        print('toggle')
        toggle()

    if(not is_running()):
        proc = run()
