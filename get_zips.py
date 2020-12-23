import urllib.request as request
from pathlib import Path
import shutil
import os
import argparse
import zipfile

from extract_zips import extract


parser = argparse.ArgumentParser(description="Download and unzip SPL data.")
parser.add_argument(
            '--unzip',
            metavar='int',
            default='-1',
            type=int,
            help='Optional number of files to extract from SPL zip.'
        )
download_or_select = parser.add_mutually_exclusive_group()
download_or_select.add_argument(
                    '--download',
                    metavar='int',
                    default='4',
                    type=int,
                    help='Optional number of SPL zip files to download, max 4.'
                )
download_or_select.add_argument(
                    '--select',
                    metavar='int',
                    type=int,
                    help="Optional SPL zip file to download, i.e. 1, 2, 3 or 4"
                )

args = parser.parse_args()
depth = args.unzip
number = args.download
spl_zip = args.select


cwd = Path(__file__).parent.absolute()
data_dir = cwd / 'data'

if not data_dir.exists():
    data_dir.mkdir(exist_ok=True)

try:
    output_dir = data_dir / 'rxnorm'
    if not output_dir.exists():
        output_dir.mkdir(exist_ok=True)
    with request.urlopen('ftp://public.nlm.nih.gov/nlmdata/.dailymed/rxnorm_mappings.zip') as r, open(  # noqa: E501
            f'{data_dir}/rxnorm.zip', 'wb') as f:
        shutil.copyfileobj(r, f)
    with zipfile.ZipFile(f'{data_dir}/rxnorm.zip') as zip_ref:
        zip_ref.extractall(output_dir)
    os.remove(f'{data_dir}/rxnorm.zip')
except Exception as err:
    raise Exception(f"Unable to perform request: {err}") 

try:
    if spl_zip:
        with request.urlopen(
                    f'ftp://public.nlm.nih.gov/nlmdata/.dailymed/dm_spl_release_human_rx_part{spl_zip}.zip') as r, open(  # noqa: E501
                        f'{data_dir}/spl_part{spl_zip}.zip', 'wb') as f:
            shutil.copyfileobj(r, f)
        extract(depth)
        os.remove(f'{data_dir}/spl_part{spl_zip}.zip')
    else:
        for i in range(1, number+1):
            with request.urlopen(
                    f'ftp://public.nlm.nih.gov/nlmdata/.dailymed/dm_spl_release_human_rx_part{i}.zip') as r, open(  # noqa: E501
                        f'{data_dir}/spl_part{i}.zip', 'wb') as f:
                shutil.copyfileobj(r, f)
            extract(depth)
            os.remove(f'{data_dir}/spl_part{i}.zip')
except Exception as err:
    raise Exception(f"Unable to perform request: {err}")
finally:
    print("Downloads complete")
