from file import File
from metadata import ImageMetadata
from storage import LocalStorage

# tests
f1 = File(content='', metadata=ImageMetadata(path='https://otus.ru/static/img/logos/logo-2022-without-text.svg'))
assert f1.metadata.filename == 'logo-2022-without-text.svg'
assert f1.metadata.extension == 'svg'

ls = LocalStorage()
f2 = ls.find('/Users/magmel/Downloads/kma.pdf')
assert f2.metadata is not None
