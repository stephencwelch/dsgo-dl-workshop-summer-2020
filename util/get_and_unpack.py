import wget, argparse, zipfile, tarfile, os, sys
from pathlib import Path

def simple_progress_bar(current, total, width=80):
    progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()

def get_and_unpack(url, location='data/'):
	print('\033[1m' + ' Downloading...this might take a little while...' + '\033[0m')

	Path(location).mkdir(exist_ok=True)
	filename = wget.download(url, out=location, bar=simple_progress_bar)

	print('\n' +  '\033[1m' + ' Unzipping...' + '\033[0m')
	zip_ref = zipfile.ZipFile(filename, 'r')
	zip_ref.extractall(path=location)
	zip_ref.close()
	os.remove(filename)
	print('\033[1m' + 'Done!' + '\033[0m')

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='(python get_and_unpack.py -url web_address')
	parser.add_argument("-url", dest='url', required=True, help='web_address')
	args = parser.parse_args()
	get_and_unpack(args.url)




