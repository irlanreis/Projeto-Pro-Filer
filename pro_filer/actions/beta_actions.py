"""Arquivo que estudantes devem editar"""


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = max(
            context["all_files"], key=lambda string: len(string.split("/"))
        )
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []
    search_term_lower = search_term.lower

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if not case_sensitive and search_term_lower in file_name.lower():
            found_files.append(path)

        if case_sensitive and search_term in file_name:
            found_files.append(path)

    return found_files
