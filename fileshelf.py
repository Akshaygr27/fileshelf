from pathlib import Path
import shutil


# Map each file category to its known file extensions (in lowercase)
CATEGORY_EXTENSIONS: dict[str, set[str]] = {
    "Documents": {".pdf", ".doc", ".docx", ".ppt", ".pptx", ".odt", ".rtf"},
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"},
    "Spreadsheets": {".xls", ".xlsx", ".csv", ".ods"},
    "Text Files": {".txt", ".md", ".log"},
    "Programs": {".py", ".js", ".ts", ".html", ".css", ".java", ".c", ".cpp", ".sh"},
}

ALL_CATEGORIES: list[str] = list(CATEGORY_EXTENSIONS.keys()) + ["Others"]


def get_category(extension: str) -> str:
    """Return the category name for a given lowercase file extension."""
    ext = extension.lower()
    for category, extensions in CATEGORY_EXTENSIONS.items():
        if ext in extensions:
            return category
    return "Others"


def get_unique_destination(dest_folder: Path, filename: str) -> Path:
    """
    Return a non-conflicting destination path inside dest_folder.
    If 'report.pdf' already exists, returns 'report_1.pdf', 'report_2.pdf', etc.
    """
    candidate = dest_folder / filename
    if not candidate.exists():
        return candidate

    base_path = Path(filename)
    stem = base_path.stem
    suffix = base_path.suffix
    counter = 1

    while True:
        new_name = f"{stem}_{counter}{suffix}"
        candidate = dest_folder / new_name
        if not candidate.exists():
            return candidate
        counter += 1


def organise_folder(folder_path_str: str) -> None:
    """Scan a directory and organise top-level files into category folders."""
    # Strip surrounding quotes in case the user pasted a quoted path
    cleaned_path = folder_path_str.strip().strip('"').strip("'")
    target_dir = Path(cleaned_path).expanduser()

    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: '{target_dir}' is not a valid directory.")
        return

    # Track how many files were moved per category
    moved_counts: dict[str, int] = {category: 0 for category in ALL_CATEGORIES}
    skipped_files: list[tuple[str, str]] = []

    # Scan only top-level items; skip subdirectories (including category folders)
    for item in target_dir.iterdir():
        if not item.is_file():
            continue

        category = get_category(item.suffix)
        category_dir = target_dir / category

        try:
            # Create the category folder if it does not already exist
            category_dir.mkdir(parents=True, exist_ok=True)

            # Avoid overwriting files with the same name
            destination_file = get_unique_destination(category_dir, item.name)

            # Move the file
            shutil.move(str(item), str(destination_file))
            moved_counts[category] += 1

        except (PermissionError, OSError, shutil.Error) as exc:
            skipped_files.append((item.name, str(exc)))

    # Display summary
    print("\n--- Organisation Summary ---")
    total_moved = 0
    for category in ALL_CATEGORIES:
        count = moved_counts[category]
        total_moved += count
        print(f"{category:<15}: {count}")

    print("-" * 28)
    print(f"Total files moved: {total_moved}")

    if skipped_files:
        print("\n--- Files That Could Not Be Moved ---")
        for filename, reason in skipped_files:
            print(f"- {filename}: {reason}")


if __name__ == "__main__":
    user_path = input("Enter the folder path to organise: ")
    organise_folder(user_path)