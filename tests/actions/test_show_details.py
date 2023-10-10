from unittest.mock import Mock, patch

import pytest
from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details_file_error(capsys):
    path_exists_os_mock = Mock(return_value=False)
    file_context_fake = {"base_path": "/home/test/!!!!"}

    with patch("os.path.exists", path_exists_os_mock):
        show_details(file_context_fake)
        captured = capsys.readouterr()

        assert captured.out == "File '!!!!' does not exist\n"


@pytest.mark.parametrize(
    "context, name,size, type, extension, date",
    [
        (
            {"base_path": "/home/test/Downloads/Trybe_logo.png"},
            "File name: Trybe_logo.png\n",
            "File size in bytes: 100\n",
            "File type: file\n",
            "File extension: .png\n",
            "Last modified date: 2019-05-21\n",
        ),
    ],
)
def test_show_details_found_file(
    capsys, context, name, size, type, extension, date
):
    path_exists_os_mock = Mock(return_value=True)
    path_getsize_os_mock = Mock(return_value=100)
    path_isdir_os_mock = Mock(return_value=False)
    path_splitext_os_mock = Mock(return_value=("Trybe_logo", ".png"))
    path_getmtime_os_mock = Mock(return_value=1558447897.0442736)

    with (
        patch("os.path.exists", path_exists_os_mock),
        patch("os.path.getsize", path_getsize_os_mock),
        patch("os.path.isdir", path_isdir_os_mock),
        patch("os.path.splitext", path_splitext_os_mock),
        patch("os.path.getmtime", path_getmtime_os_mock),
    ):
        show_details(context)
        captured = capsys.readouterr()

        assert name in captured.out
        assert size in captured.out
        assert type in captured.out
        assert extension in captured.out
        assert date in captured.out


@pytest.mark.parametrize(
    "context, name, size, type, extension, date",
    [
        (
            {"base_path": "/home/test/Downloads"},
            "File name: Downloads\n",
            "File size in bytes: 500\n",
            "File type: directory\n",
            "File extension: [no extension]\n",
            "Last modified date: 2019-05-21\n",
        ),
    ],
)
def test_show_details_found_directory(
    capsys, context, name, size, type, extension, date
):
    path_exists_os_mock = Mock(return_value=True)
    path_getsize_os_mock = Mock(return_value=500)
    path_isdir_os_mock = Mock(return_value=True)
    path_splitext_os_mock = Mock(return_value=("Downloads", ""))
    path_getmtime_os_mock = Mock(return_value=1558447897.0442736)

    with (
        patch("os.path.exists", path_exists_os_mock),
        patch("os.path.getsize", path_getsize_os_mock),
        patch("os.path.isdir", path_isdir_os_mock),
        patch("os.path.splitext", path_splitext_os_mock),
        patch("os.path.getmtime", path_getmtime_os_mock),
    ):
        show_details(context)
        captured = capsys.readouterr()

        assert name in captured.out
        assert size in captured.out
        assert type in captured.out
        assert extension in captured.out
        assert date in captured.out
