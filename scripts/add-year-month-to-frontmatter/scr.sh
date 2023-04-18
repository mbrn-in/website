#!/bin/bash

# create the 'new' folder if it doesn't exist
mkdir -p new

# loop through all markdown files in the current directory and its subdirectories
find . -name '*.md' -type f | while read file; do
    # copy the file to the 'new' folder with the same folder structure
    mkdir -p "new/$(dirname "$file")"
    cp "$file" "new/$file"

    # extract the date and year from the front matter
    date=$(grep -oP 'date: \K.*(?=\s\d{2}:\d{2}:\d{2})' "new/$file")
    year=$(echo "$date" | cut -d'-' -f1)

    # extract the year and day from the date parameter
    day=$(echo "$date" | cut -d'-' -f3)
    month=$(echo "$date" | cut -d'-' -f2)

    # format the month parameter value as 'yyyy/mm'
    month="$year/$month"

    # add the 'year' and 'month' parameters to the front matter
    sed -i "/^date:/a year: $year" "new/$file"
    sed -i "/^date:/a month: $month" "new/$file"
done
