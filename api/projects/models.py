from datetime import datetime

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy_media import Image, ImageAnalyzer, ImageValidator, ImageProcessor
from configuration.db import Base
from projects.schemas import Json


class ImageWithMyFilename(Image):
    """
    Overwrite filename property
    """
    @property
    def filename(self) -> str:
        if not self.timestamp:
            self.timestamp = datetime.now().timestamp()
        time_key = datetime.fromtimestamp(float(self.timestamp)).strftime("%Y/%m/%d/%H:%M:%S")
        # return '%s-%s%s%s' % (self.__prefix__, self.key, self.suffix,
        #                       self.extension if self.extension else '')
        return f'{time_key}-{self.key}{self.extension if self.extension else ""}'


class ProjectImage(ImageWithMyFilename):
    __pre_processors__ = [
        ImageAnalyzer(),
        ImageValidator(
            minimum=(80, 80),
            # min_aspect_ratio=1.2,
            content_types=['image/jpeg', 'image/png']
        ),
        ImageProcessor(
            fmt='png',
        )
    ]


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    description = Column(Text)
    url = Column(String)
    photo_url = Column(ProjectImage.as_mutable(Json))
