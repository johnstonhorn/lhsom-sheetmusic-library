# Sheet Music Submission Form - Quick Start

This document provides a quick overview of the submission form setup. For detailed instructions, see [SUBMISSION-FORM-GUIDE.md](SUBMISSION-FORM-GUIDE.md).

---

## What You Need to Do

### 1. Create the Google Form (15 minutes)

1. Go to [forms.google.com](https://forms.google.com)
2. Create a new blank form
3. Title: **"LHSOM Sheet Music Submission"**
4. Add the 11 questions listed in [SUBMISSION-FORM-GUIDE.md](SUBMISSION-FORM-GUIDE.md)
5. Link responses to a Google Sheet
6. Copy the form URL

### 2. Update the Submit Page

1. Open `pages/submit.md`
2. Replace `YOUR_GOOGLE_FORM_URL_HERE` with your actual Google Form URL
3. Optionally update the contact email
4. Commit and push

### 3. Test the Form

1. Fill out a test submission
2. Verify it appears in your Google Sheet
3. Check that all fields map correctly

### 4. Add Approved Entries to Catalog

When you have submissions to add:

1. Export approved rows from Google Sheets as CSV
2. Save as `data/submissions.csv`
3. Run: `python3 merge-submissions.py`
4. Review the merged `data/entire_library.csv`
5. Commit and push to GitHub

---

## Files Created

| File | Purpose |
|------|---------|
| `pages/submit.md` | Submit page on the site (embeds Google Form) |
| `merge-submissions.py` | Python script to merge submissions into catalog |
| `SUBMISSION-FORM-GUIDE.md` | Detailed setup and workflow guide |
| `data-form-setup.md` | This quick-start overview |

---

## Navigation

The "Submit" link has been added to the site navigation. It will appear in the main menu alongside Home, Browse, Clouds, Table, and About.

---

## Next Steps

1. **Create the Google Form** using the guide
2. **Update `pages/submit.md`** with your form URL
3. **Test the workflow** with a sample submission
4. **Go live!** Share the submit link with your team

---

## Support

If you run into issues:
- Check the detailed guide: [SUBMISSION-FORM-GUIDE.md](SUBMISSION-FORM-GUIDE.md)
- Google Forms help: https://support.google.com/docs/answer/6281585