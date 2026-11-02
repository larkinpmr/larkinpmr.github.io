---
title: "PM&R Hub — Chief Handoff Guide"
subtitle: "Larkin South Miami PM&R Hub · larkinpmr.github.io"
---

# What the hub is

The hub website (**https://larkinpmr.github.io**) is built from Google Drive. Nobody edits the website itself. You edit the Google files below, and the site updates on its own within a few minutes. It is free and has nothing to renew.

**Hand these to the next chiefs every year:**

- **Chief Gmail:** larkinpmrchief@gmail.com. This account owns every Google file and the script that feeds the site.
- **GitHub account:** `larkinpmr`, signed in with the chief Gmail. It hosts the website. You only need it for design changes.
- Update the chief Gmail's **recovery phone and email** to the new chief's. If 2-step verification is on, move it to the new chief's phone. Losing this account means losing control of the hub.

**The saved copy is public, so it holds nothing private.** The website file that lets the site open instantly (`data/snapshot.json`) contains only the rotation names, the note templates and the "read this first" note. Schedules, guide text, policies and contacts load from Google after sign-in and are kept on each signed-in device. Settings rows with addresses or passcodes (lecture reminder…, invitation…, weekly email…, Zoom passcode) are never sent to the website.

# What controls what

| Google file (in the chief Drive) | What it controls on the site | Who edits it |
|---|---|---|
| **Handbooks** (Drive folder of Google Docs) | Every rotation guide and policy page: one Google Doc per page, including pictures, contacts and links | Residents (quarterly review); chiefs approve |
| **Didactic Schedule** (Google Sheet) | Lectures page, Home "next lecture", the didactics calendar | Chiefs |
| **Resident Schedule** (Google Sheet) | Schedule page, "who is on this rotation", personal cards and calendars, onboarding reminders | Chiefs |
| **Hub Control Panel** (Google Sheet) | Settings, Key Contacts, Quick Links, Announcements, the rotation list, page edits | Chiefs, or through the Chief editor |
| **Hub pictures** (Drive folder) | The pictures from the Handbook that the site shows. **Do not delete or rename it.** It can be moved into another folder. | Nobody: the script fills it |

**Site passcode:** the Control Panel **Settings** tab has a "Site passcode" row. Each phone or computer is asked for it once and then remembered. Change it each year (every device will be asked again); leave it blank to turn the passcode screen off. It keeps casual visitors out but is not real security, so keep patient information out of everything.

**Home page headline:** the Settings tab rows "Home headline" and "Home subtitle" change the big welcome line and the sentence under it. Put *asterisks* around the words that should get the theme color (for example `Everything for the year, *in one place.*`). Leave a row blank for the default; a single `-` hides the subtitle.

**Holiday themes:** on certain days the whole site switches to holiday colors on its own, then back the next day: New Year's (Dec 31–Jan 1), Valentine's Day, Match season (Match Day through March 31), St. Patrick's Day, National Doctors' Day (March 30), graduation week (June 24–30), July 4, Halloween, Thanksgiving (Thursday–Sunday) and Christmas (Dec 24–26). July 1 shows a "Welcome" greeting only. To turn them all off, set the Settings row "Holiday themes" to `off`. To preview one, add `?holiday=halloween` (or match, doctors, thanksgiving, christmas…) to the site address.

**Zoom links for virtual didactics:** the Settings row "Virtual lecture link" holds the usual Zoom link. Every session whose Location says "Virtual" gets a **Join Zoom** button on the site and the link in its calendar event (didactics and personal calendars). For a one-off meeting, add a column named **Meeting link** to the Didactic Schedule and paste that day's link on its first row; it overrides the usual one. Keep a passcode or waiting room on the Zoom meeting, since the calendar links are open.

**Lecture slides upload:** the Settings row **Lecture slides folder** holds the link to the shared Google Drive folder (not in the chief account) where residents put their slides. When it's filled in, the Didactics page shows an **Upload slides** button and the "You've been added" box on Home shows **Upload your slides**. Both simply open that folder, so residents need **edit** access to it (Contributor or above in a shared drive). Leave the row blank to hide the buttons.

**Journal Club and the Didactics page:** sessions marked "Journal Club" in the Didactic Schedule's **Type** column (or with "Journal Club" in the topic) get a teal accent and a book icon. On computers, the Didactics page shows a small calendar of the current month; tap a dotted day to jump to it.

**First-visit tour:** new devices see a 5-step tour of the hub once. Anyone can replay it from the gear menu ▸ "Take a tour".

**Half-month rotations:** to split a month in the Resident Schedule, give that month two columns (insert a column next to it; merge the month header across both, or leave the new header blank). The first column is the 1st–15th, the second starts on the 16th. Residents whose halves differ show both rotations on the site, and "Where everyone is", their personal card and their personal calendar switch on the 16th. Any month can be split, every year, with nothing else to set up.

**Chief editor:** open the gear menu on the site and choose "Chief editor". It only works when you are signed in as the chief Gmail, and it edits the Control Panel tabs without opening the sheet.

# Home page extras

- **Quick links:** the **Quick Links** tab (Label, URL, Note). Home shows 8 of them as small one-line buttons plus an **All links** button; every link is on **Resources ▸ Links**. Two optional columns: **Home** (type `yes` on the links Home should show; without it, the first 8 rows) and **Group** (a heading on the Links page, e.g. Schedules, Forms, ACGME; without it, links are grouped by kind: Sheets, Docs, Drive, Forms, Websites). Put the most-used links first.
- **PTO / Time off:** the hub reads the **chief Google Calendar** (the account's main calendar). Every event whose title has **PTO** and a resident's name (e.g. `PTO – Chris Keener`, `Keener PTO`) appears on **Resident Schedule ▸ Time off** (month calendar on computers, list on phones), as an **Away this week** line at the top of Home (the words link to the calendar), as a small dot on that month in the schedule grid (tap for dates), on that resident's page, and as a small "off today" tag next to their name on Home and on their rotation guide. Only the name, the dates and CME or PTO (CME when the title says CME or conference) are shown; notes and reasons never leave the calendar. Events with no matching resident name are skipped: run **testPTO** to see what was found and what was skipped. First time only: running testPTO asks you to allow Calendar access. Optional Settings rows: **PTO calendar** (a Calendar ID, if PTO is kept on a separate calendar: then every event on it is shown, never skipped; if no resident name matches, the title is shown without its type and anything in brackets) and **PTO keyword** (if events are titled differently, e.g. `Vacation`). Nicknames in quotes in Contacts or Approved Emails (`Bhargavi "Vee" Madhu`) are recognized automatically; add others in a Settings row **Nicknames** (`Vee = Bhargavi Madhu; Rudy = Rodolfo Rivera`). Small spelling slips (Bharghavi) still match.
- **Birthdays:** add a column headed **Birthday** to the private **Approved Emails** tab and type each person's birthday (any format: 3/15, 3/15/1994, March 15). On the day, Home shows "🎂 Happy birthday, …!" to everyone; the person sees their own name. Only the name and month-day ever reach the website, never the year or email.
- **Countdowns:** Settings row **Countdowns**, written `Label = date` and separated by `;` (e.g. `In-training exam = 2/27/2027; Graduation = 6/30/2027`). Home shows "41 days to In-training exam" chips; each disappears after its date.
- **Rotation feedback:** Settings row **Rotation feedback form** = the link to a Google Form. In the last week of a resident's rotation and the week after, their Home shows "How was SA? 2-minute feedback" (Give feedback / Not now). To have the form filled in automatically, use a prefilled-form link with `{rotation}` and `{name}` where the answers go.

# Email sign-in (who can use the hub)

With the Settings row **Email sign-in** set to `on`, the hub has no passcode. The first time someone opens it on a phone or computer, they enter their email and receive a 6-digit code from the chief Gmail; after that, that device stays signed in. Google only sends schedules, contacts and the Handbook to verified devices, so the data is protected at the source, not just hidden. (The saved copy in the public GitHub repo and the calendar links stay open, as decided.)

- **Approved Emails tab** (private): email(s), name, role, Active. Only these emails can get a code; several emails per person are fine, separated by commas. To remove someone, set Active to `no` or delete the row: they are signed out on their next visit (within about a minute).
- **Sign-ins tab** (private): every verified device, when it was last used, and Status. Type `revoked` in Status to sign out one device (a lost phone, say). Don't edit the Key column.
- **New academic year:** changing "Academic Year" in Settings makes every device verify once more.
- **Turning it off:** set "Email sign-in" to `off`; the old passcode screen (Settings "Site passcode") applies again.
- **Residents don't need to pick their name:** once signed in, Home shows their own rotation and lectures, as long as their name on the Approved Emails tab matches the Resident Schedule (first + last name).
- **"You've been added" box:** when a resident's name appears on a didactics row (or one of their talks moves), Home shows a highlighted box with the talk until they tap **Got it**. No email is sent, by design.
- Setup (once): run **installSignIn** to create the two tabs, fill in Approved Emails, then set "Email sign-in" to `on`. Codes are limited to 5 an hour per email and expire after 15 minutes; 5 wrong tries cancel a code.

# Editing the Handbooks (the rules that keep the site working)

The **Handbooks** folder holds one Google Doc per page. Its link is in the Control Panel **Settings** tab next to "Handbooks Folder".

- **The doc's name is the page title.** Rename the doc to rename the page.
- **The folder is the group** it appears under on the Rotation Guides page (Inpatient Rehab, Consult Service, Outpatient, EMG/EDX, Neurorehab, Elective). Move a doc to move it on the site. A new folder makes a new group.
- **Policies** go in the **Policies** folder and appear under Resources.
- **"Note shown on every rotation"** (in the Handbooks folder itself) appears at the top of every rotation guide. "How to edit these Handbooks" is instructions only.
- **To add a rotation:** in the right folder, open an existing guide and use File ▸ Make a copy (keeps the look), rename it, and write the guide. It appears on the site automatically. To give it a **schedule code** (so it shows in the resident schedule, "who's on this rotation" and personal calendars), add a row in the Control Panel **Rotations** tab with **exactly the same name** as the doc.
- **To remove a rotation:** move its doc to the trash (and delete its Rotations-tab row if it has one).
- **"Last updated" is automatic.** Each guide and policy page shows the date and time its doc was last edited in Drive (plus a "Recently updated" tag for a week), so don't type update dates into the docs. Any edit moves it, even a small typo fix.
- Red text stays red on the site. Use it for warnings and "⚠ Confirm" notes. Pictures, tables and links all carry over; tapping a picture on the site makes it full screen.
- Keep patient information out. The website and its code are public.
- Use **Suggesting** mode for big changes, so the chiefs can review them.
- The old single "PM&R Program Handbook" doc is an archive: edits there no longer reach the site.

# Guest lecturer reminder emails

Every morning around 8 AM the chief Gmail checks the Didactic Schedule and emails each guest lecturer a week before their lecture, with the topic, date, time (2–4 PM is shown as flexible), virtual or in person, the Zoom link or location, and Google/Outlook/Apple calendar buttons. Residents never get these.

**Setup (once):**

1. In the Control Panel **Settings** tab add two rows: `Lecture reminders` = `test`, and `Lecture reminder test email` = the address that should receive test copies.
2. In Apps Script, run **installLectureReminders** and click Allow when Google asks to send email. It creates the **Lecturers**, **Lecture Reminders** and **Lecture Locations** tabs and turns on the daily check.
3. **Lecturers tab:** one row per guest: name exactly as written in the Didactic Schedule's speaker column, email (several are fine, separated by commas: every email goes to all of them), other spellings (e.g. `Dr. Kahn; Stuart Kahn`), and "yes" under Send reminders.
4. Run **previewLectureReminders** (who gets what, when; sends nothing) and **sendTestReminder** (two sample emails to the test address).
5. When the test emails look right, change `Lecture reminders` to `on`. Use `off` to pause everything.

**What happens automatically:**

- **Test mode** (`test`, or blank): every reminder goes to the test address instead, marked with who it would have gone to.
- **No duplicates:** every email is logged on the **Lecture Reminders** tab (and in the Gmail Sent folder).
- **Moved lecture:** the lecturer gets a new reminder that says the date changed.
- **Canceled lecture:** if a reminded lecture disappears from the sheet or is marked "Canceled", the chief Gmail gets an alert to contact the lecturer personally (no automatic email to them).
- **Missing emails:** every Monday the chief Gmail gets a list of guest lectures in the next 3 weeks whose speaker isn't on the Lecturers tab. Run **checkLecturerEmails** any time for the same list.
- **Failures:** if an email can't be sent, the chief Gmail is told the same morning.
- The Lecturers, Lecture Reminders and Lecture Locations tabs, and the "Lecture reminder…" Settings rows, are never sent to the website. **Lecture Locations** turns sheet shorthand into something a guest understands ("Larkin South" → "Larkin South, G&E building, 4th floor", plus an optional address that becomes a directions link).

Other Settings rows: **Lecture reminder days** (`7`, or `7, 1` for a week before and the day before), **Didactics start time** (blank = 2:00 PM), **Guest lecture length (hours)** (blank = 2), **Virtual lecture link**, **Lecture reminder signature** (leave blank: every reminder and invitation is signed "Physical Medicine & Rehabilitation Chief Residents" + the Academic Year, the hospital, the chief email, and each chief's name and cell from the Contacts tab, so it updates itself when the Contacts tab changes in July).

# Inviting guest lecturers

The private **Invitations** tab in the Control Panel turns a row into a ready-to-edit invitation in the chief Gmail's **Drafts** folder. Nothing is sent until you open the draft and press Send.

1. **Once:** in Apps Script, run **installInvitations** (click Allow if Google asks about Gmail). It creates the tab.
2. Fill in a row: name, email, topic (optional), proposed dates (optional, separated by `;`, e.g. `12/14/2026; Jan 11`), and format (virtual, in person or either).
3. Type **yes** under "Create draft?". Within a few seconds the draft is in Gmail ▸ Drafts and the Status column says so. Each row makes one draft, once.
4. Open the draft, personalize it, and send. Replies come to the chief Gmail.

If "Proposed dates" is blank, the draft suggests the next few Monday didactics (2–10 weeks out) that don't have a guest speaker yet. When someone says yes, add them to the Didactic Schedule and the **Lecturers** tab; the 7-day reminder then happens on its own.

**Invitation drafts (the first ask):** the Didactic Schedule's **Confirmed** column decides what each guest lecture gets: `yes` or `confirmed` → the 7-day reminder; blank → an invitation draft (and no reminder); anything else (`rescheduled`, `declined`…) → nothing at all. Every Monday morning, the script looks up to 6 weeks ahead for guest lectures (speakers who aren't residents) that aren't marked Confirmed and haven't been invited, creates an invitation draft for each in Gmail ▸ Drafts ("would you be available on [date], 2–4 PM? if not, another date in [month]?"), lists them on the Invitations tab with the block theme and same-day resident lectures as a note for the chiefs, and emails the chief Gmail that drafts are ready. The guest's email is filled in when they're on the Lecturers tab; otherwise add it in the draft. Run **draftUpcomingInvitations** to do it right away. Settings rows: **Invitation lead (weeks)** (blank = 6), **Invitation drafts** (`off` to stop the Monday drafts; the older name **Automatic invitations** still works). Nothing is ever sent automatically: every invitation waits in Drafts for a chief to send. Each invitation ends with "Thank you," and a highlighted **[Your name]** for the chief who sends it, followed by the chief Gmail's own default signature (Gmail ▸ Settings ▸ Signature), so next year's signature carries over by itself. Lecture reminders use the same signature. Reminders go only to lecturers marked yes/confirmed; a lecture still blank a week out triggers an alert to the chiefs instead.

**Guide pages:** each rotation guide shows a **First day** card (the first address in the doc, tap for directions, and the first phone numbers) and a **Jump to** menu built from its section titles (headings, or short lines that are entirely bold, like "Responsibilities:"). Both come from the doc itself, so editing the Handbooks doc updates them. Inpatient guides and the Rotation Guides page show the "Starting an inpatient rotation? Read this first" banner, which opens the readiness note. On Home, "Onboarding due" shows only your own row once you pick your name ("Show everyone" expands it); Didactics shows the next 4 weeks first ("Show the rest of the year" for more). The gear menu has **Home screen setup**: save the hub as an app, subscribe to the didactics and personal calendars, and add the phone's Calendar widget (real home-screen widgets would need a paid native app, so this uses the calendar widget instead).

# Weekly Sunday email (a draft, never sent automatically)

Every Sunday around 7 AM, a draft of the weekly email to all residents appears in **Gmail ▸ Drafts**, and the chief Gmail gets a note that it's ready. Open it, check it, and press **Send**.

What's in it, in this order:
- A greeting (it rotates each week through the **greeting** rows on the Weekly Email tab) and the **standing messages** (case logs and work hours…).
- **DIDACTICS UPDATE**: the week's Monday (and Thursday) sessions, written out: "Didactics this Monday (11/16) will be held virtually at 2:00 PM" with each lecture and presenter, then the Zoom link, meeting ID and passcode (Settings **Virtual lecture link** and **Zoom passcode**), or the in-person location and address (Lecture Locations tab). A week whose only row says "No Didactics" or "Holiday Break" becomes "There will be no didactics this week (Labor Day)." Then a link to the hub's didactic calendar.
- **WEEKLY UPDATES**: this week's updates, a good-luck line when rotations switch that week, the SAE countdown (the Settings **Countdowns** entry whose name has SAE or in-training), and birthdays that week.
- **REMINDER HELPFUL LINKS** with the PTO protocol (PTO forms go to **Carola**, the program coordinator), a small **PM&R Hub** button (Settings **Hub link** changes the address), and the chief Gmail's own signature.

The subject follows the usual style: "Virtual Didactics 11/02", "Didactics at ISS 11/09", "Didactics 11/16 & 11/19", "No Didactics 09/07".

**Weekly Email tab** (private): one row per line. Type **greeting** (one per row; a different one is used each week), **standing** (every week), **update** (used in the next Sunday draft only; give a **Show until** date to keep it longer), **link** (label, link, note; `{year}` becomes the academic year) and **pto step** (the bullets under the PTO form). `**bold**` and `*italic*` work. Run **draftWeeklyEmail** to make (or remake) the draft any time; remaking replaces that week's earlier draft.

**Who gets it:** the Google Contacts labels **2027 Class**, **2028 Class** and **2029 Class** in the chief account, addressed directly (no BCC). They move up by themselves when the Academic Year changes in July. Settings **Weekly email to** replaces them (labels or addresses), **Weekly email also to** adds people, **Weekly email CC** copies people (e.g. the program director and coordinator; **Weekly email BCC** for blind copies), **Weekly email** = `off` pauses it. If a label can't be found, the draft uses the residents on the Approved Emails tab and the note says so.

**One-time setup:** in Apps Script, click **+** next to **Services**, add **People API** (reads the class labels), then click + again and add **Gmail API** (reads the chief signature). Then run **installWeeklyEmail** (creates the tab and the Sunday schedule) and **draftWeeklyEmail** to see this week's draft.

# Applicant page (larkinpmr.github.io/apply)

A lean public page for interview season: header, quick stats, "Why Larkin PM&R" highlights, rotation cards (site, city, PGY, one line each, with a PGY filter), a typical week, interview day and where graduates went. It shows **only** the Control Panel's **Applicant Page** tab: no resident names, schedules, contacts or Handbook, and it needs no sign-in.

- Setup (once): run **installApplicantPage**. It creates the tab with a starter draft (the stats, highlights and blurbs are a draft: check them).
- One row per item; the **Section** column says what it is: Headline (text between *asterisks* gets the gradient), Subtitle, Stat (number + label), Highlight (title, starting with an emoji if you like, + text), Rotation (name, blurb, Where, PGY, Group), Week (day + text; *asterisks* highlight that day), Interview (time + what), Graduate (class year + where they went), Contact email.
- **Show page** row: `on` = applicants see it; `off` = "coming soon". Check edits first at larkinpmr.github.io/apply/?preview. Changes appear within about 5 minutes.
- `data/apply.json` in the repo is the saved copy used if Google is unreachable (it starts as the draft, with the page off).

# Start of each academic year (July)

Everything runs from the **PM&R Hub** menu at the top of the Control Panel sheet:

1. **PM&R Hub ▸ Start a new academic year.** It asks for the new year (e.g. 2027-2028) and, optionally, links to new schedule sheets you already made. Otherwise it copies this year's Didactic and Resident Schedule sheets for you, points Settings at the new sheets, sets the Academic Year (every device verifies its email once more), and turns off sign-in for the graduating residents (the highest PGY on the old Resident Schedule). Run it when the new year should go live, usually July 1.
2. **PM&R Hub ▸ Open the yearly checklist.** The **Yearly Checklist** tab lists the remaining human steps with tick boxes, and resets each year:
   - fill in the new schedules
   - new residents on Approved Emails
   - new chiefs in Contacts and in the chief Gmail signature
   - the incoming class's contact label (e.g. "2030 Class")
   - the new contact list link on the Weekly Email tab
   - Lecturers
   - Handbook review and the link check
   - handing over the chief Gmail (recovery phone and email, 2-step verification)
3. **PM&R Hub ▸ Check that everything is working**, and fix anything it lists.

Also check the **Rotations** tab codes match the codes used in the new Resident Schedule (any code the site doesn't recognize shows as plain text).

# Quarterly Handbook review

1. Residents update their rotation docs in the Handbooks folder. Chiefs accept or reject suggestions.
2. Resolve every red **"⚠ Confirm"** note: either fix the fact or delete the note.
3. In Apps Script, run **checkHandbookLinks**. Fix broken links in the Handbook. For "Private" links, open the Drive file and set sharing to "Anyone with the link".
4. Run **refreshHandbookNow** so the site picks up the changes right away.

# The PM&R Hub menu

Open the **Hub Control Panel** sheet: the **PM&R Hub** menu sits next to Help. Every item shows its result in a box. You only open **Extensions ▸ Apps Script** to paste new code.

| Menu item | What it does |
|---|---|
| **Draft this week's email now** | Makes (or remakes) this week's weekly email draft in Gmail ▸ Drafts |
| **Draft lecture invitations now** | Invitation drafts for unconfirmed guest lectures in the next 6 weeks (never duplicates) |
| **Refresh the Handbook on the site now** | After editing a Handbooks doc, if you don't want to wait the ~5 minutes |
| **Check that everything is working** | Lists what's fine (✓) and what needs fixing (⚠), with how to fix it |
| **Set up / repair automatic tasks** | Turns on (or restarts) every automatic task: 5-minute data refresh, daily lecture reminders and Monday invitation drafts, Sunday weekly email, Monday health check. Safe to run any time |
| **Start a new academic year…** | The July switch (see above) |
| **Open the yearly checklist** | The Yearly Checklist tab |
| **More ▸** | Preview lecture reminder emails · Send two test reminders · Check every link in the Handbook · Show what the site reads · Show the PTO the hub found · Rewrite the "How to update" tab |

**Monday health check:** every Monday at 9 AM the hub checks itself and emails the chief Gmail **only if something needs fixing**, for example:
- a stopped automatic task
- a Services switch turned off
- last year's Academic Year
- a schedule sheet it can't open, or no lectures in the next 8 weeks
- a missing class contact label
- no Gmail signature

No email means all is well.

The same functions can still be run from the Apps Script editor (refreshHandbookNow, testHub, draftWeeklyEmail, draftUpcomingInvitations, checkHandbookLinks, testPTO, installAutoRefresh…), but the menu covers them all.

**If you ever paste new code into Code.gs or Admin.html:** click **Deploy ▸ Manage deployments**. For **each** of the two deployments, click the pencil, set Version to **New version**, and click **Deploy**. Without this, the site keeps running the old code. The links stay the same. Then reload the Control Panel sheet so the **PM&R Hub** menu shows the latest items.

# When something looks wrong

| What you see | What to do |
|---|---|
| Anything odd, or an email from the hub saying something needs fixing | **PM&R Hub ▸ Check that everything is working**; for anything automatic, **PM&R Hub ▸ Set up / repair automatic tasks** |
| Site footer says **"Saved copy"** | Google could not be reached. Use **PM&R Hub ▸ More ▸ Show what the site reads** and read the "Errors" line. Most often a file link in Settings is wrong, or the file is not in the chief Drive. |
| A Handbook change isn't on the site after 10 minutes | **PM&R Hub ▸ Refresh the Handbook on the site now**, then reload the site (⌘+Shift+R or Ctrl+Shift+R). |
| A guide is missing, shows up twice, or has no schedule code | The doc name and the Rotations-tab name must match exactly (spaces and dashes are forgiven). Check the doc is a Google Doc (not a Word file) inside a folder in Handbooks. |
| A picture is missing | Run **refreshHandbookNow** and read the "Picture problem" line, if any. Make sure the **Hub pictures** folder still exists. |
| Chief editor says "Sorry, unable to open the file" | You are signed into more than one Google account. Use a private window signed in only as the chief Gmail. |
| Script asks for permission again | Click Allow with the chief account. Google sometimes asks after code changes. |

# Design changes and the backup copy

The website's look and layout live in the GitHub repository **larkinpmr/larkinpmr.github.io** (one file, `index.html`). The repo has notes for Claude (`CLAUDE.md`), so the easiest way to change the design is to open Claude, connect the repo, and describe what you want.

The site also keeps a **saved copy** of all content in the repo (`data/snapshot.json`), shown instantly and used if Google is down. After big changes, ask Claude to "rebuild the hub's saved copy" and give it the Handbooks folder downloaded from Drive (right-click ▸ Download; Drive turns the docs into Word files in a .zip). Also download the Resident Schedule and Didactic Schedule (File ▸ Download ▸ Microsoft Excel). The tools for this are `tools/build_snapshot.py` (Handbooks) and `tools/build_schedules.py` (schedules).
