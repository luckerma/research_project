import bibtexparser


def clean_bib_file(input_path, output_path):
    with open(input_path) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    relevant_fields = {
        "author",
        "booktitle",
        "date",
        "doi",
        "journal",
        "journaltitle",
        "number",
        "pages",
        "publisher",
        "title",
        "volume",
    }

    cleaned_entries = []
    for entry in bib_database.entries:
        # Skip entries that don't have an ENTRYTYPE
        if "ENTRYTYPE" not in entry:
            print(
                f"Skipping entry with missing ENTRYTYPE: {entry.get('ID', 'Unknown ID')}"
            )
            continue

        # Only keep the year part of the date
        if "date" in entry:
            year = entry["date"].split("-")[0]  # Extract the year part
            entry["date"] = year

        cleaned_entry = {field: entry.get(field, "") for field in relevant_fields}

        cleaned_entry["ENTRYTYPE"] = entry["ENTRYTYPE"]
        cleaned_entry["ID"] = entry["ID"]

        cleaned_entries.append(cleaned_entry)

    bib_database.entries = cleaned_entries

    with open(output_path, "w") as bibtex_file:
        bibtexparser.dump(bib_database, bibtex_file)


input_file = "./resources/references.bib"
output_file = "./resources/references_cleaned.bib"

clean_bib_file(input_file, output_file)
