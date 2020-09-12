import urllib.request as request
from pathlib import Path


cwd = Path(__file__).parent.absolute()
data_dir = cwd / 'data'

if not data_dir.exists():
    data_dir.mkdir(exist_ok=True)

try:
    for i in range(1, 5):
        with request.urlopen(
                f'ftp://public.nlm.nih.gov/nlmdata/.dailymed/\
                dm_spl_release_human_rx_part{i}.zip') as r, open(
                    f'{data_dir}/spl_part{i}.zip', 'wb') as f:
            f.write(r.read())
except Exception as err:
    raise (f"Unable to perform request: {err}")
finally:
    print("Downloads complete")
