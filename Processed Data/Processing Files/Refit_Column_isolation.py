import csv

i = 16

with open(rf"C:\Users\44749\NILM\nilm_analyzer_EM401\refit\House_{i}.csv") as instream:
    # Setup the input
    reader = csv.DictReader(instream)
    rows = list(reader)

    # Setup the output fields
    output_fields = reader.fieldnames
    output_fields.remove("Appliance1")
    output_fields.remove("Appliance2")
    output_fields.remove("Appliance3")
    output_fields.remove("Appliance4")
    output_fields.remove("Appliance5")
    output_fields.remove("Appliance6")
    output_fields.remove("Appliance7")
    output_fields.remove("Appliance8")
    output_fields.remove("Appliance9")

with open(rf"C:\Users\44749\NILM\nilm_analyzer_EM401\Processed Data\refit_H{i}_aggregate.csv", "w") as outstream:
    # Setup the output
    writer = csv.DictWriter(
        outstream,
        fieldnames=output_fields,
        extrasaction="ignore",  # Ignore extra dictionary keys/values
    )

    # Write to the output
    writer.writeheader()
    writer.writerows(rows)