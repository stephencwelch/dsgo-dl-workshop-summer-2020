import sys, wget, tarfile, os

def simple_progress_bar(current, total, width=80):
    progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()

def get_mvtech_dataset(data_dir, dataset_name):
    data_dir.mkdir(exist_ok=True)
    if not (data_dir/('%s.tar.xz'%dataset_name)).exists():
        wget.download('ftp://guest:GU.205dldo@ftp.softronics.ch/mvtec_anomaly_detection/%s.tar.xz'%dataset_name, \
                      out=str(data_dir/('%s.tar.xz'%dataset_name)), bar=simple_progress_bar)
    if not (data_dir/dataset_name).exists():
        tar=tarfile.open(data_dir/('%s.tar.xz'%dataset_name))
        tar.extractall(data_dir)
        tar.close()
        os.chmod(data_dir/dataset_name, 0o777) #May need to change permissions
