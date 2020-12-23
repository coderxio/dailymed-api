from pathlib import Path


def get_spls():
    cwd = Path(__file__)
    partial_dir = cwd.parent.parent.parent.absolute() / 'data' / 'spls'
    adjusted_filenames = [
        f'file://{path}' for path in list(partial_dir.iterdir())]
    return adjusted_filenames


def get_rxnorm():
    cwd = Path(__file__)
    rxnorm_dir = cwd.parent.parent.parent.absolute() / 'data' / 'rxnorm'
    adjusted_filenames = [
        f'{path}' for path in list(rxnorm_dir.iterdir())
    ]
    return adjusted_filenames
