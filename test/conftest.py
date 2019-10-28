import pytest
from scripts.sample_data import download_and_extract


@pytest.fixture()
def application():
    import zivid

    with zivid.Application() as app:
        yield app


@pytest.fixture(scope="session")
def sample_data_file():
    from pathlib import Path
    import tempfile

    with tempfile.TemporaryDirectory() as temp_dir:
        sample_data = Path(temp_dir) / "MiscObjects.zdf"
        download_and_extract(sample_data)
        yield sample_data


@pytest.fixture()
def file_camera(application, sample_data_file):  # pylint: disable=redefined-outer-name
    with application.create_file_camera(sample_data_file) as file_cam:
        yield file_cam


@pytest.fixture()
def frame(
    application, sample_data_file
):  # pylint: disable=redefined-outer-name, unused-argument
    import zivid

    with zivid.Frame(sample_data_file) as frame:
        yield frame


@pytest.fixture()
def random_settings():
    import datetime
    from random import randint, choice, uniform
    import zivid

    heavily_modified_settings = zivid.Settings(
        bidirectional=choice([True, False]),
        blue_balance=uniform(1, 8),
        brightness=uniform(0, 1.8),
        exposure_time=datetime.timedelta(microseconds=randint(6500, 100000)),
        filters=zivid.Settings.Filters(
            contrast=zivid.Settings.Filters.Contrast(
                enabled=choice([True, False]), threshold=uniform(0, 100)
            ),
            outlier=zivid.Settings.Filters.Outlier(
                enabled=choice([True, False]), threshold=uniform(0, 100)
            ),
            saturated=zivid.Settings.Filters.Saturated(enabled=choice([True, False])),
            reflection=zivid.Settings.Filters.Reflection(enabled=choice([True, False])),
            gaussian=zivid.Settings.Filters.Gaussian(
                enabled=choice([True, False]), sigma=uniform(0.5, 5)
            ),
        ),
        gain=uniform(1, 16),
        iris=randint(0, 72),
        red_balance=uniform(1, 8),
    )
    yield heavily_modified_settings


@pytest.fixture()
def three_frames(
    application,  # pylint: disable=redefined-outer-name, unused-argument
    sample_data_file,  # pylint: disable=redefined-outer-name
):
    import zivid

    frames = [zivid.Frame(sample_data_file)] * 3
    yield frames
    for fram in frames:
        fram.release()
