# Scripts

This folder contains scripts which were used while migrating from website from LAMP to Hugo.

## Folder: `create-md-files-from-json`

This folder contains a Python script and a JSON file. The JSON file is generated from the MySQL export.

### Goal

The goal of the script is to create Markdown files from the JSON data. The frontmatter of the Markdown file should contain the JSON data.

## Folder: `add-year-month-to-frontmatter`

This folder contains a bash script that takes all the markdown files in the current directory and its subdirectories and copies them to a new directory named 'new', while recreating the same folder structure within 'new'. It also extracts the date from the front matter of each file, formats it to 'yyyy/mm', and adds the 'year' and 'month' parameters to the front matter.

### What does the script do (detailed explanation)?

The script starts by creating the 'new' folder if it doesn't exist using the `mkdir` command with the `-p` option.

It then uses the `find` command to search for all the markdown files in the current directory and its subdirectories with the `-name` option, and the `-type f` option specifies that only files should be returned. The output is piped to a `while` loop that reads each file path and performs the following actions:

- It creates the directory structure of the file path in the 'new' folder using the `mkdir` command with the `-p` option, and copies the file to the 'new' folder using the `cp` command.
- It extracts the date from the front matter using the `grep` command with the `-oP` option, which searches for a pattern using Perl regular expressions. The pattern extracts the date parameter from the front matter using a lookbehind and a lookahead assertion. The resulting date is stored in a variable called `date`.
- It extracts the year and month from the date using the `cut` command, which separates text based on a delimiter. The year is extracted by specifying the `-d'-' -f1` option, and the month is extracted by specifying the `-d'-' -f2` option. The resulting values are stored in variables called `year` and `month`, respectively.
- It formats the month value as 'yyyy/mm' by concatenating the `year` variable with a slash and the `month` variable, and overwriting the value of `month` with the resulting string.
- It adds the 'year' and 'month' parameters to the front matter using the `sed` command. The `"/^date:/a"` option specifies that the new lines should be added after the line that matches the regular expression `^date:`, and the variable values are included in the added lines. The `sed` command is applied to the file in the 'new' folder using the `-i` option, which specifies that the changes should be made in-place.
