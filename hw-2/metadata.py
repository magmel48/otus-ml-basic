from datetime import date
from pydantic import BaseModel, Field
from typing import Optional


class Metadata(BaseModel):
    path: str  # full path including protocol (file://, https://, ftp://, etc.)
    size: int = Field(default=0)  # in bytes
    created_at: date = Field(default_factory=lambda: date.today())
    updated_at: date = Field(default_factory=lambda: date.today())
    created_by: Optional[str] = Field(default=None)  # 'group@user' format
    updated_by: Optional[str] = Field(default=None)  # 'group@user' format

    @staticmethod
    def get_extension(filename):
        if '/' in filename:
            raise ValueError('cannot be a path')

        return filename.split('.')[-1]

    @staticmethod
    def get_filename(path):
        return path if len(path) == 0 else path.split('/')[-1]

    @property
    def filename(self):
        return Metadata.get_filename(self.path)

    @property
    def extension(self):
        return Metadata.get_extension(Metadata.get_filename(self.path))


class SoundMetadata(Metadata):
    bitrate: int = Field(default=0)


class VideoMetadata(SoundMetadata):
    pass


class ImageMetadata(Metadata):
    width: int = Field(default=0)
    height: int = Field(default=0)
