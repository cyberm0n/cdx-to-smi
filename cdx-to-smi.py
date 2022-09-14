import argparse
import os

parser = argparse.ArgumentParser(description="cdx to smi")
parser.add_argument("-p","--packet",metavar="<packet name>",help="cdx to smi formatting",default="-")
group = parser.add_mutually_exclusive_group()
args = parser.parse_args()
def progress():
	os.system("obabel -icdx "+args.packet+" -osmi -O output2.smi")

	with open("output2.smi","r") as f:
		return f.read()

if args.packet != "-":
	print(progress())
