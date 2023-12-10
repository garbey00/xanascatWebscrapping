#!/bin/sh

# Loop from 0 to 38
for i in {0..38}; do
    # Define the URL you want to download (replace <URL_TEMPLATE> with your actual URL template)
    url="https://xanascat.gencat.cat/ca/programes/vacances-en-familia/primera-convocatoria-2024?field_hostel_target_id_verf=All&field_taxon_stay_type_target_id=All&page=$i"

    # Define the output file name (adjust as needed)
    output_file="file_$i.txt"

    # Use wget to download the file
    wget "$url" -O "$output_file"

    # Optional: Add a sleep to avoid overwhelming the server with too many requests in a short time
    sleep 1
done




