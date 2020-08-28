from pathlib import Path

def get_filenames():
    cwd = Path(__file__)
    partial_dir = cwd.parent.parent.parent.absolute() / 'data' / 'partial'
    adjusted_filenames = [ f'file://{path}' for path in list(partial_dir.iterdir()) ]
    return adjusted_filenames
