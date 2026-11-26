import base64, pathlib, tarfile, io
archive = base64.b64decode(pathlib.Path('site.tar.gz.b64').read_text())
with tarfile.open(fileobj=io.BytesIO(archive), mode='r:gz') as bundle:
    bundle.extractall('dist', filter='data')
