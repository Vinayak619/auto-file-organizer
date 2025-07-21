import os
import pytest
from project import file_list, category
'''
check weather the files are listed correctly, the categories are assigned properly and weather the file moved to the correct folder
'''


@pytest.fixture
def sample_folder(tmp_path):
    files = ["img.jpg", "notes.pdf", "song.mp3", "clip.mp4", "unknown.xyz"]
    for file in files:
        (tmp_path / file).write_text("dummy")
    return tmp_path

def test_move_file(sample_folder):
    from project import move_file
    files = file_list(sample_folder)
    move_file(files, sample_folder)
    assert (sample_folder / "Images" / "img.jpg").exists()
    assert (sample_folder / "Documents" / "notes.pdf").exists()
    assert (sample_folder / "Music" / "song.mp3").exists()
    assert (sample_folder / "Videos" / "clip.mp4").exists()
    assert (sample_folder / "Others" / "unknown.xyz").exists()


def test_file_list(sample_folder):
    result = file_list(sample_folder)
    assert len(result) == 5
    assert all(os.path.isfile(f) for f in result)

def test_category():
    assert category("photo.jpg") == "Images"
    assert category("report.pdf") == "Documents"
    assert category("music.mp3") == "Music"
    assert category("movie.mkv") == "Videos"
    assert category("something.unknown") == "Others"
