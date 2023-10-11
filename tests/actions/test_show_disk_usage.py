from pro_filer.actions.main_actions import show_disk_usage
from pro_filer.cli_helpers import _get_printable_file_path  # NOQA


def test_show_disk_usage_files_without(capsys):
    context_file = {"all_files": []}
    show_disk_usage(context_file)
    captured = capsys.readouterr()

    assert captured.out == "Total size: 0\n"


def test_show_disk_files_usages(tmp_path, capsys):
    content_one = "Creatina para abastecer os musculos"
    content_two = "Hello"

    output_file_one = tmp_path / "example_one.txt"
    output_path_two = tmp_path / "example_two.txt"

    output_file_one.touch()
    output_file_one.write_text(content_one)

    output_path_two.touch()
    output_path_two.write_text(content_two)

    context = {"all_files": [str(output_file_one), str(output_path_two)]}

    output_one = f"'{_get_printable_file_path(str(output_file_one))}':".ljust(
        70
    )
    output_two = f"'{_get_printable_file_path(str(output_path_two))}':".ljust(
        70
    )
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert (
        captured.out
        == f"{output_one} 35 (87%)\n\
{output_two} 5 (12%)\nTotal size: 40\n"
    )
