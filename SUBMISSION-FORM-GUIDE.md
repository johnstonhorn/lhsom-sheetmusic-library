# Sheet Music Submission Form - Setup Guide

## Overview
This guide walks you through creating a Google Form for users to submit newly purchased sheet music, which you can then review and add to the catalog.

---

## Step 1: Create the Google Form

1. Go to [forms.google.com](https://forms.google.com)
2. Click **Blank** to create a new form
3. Title it: **"LHSOM Sheet Music Submission"**
4. Description: *"Submit newly purchased sheet music for the U of I Music Library catalog. All submissions will be reviewed before being added to the public catalog."*

### Add the following questions:

| # | Question | Type | Required | Options/Settings |
|---|----------|------|----------|------------------|
| 1 | **Title of Work** | Short answer | ✅ Yes | |
| 2 | **Composer** (Last, First format) | Short answer | ✅ Yes | |
| 3 | **Arranger** (if applicable) | Short answer | No | |
| 4 | **Ensemble Type** | Dropdown | ✅ Yes | Wind Ensemble<br>Orchestra<br>Choral<br>Marching Band<br>Percussion Ensemble<br>Brass Quintet<br>Brass Ensembles<br>Wind Quintet<br>Trombone Ensemble<br>Horn Ensemble<br>Flute Ensemble |
| 5 | **Publisher** | Short answer | No | |
| 6 | **Envelope/Call Number** | Short answer | No | Library shelf location |
| 7 | **Number of Copies** | Short answer | No | |
| 8 | **Score Type** | Dropdown | No | Full Score<br>Condensed Score<br>Oversized<br>(Leave blank if N/A) |
| 9 | **Playing Time** | Short answer | No | Format: MM:SS or "approx. 4 min" |
| 10 | **Missing Parts?** | Multiple choice | No | Yes / No / Not Applicable |
| 11 | **Comments** | Paragraph | No | Condition, notes, purchase date, etc. |

### Form Settings:
- **Collect email addresses**: ✅ Yes (Settings → Responses → Collect email addresses)
- **Limit to 1 response**: ❌ No (or ✅ Yes if you prefer)
- **Allow response editing**: ✅ Yes

---

## Step 2: Link to Google Sheets

1. In the Google Form, click the **Responses** tab
2. Click **"Link to Sheets"** (green Sheets icon)
3. Click **"Create a new spreadsheet"** or select existing
4. Name it: **"LHSOM Sheet Music Submissions"**
5. Click **Create**

This creates a Google Sheet where all form responses are collected automatically.

---

## Step 3: Share the Form

1. Click **Send** button (top right of form)
2. Click the **link icon** (🔗)
3. Check **"Shorten URL"**
4. Copy the link
5. Optional: Embed on a website or share directly via email

**Recommended placement:** Add a "Submit New Composition" link to your site's navigation.

---

## Step 4: Review Workflow

### Weekly/Bi-weekly Review:
1. Open the **LHSOM Sheet Music Submissions** Google Sheet
2. Review new entries (they appear chronologically)
3. For each submission:
   - Check for completeness
   - Verify accuracy (composer name format, etc.)
   - Decide: **Approve** or **Reject**

### Approve/Reject System:
Add a column in the Google Sheet called **"Status"**:
- Leave blank = Pending
- Mark as **"APPROVED"** = Ready to add to catalog
- Mark as **"REJECTED"** = Don't add (add notes in another column if needed)

---

## Step 5: Add Approved Entries to Catalog

Once you have approved entries to add:

1. **Download the current catalog:**
   - Go to your GitHub repo: `johnstonhorn/lhsom-sheetmusic-library`
   - Download `data/entire_library.csv`

2. **Export approved entries from Google Sheets:**
   - Filter the sheet to show only "APPROVED" rows
   - File → Download → CSV

3. **Merge the CSVs:**
   - Use the `merge-submissions.py` script (provided in this repo)
   - Run: `python3 merge-submissions.py`

4. **Commit and push:**
   - The merged `entire_library.csv` is ready
   - `git add data/entire_library.csv`
   - `git commit -m "[data] Add N new compositions from submission form"`
   - `git push origin main`

5. **Mark entries as processed:**
   - In Google Sheets, mark approved entries as "PROCESSED" to avoid duplicates

---

## Step 6: Add "Submit" Link to Site (Optional)

To add a submission link to your site's navigation:

1. Edit `_data/config-nav.csv`
2. Add a row:
   ```
   label,href,target
   Submit New,,,
   ```
3. Or add a button to `index.md` or `pages/about.md`

---

## Automation Option (Advanced)

If you want to automate the merge process:

1. Use **Google Apps Script** to export approved rows as CSV
2. Use **GitHub Actions** to pull the CSV and update the repo automatically
3. Or use a service like **Make.com** or **Zapier** to connect Google Sheets to GitHub

Let me know if you'd like help setting up automation!

---

## Notes

- **objectid generation:** The merge script automatically generates unique IDs for new entries
- **Field mapping:** The form fields map directly to CSV columns
- **Data quality:** Review entries for consistent formatting (especially composer names)
- **Spam protection:** Google Forms has built-in spam filtering

---

## Support

If you need help:
- Google Forms help: https://support.google.com/docs/answer/6281585
- CollectionBuilder docs: https://collectionbuilder.github.io/cb-docs/