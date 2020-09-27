import urllib.request as request
from pathlib import Path
import shutil
import os
import argparse

from extract_zips import extract


parser = argparse.ArgumentParser(description="Download and unzip SPL data.")
parser.add_argument('--unzip', metavar='u', default='-1', type=int, help='Number of files to unzip from SPL')
download_or_select = parser.add_mutually_exclusive_group()
download_or_select.add_argument('--download', metavar='d', default='4', type=int, help='Number of SPL files to download, max 4')
download_or_select.add_argument('--select', metavar='s', type=int, help="Specific SPL file to download, i.e. 1, 2, 3 or 4")

args = parser.parse_args()
depth = args.unzip
number = args.download
spl = args.select


cwd = Path(__file__).parent.absolute()
data_dir = cwd / 'data'

if not data_dir.exists():
    data_dir.mkdir(exist_ok=True)

try:
    if number == 4 and not spl:
        for i in range(1, 5):
            with request.urlopen(
                    f'ftp://public.nlm.nih.gov/nlmdata/.dailymed/dm_spl_release_human_rx_part{i}.zip') as r, open(  # noqa: E501
                        f'{data_dir}/spl_part{i}.zip', 'wb') as f:
                shutil.copyfileobj(r, f)
            extract(depth)
            os.remove(f'{data_dir}/spl_part{i}.zip')
    elif number < 4 and not spl:
        for i in range(1, number):
            with request.urlopen(
                        f'ftp://public.nlm.nih.gov/nlmdata/.dailymed/dm_spl_release_human_rx_part{i}.zip') as r, open(  # noqa: E501
                            f'{data_dir}/spl_part{i}.zip', 'wb') as f:
                shutil.copyfileobj(r, f)
            extract(depth)
            os.remove(f'{data_dir}/spl_part{i}.zip')
    elif spl:
        with request.urlopen(
                    f'ftp://public.nlm.nih.gov/nlmdata/.dailymed/dm_spl_release_human_rx_part{spl}.zip') as r, open(  # noqa: E501
                        f'{data_dir}/spl_part{spl}.zip', 'wb') as f:
            shutil.copyfileobj(r, f)
        extract(depth)
        os.remove(f'{data_dir}/spl_part{spl}.zip')

except Exception as err:
    raise (f"Unable to perform request: {err}")
finally:
    print("Downloads complete")
