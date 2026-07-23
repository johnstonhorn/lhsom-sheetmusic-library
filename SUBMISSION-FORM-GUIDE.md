# Sheet Music Submission Form - Setup Guide (Microsoft 365)

> **Note:** This guide uses Microsoft Forms and Excel Online, which are part of U of I's Microsoft 365 campus license. This ensures the School of Music can maintain the system without migrating away from Google.

---

## Overview
This guide walks you through creating a Microsoft Form for users to submit newly purchased sheet music, which you can then review and add to the catalog.

---

## Step 1: Create the Microsoft Form

1. Go to **[forms.office.com](https://forms.office.com)** (login with your U of I credentials)
2. Click **+ New form**
3. Title it: **"LHSOM Sheet Music Submission"**
4. Description: *"Submit newly purchased sheet music for the U of I Music Library catalog. All submissions will be reviewed before being added to the public catalog."*

### Add the following questions:

| # | Question | Type | Required | Options/Settings |
|---|----------|------|----------|------------------|
| 1 | **Title of Work** | Text | ✅ Yes | Short answer |
| 2 | **Composer** (Last, First format) | Text | ✅ Yes | Short answer |
| 3 | **Arranger** (if applicable) | Text | No | Short answer |
| 4 | **Ensemble Type** | Choice | ✅ Yes | Dropdown: Wind Ensemble, Orchestra, Choral, Marching Band, Percussion Ensemble, Brass Quintet, Brass Ensembles, Wind Quintet, Trombone Ensemble, Horn Ensemble, Flute Ensemble |
| 5 | **Location** | Choice | ✅ Yes | Dropdown: LHSOM Library, Main Library |
| 6 | **Publisher** | Text | No | Short answer |
| 7 | **Envelope/Call Number** | Text | No | Short answer |
| 8 | **Number of Copies** | Text | No | Short answer (or Number type) |
| 9 | **Score Type** | Choice | No | Dropdown: Full Score, Condensed Score, Oversized, N/A |
| 10 | **Playing Time** | Text | No | Short answer (e.g., "3:45" or "approx. 4 min") |
| 11 | **Missing Parts?** | Choice | No | Dropdown: Yes, No, Not Applicable |
| 12 | **Comments** | Text | No | Long answer / Paragraph |

### Form Settings:
- Click the **three dots (...)** → **Settings**
- **Who can fill out this form**: Choose "Anyone in my organization" (U of I members) or "Specific people" if you prefer
- **Shuffle answers**: ❌ Off (not applicable for this form)
- **One response per person**: ❌ Off (or ✅ On if you prefer)
- **Allow editing of responses**: ✅ Yes

---

## Step 2: View Responses in Excel

Microsoft Forms automatically creates an Excel workbook to store responses:

1. In your Form, click the **Responses** tab
2. Click **Open in Excel**
3. This downloads an Excel file with all responses
4. **Important:** For ongoing use, save this Excel file to **OneDrive** or **SharePoint**:
   - In Excel Online, click **File → Save As → Save to OneDrive/SharePoint**
   - Name it: **"LHSOM Sheet Music Submissions"**
   - This creates a live, always-updated Excel sheet

### Alternative: Link to Excel Online
Some Microsoft Forms setups automatically create an Excel link:
1. In the Responses tab, look for **"Open in Excel"** or **"View in Excel"**
2. Click it and save to your OneDrive/SharePoint
3. This Excel file will **automatically update** as new responses come in

---

## Step 3: Share the Form

1. Click the **Send** button (top right of form)
2. Click the **link icon** (🔗)
3. Choose your audience settings
4. Copy the link
5. Optional: Get an embed code for websites

**Recommended placement:** Add a "Submit New Composition" link to your site's navigation (already configured in the repo).

---

## Step 4: Review Workflow

### Weekly/Bi-weekly Review:
1. Open the **LHSOM Sheet Music Submissions** Excel file (from OneDrive/SharePoint)
2. Review new entries (they appear chronologically, newest at bottom)
3. For each submission:
   - Check for completeness
   - Verify accuracy (composer name format, etc.)
   - Decide: **Approve** or **Reject**

### Approve/Reject System:
Add columns in the Excel sheet:
| Column Name | Purpose |
|-------------|---------|
| **Status** | Mark as "APPROVED", "REJECTED", or leave blank for "Pending" |
| **Notes** | Add notes for rejections or follow-up |
| **Processed** | Mark as "PROCESSED" after adding to catalog (to avoid duplicates) |

**How to add columns:**
1. Open the Excel file in Excel Online or desktop Excel
2. Insert new columns at the end of the table
3. Name them: `Status`, `Notes`, `Processed`
4. As you review, fill in these columns

---

## Step 5: Add Approved Entries to Catalog

Once you have approved entries to add:

### Option A: Manual Export (Simple)
1. In Excel, **filter** the Status column to show only "APPROVED" rows
2. Select those rows, **copy** them
3. Paste into a new Excel file
4. **Save As** → CSV (Comma delimited) → `submissions.csv`
5. Place in `data/` folder of your repo
6. Run: `python3 merge-submissions.py`
7. Commit and push

### Option B: Power Automate (Advanced - Optional)
If you want to automate the process:
1. Use **Power Automate** to trigger when a new response is marked "APPROVED"
2. Append the row to a separate "Approved Submissions" Excel file
3. Use GitHub Actions or a script to merge automatically

*(Let me know if you'd like help setting up Power Automate)*

---

## Step 6: Add "Submit" Link to Site (Optional)

To add a submission link to your site's navigation:

The navigation is already configured in `_data/config-nav.csv`. Just update `pages/submit.md` with your Microsoft Form URL:

1. Edit `pages/submit.md`
2. Replace `YOUR_GOOGLE_FORM_URL_HERE` with your Microsoft Form URL
3. Change "Google Form" references to "Microsoft Form" if desired
4. Commit and push

---

## Microsoft Forms vs Google Forms - Key Differences

| Feature | Microsoft Forms | Google Forms |
|---------|----------------|--------------|
| **Access** | forms.office.com (U of I login) | forms.google.com |
| **Responses** | Excel Online / OneDrive | Google Sheets |
| **Sharing** | Organization-wide or specific people | Anyone or specific people |
| **Export** | Excel (.xlsx) → CSV | Google Sheets → CSV |
| **Embed** | iframe code provided | iframe code provided |
| **Cost** | ✅ Included in Microsoft 365 | ✅ Free |

---

## Notes

- **objectid generation:** The merge script automatically generates unique IDs for new entries
- **Field mapping:** The form fields map directly to CSV columns (see `merge-submissions.py`)
- **Data quality:** Review entries for consistent formatting (especially composer names)
- **Spam protection:** Microsoft Forms has built-in spam filtering
- **U of I Specific:** Since this uses Microsoft 365, it's fully supported by U of IT and can be handed off to School of Music without any migration

---

## Support

- Microsoft Forms help: https://support.microsoft.com/forms
- Excel/OneDrive help: https://support.microsoft.com/office
- CollectionBuilder docs: https://collectionbuilder.github.io/cb-docs/
- U of IT Help Desk: https://www.uidaho.edu/it/contact-it