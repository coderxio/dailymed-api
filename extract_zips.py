from io import BytesIO
import zipfile
from pathlib import Path


def extract(depth=-1):
    cwd = Path(__file__).parent.absolute()
    data_dir = cwd / 'data'
    partial_dir = data_dir / 'partial'

    if not partial_dir.exists():
        partial_dir.mkdir(exist_ok=True)

    try:
        ziped_dm_data = list(data_dir.glob('*.zip'))[0]
    except Exception:
        raise Exception("Is there a zip file in the data dir?")

    with zipfile.ZipFile(ziped_dm_data) as zip_ref:
        unzip_count = depth

        for spl_zip in zip_ref.namelist():
            if not unzip_count:
                break
            unzip_count -= 1
            nested_zip_data = BytesIO(zip_ref.read(spl_zip))
            with zipfile.ZipFile(nested_zip_data) as nested_zip:
                for unzip_file in nested_zip.namelist():
                    if unzip_file.endswith('xml'):
                        nested_zip.extract(unzip_file, partial_dir)


if __name__ == '__main__':
    extract()
