import abc
from file import File
from metadata import Metadata, SoundMetadata, VideoMetadata, ImageMetadata
from errors import UnsupportedFileExtension


SOUND_EXTENSIONS = ['mp3', 'ogg']
VIDEO_EXTENSIONS = ['mp4', 'mov', 'avi']
IMAGE_EXTENSIONS = ['jpeg', 'bmp', 'pdf', 'png', 'gif']


class Storage:
    @abc.abstractmethod
    def save(self, file):
        """Saves the file into the storage. Rewrites it if exists."""
        pass

    @abc.abstractmethod
    def find(self, path) -> File:
        """
        Finds and returns the file from the storage.

        :raises FileNotFoundError: if no file found.
        """
        pass

    @abc.abstractmethod
    def convert(self, file, content, metadata):
        """
        Converts the file into the new format.

        :param file: Old file.
        :param content: When the file converted into
        the new format - content can be untouched.
        :param metadata: New metadata.
        :return: None
        :raises UnsupportedConversion: if new format
        is not supported by the system.
        """
        pass


class LocalStorage(Storage):
    def save(self, file):
        with open(file.metadata.path, 'w') as local_file:
            local_file.write(file.content)

    def find(self, path) -> File:
        file = File(content='', metadata=Metadata(path=path))

        if file.metadata.extension in SOUND_EXTENSIONS:
            file.metadata = SoundMetadata(path=path, bitrate=16000)
        elif file.metadata.extension in VIDEO_EXTENSIONS:
            file.metadata = VideoMetadata(path=path, bitrate=32000)
        elif file.metadata.extension in IMAGE_EXTENSIONS:
            file.metadata = ImageMetadata(path=path, width=500, height=500)
        # in case of adding new file formats we need to add more branches here
        else:
            raise UnsupportedFileExtension(
                f'{file.metadata.extension} is not supported')

        return file

    def convert(self, file, content, metadata) -> File:
        file.content = content
        file.metadata = metadata

        return file


class S3Storage(Storage):
    def save(self, file):
        pass

    def find(self, path) -> File:
        pass

    def convert(self, file, content, metadata) -> File:
        pass
