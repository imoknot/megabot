from pydantic import BaseModel


class ExcludeNone(BaseModel):
    def dict(self, *args, **kwargs):
        if kwargs.get('exclude_none'):
            del kwargs['exclude_none']
        return super().dict(*args, exclude_none=True, **kwargs)


class Location(ExcludeNone):
    longitude: float
    latitude: float
    horizontal_accuracy: float
    live_period: int | None = None
    heading: int | None = None
    proximity_alert_radius: int | None = None


class File(ExcludeNone):
    file_id: str
    file_unique_id: str
    file_size: int
    file_path: str | None = None


class Venue(ExcludeNone):
    location: Location
    title: str
    address: str
    foursquare_id: str | None = None
    foursquare_type: str | None = None
    google_place_id: str | None = None
    google_place_type: str | None = None
