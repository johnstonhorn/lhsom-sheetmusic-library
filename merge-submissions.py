#!/usr/bin/env python3
"""
Merge approved sheet music submissions from Google Sheets into the main catalog.

Usage:
    python3 merge-submissions.py

This script:
1. Reads the main catalog (data/entire_library.csv)
2. Reads approved submissions (data/submissions.csv - export from Google Sheets)
3. Merges them, generating unique objectids
4. Outputs the merged catalog to data/entire_library.csv
"""

import csv
import os
from datetime import datetime

# Configuration
CATALOG_FILE = "data/entire_library.csv"
SUBMISSIONS_FILE = "data/submissions.csv"  # Export approved rows from Google Sheets
OUTPUT_FILE = "data/entire_library.csv"

# Column mapping (form question → CSV header)
COLUMN_MAPPING = {
    "Title of Work": "title",
    "Composer": "Composer",
    "Arranger": "Arranger",
    "Ensemble Type": "Library",
    "Publisher": "Publisher",
    "Envelope/Call Number": "Envelope",
    "Number of Copies": "Copies",
    "Score Type": "Score Type",
    "Playing Time": "PlayingTime",
    "Missing Parts?": "Missing Parts?",
    "Comments": "Comments"
}

# Master headers (matching existing catalog format)
MASTER_HEADERS = [
    'objectid', 'Library', 'Composer', 'Arranger', 'title', 'Drawer',
    'Envelope', 'Copies', 'Score Type', 'Publisher', 'Performance Date',
    'PlayingTime', 'Score (Full/Cond/Oversized)', 'Missing Parts?', 'Comments'
]


def load_catalog():
    """Load the existing catalog and return rows and the highest objectid number."""
    if not os.path.exists(CATALOG_FILE):
        print(f"Warning: {CATALOG_FILE} not found. Starting fresh.")
        return [], 0

    with open(CATALOG_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Find the highest objectid number
    max_id = 0
    for row in rows:
        obj_id = row.get('objectid', '')
        if obj_id.startswith('id_'):
            try:
                num = int(obj_id[3:])
                max_id = max(max_id, num)
            except ValueError:
                pass

    return rows, max_id


def load_submissions():
    """Load approved submissions from Google Sheets export."""
    if not os.path.exists(SUBMISSIONS_FILE):
        print(f"No submissions file found at {SUBMISSIONS_FILE}")
        print("Place your Google Sheets export as 'data/submissions.csv'")
        return []

    with open(SUBMISSIONS_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Loaded {len(rows)} submissions from {SUBMISSIONS_FILE}")
    return rows


def map_submission(submission, start_id):
    """Map a Google Forms submission to catalog format."""
    mapped = {h: '' for h in MASTER_HEADERS}

    # Map form fields to CSV headers
    for form_field, csv_header in COLUMN_MAPPING.items():
        value = submission.get(form_field, '').strip()
        if value:
            mapped[csv_header] = value

    # Handle special cases
    # Convert "Yes/No" to proper format for Missing Parts?
    if mapped['Missing Parts?'] == 'Yes':
        mapped['Missing Parts?'] = 'Yes'
    elif mapped['Missing Parts?'] == 'No':
        mapped['Missing Parts?'] = 'No'

    # Generate objectid
    mapped['objectid'] = f'id_{start_id}'

    return mapped


def main():
    print("=" * 60)
    print("Sheet Music Catalog Merge Tool")
    print("=" * 60)

    # Load existing catalog
    print(f"\nLoading catalog from {CATALOG_FILE}...")
    catalog, max_id = load_catalog()
    print(f"Found {len(catalog)} existing entries (highest ID: id_{max_id})")

    # Load submissions
    print(f"\nLoading submissions from {SUBMISSIONS_FILE}...")
    submissions = load_submissions()

    if not submissions:
        print("\nNo submissions to process. Exiting.")
        return

    # Merge submissions into catalog
    new_entries = []
    next_id = max_id + 1

    for submission in submissions:
        mapped = map_submission(submission, next_id)
        new_entries.append(mapped)
        print(f"  Mapped: '{mapped['title']}' by {mapped['Composer']} → {mapped['objectid']}")
        next_id += 1

    # Combine all entries
    all_entries = catalog + new_entries

    # Write merged catalog
    print(f"\nWriting merged catalog to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=MASTER_HEADERS)
        writer.writeheader()
        for entry in all_entries:
            writer.writerow(entry)

    print(f"\n✓ Complete!")
    print(f"  - Existing entries: {len(catalog)}")
    print(f"  - New entries added: {len(new_entries)}")
    print(f"  - Total entries: {len(all_entries)}")
    print(f"  - Next available ID: id_{next_id}")

    # Summary of new entries
    if new_entries:
        print("\nNew entries summary:")
        libraries = {}
        for entry in new_entries:
            lib = entry.get('Library', 'Unknown')
            libraries[lib] = libraries.get(lib, 0) + 1
        for lib, count in sorted(libraries.items()):
            print(f"  {lib}: {count}")

    print("\nNext steps:")
    print("1. Review the merged catalog in data/entire_library.csv")
    print("2. Commit the changes: git add data/entire_library.csv")
    print("3. Commit with message: '[data] Add N new compositions from submission form'")
    print("4. Push to GitHub: git push origin main")
    print("5. Mark processed entries as 'PROCESSED' in your Google Sheet")


if __name__ == "__main__":
    main()