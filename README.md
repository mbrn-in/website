# Multimedia website

[![Netlify Status](https://api.netlify.com/api/v1/badges/6b092cd3-e286-499f-8708-64d531a2f8b7/deploy-status)](https://app.netlify.com/sites/mbrn-in/deploys)

This repo contains source code for the mbrn.in website.

## Tech stack

- Hugo - static site generator
- Bootstrap & CSS - style & responsive design
- Netlify - static hosting

## Where to add thumbnails?

Please don't touch the `public` folder. It's an automatically generated directory.
You've no thing to do with it.

- Add the thumbnails in `static\images\thumbnails` folder.
- Images can be added as png/jpg, .webp conversion is taken care automatically.
- Ensure that there are no spaces in the names of images. Either use hyphens or underscores. For example: `guru-purnima-2025.png`.

## Steps to add an event:

1. Open GitHub Desktop and fetch origin.
2. Switch back to Visual Studio Code.
3. In the terminal, run `git pull` to sync with the latest changes.
4. Create a new branch using `git checkout -b <name-of-the-branch>`.
5. Navigate to the content folder.
6. Go to the desired year folder.
7. Create the event markdown file with the .md extension: `<filename/slug>.md`.
8. Add and fill in the required details such as title, date, month, and year.
The title should be in this format: `<event-name> photos/videos year`
Eg: `independence day photos 2025`
9. Add the category of the event (photo, video, or audio).
10. Add the required thumbnail image with the specified dimensions. Ensure that image has .jpg/png extension not .JPG/PNG (uppercase).
11. Include a short description and a long description of the event.
12. Add the YouTube link or Drive link or OneDrive link.
13. Verify the changes locally by running the command `hugo server --navigateToChanged` in the terminal.
14. If everything is correct, commit and push the changes to the **newly created** branch.
15. Create a pull request and merge the branch into the main repository.
