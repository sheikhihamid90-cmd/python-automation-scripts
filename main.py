import argparse
from pathlib import Path
import csv


def word_count(file_path: str) -> None:
    path = Path(file_path)
    if not path.exists():
        print('File not found.')
        return

    text = path.read_text(encoding='utf-8')
    words = text.split()
    print(f'Word count: {len(words)}')


def bulk_rename(folder_path: str, prefix: str) -> None:
    folder = Path(folder_path)
    if not folder.exists() or not folder.is_dir():
        print('Folder not found.')
        return

    files = [file for file in folder.iterdir() if file.is_file()]
    if not files:
        print('No files found.')
        return

    for index, file in enumerate(files, start=1):
        new_name = f'{prefix}_{index}{file.suffix}'
        file.rename(folder / new_name)
    print(f'Renamed {len(files)} files.')


def csv_summary(file_path: str) -> None:
    path = Path(file_path)
    if not path.exists():
        print('CSV file not found.')
        return

    with path.open('r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        print('CSV is empty.')
        return

    print(f'Rows: {len(rows) - 1}')
    print(f'Columns: {len(rows[0])}')
    print(f'Headers: {", ".join(rows[0])}')


def main() -> None:
    parser = argparse.ArgumentParser(description='Python automation scripts collection')
    subparsers = parser.add_subparsers(dest='command')

    wordcount_parser = subparsers.add_parser('wordcount', help='Count words in a text file')
    wordcount_parser.add_argument('file')

    rename_parser = subparsers.add_parser('rename', help='Rename files in a folder')
    rename_parser.add_argument('folder')
    rename_parser.add_argument('prefix')

    csv_parser = subparsers.add_parser('csv-summary', help='Summarize a CSV file')
    csv_parser.add_argument('file')

    args = parser.parse_args()

    if args.command == 'wordcount':
        word_count(args.file)
    elif args.command == 'rename':
        bulk_rename(args.folder, args.prefix)
    elif args.command == 'csv-summary':
        csv_summary(args.file)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
