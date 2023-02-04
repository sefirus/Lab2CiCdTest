import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--difficulty', default=1, help='set difficulty level; from 1 to 3')

args = parser.parse_args()