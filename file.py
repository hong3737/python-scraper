import csv

def save_to_file(file_name, jobs_db):
    #csv : comma separated values
    file = open(f"{file_name}.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow([
            "Title",
            "Company",
            "Link",
            "Platform"
        ])

    for job in jobs_db:
        writer.writerow(job.values())
    file.close()