"""Contains capture assistant functions and classes."""
from enum import EnumMeta, Enum, _EnumDict

import _zivid
import zivid._settings_converter as _settings_converter


class StrEnumMeta(EnumMeta):
    def __new__(metacls, cls, bases, oldclassdict):
        newclassdict = _EnumDict()
        for k, v in oldclassdict.items():
            if v == ():
                v = k
            newclassdict[k] = v
        return super().__new__(metacls, cls, bases, newclassdict)

class AutoStrEnum(str, Enum, metaclass=StrEnumMeta):
    "base class for name=value str enums"

class AmbientLightFrequency(AutoStrEnum):
    """Ensure compatibility with the frequency of the ambient light in the scene."""

    hz50 = ()
    hz60 = ()
    none = ()

    def __str__(self):
        return str(self.name)


assert AmbientLightFrequency.__members__.keys() == _zivid.captureassistant.AmbientLightFrequency.__members__.keys(), f"{AmbientLightFrequency} not in sync with C++ implementation."

class SuggestSettingsParameters:  # pylint: disable=too-few-public-methods
    """Input to the Capture Assistant algorithm.

    Used to specify a constraint on the total capture time for the settings suggested by the Capture Assistant,
    and optionally specify the ambient light frequency.
    The capture time constraint assumes a computer meeting Zivid's recommended minimum compute power.

    """

    def __init__(self, max_capture_time, ambient_light_frequency=None):
        """Initialize SuggestSettingsParameters.

        Args:
            max_capture_time: an instance of datetime.timedelta
            ambient_light_frequency: a member of the enum zivid.captureassistant.AmbientLightFrequency

        """
        if ambient_light_frequency is None:
            self.__impl = _zivid.captureassistant.SuggestSettingsParameters(
                max_capture_time
            )
        else:
            self.__impl = _zivid.captureassistant.SuggestSettingsParameters(
                max_capture_time,
                getattr(_zivid.captureassistant.AmbientLightFrequency, ambient_light_frequency.name),
            )

    @property
    def max_capture_time(self):
        """Get max capture time.

        Returns:
            Instance of datetime.timedelta

        """
        return self.__impl.maxCaptureTime()

    @property
    def ambient_light_frequency(self):
        """Get ambient light frequency.

        Returns:
            Instance of AmbientLightFrequency

        """
        return AmbientLightFrequency(self.__impl.ambientLightFrequency().name)

    def __str__(self):
        return self.__impl.to_string()


def suggest_settings(camera, suggest_settings_parameters):
    """Find settings for the current scene based on the suggest_settings_parameters.

    The suggested settings returned from this function should be passed into hdr.capture to perform the actual capture.

    Args:
        camera: an instance of zivid.Camera
        suggest_settings_parameters: an instance of zivid.captureassistant.SuggestSettingsParameters which provides
                                     parameters (e.g., max capture time constraint) to the suggest_settings algorithm.

    Returns:
        List of Settings.

    """
    internal_settings = _zivid.captureassistant.suggest_settings(
        camera._Camera__impl,  # pylint: disable=protected-access
        suggest_settings_parameters._SuggestSettingsParameters__impl,  # pylint: disable=protected-access
    )
    return [_settings_converter.to_settings(internal) for internal in internal_settings]
