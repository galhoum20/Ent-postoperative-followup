ENT POSTOPERATIVE FOLLOW-UP — VERSION 8

WHAT THIS VERSION INCLUDES
- Installable Android-friendly Progressive Web App (PWA).
- No app login screen and no app password.
- Patient records are stored locally in the browser/app on this device.
- Manual encrypted Download Backup and Restore Backup options remain available.
- Backup files use a separate password chosen at backup time; this is NOT an app login.
- No Google Drive, no OAuth, no cloud synchronization, and no automatic upload.
- Patient history, search, operation filter, newest/oldest sorting, editing and deletion.
- Today's follow-up dashboard, CSV export, clinical images, notes, complications and WhatsApp message preparation.
- Follow-up days: Adenotonsillectomy/Adenoidectomy/Tonsillectomy = days 3, 7, 14; Septoplasty + Turbinate Reduction = days 7, 14, 21, 28.
- Operation date is day 0. Follow-ups calculated for Friday are moved to Saturday; the postoperative day number remains unchanged.

IMPORTANT DATA / PRIVACY NOTES
- Patient data stays on the device/browser profile and is not sent to Google Drive or an app server.
- If you clear browser data, uninstall/clear the app's storage, or lose the phone, local records may be lost. Download encrypted backups regularly and keep the backup password separately.
- Restoring a backup replaces the current patient database on that device.
- Anyone who can unlock and use this phone/browser profile may be able to open the app. Keep the device protected.
- This is a lightweight follow-up tool, not a certified electronic medical record system. Use it only in accordance with your facility's patient-data and privacy policies.

HOW TO HOST AND INSTALL ON ANDROID
1. Upload the CONTENTS of this folder to an HTTPS static web host. The app must be served over HTTPS for secure storage/encryption and service-worker installation (localhost is only for development).
2. Open the resulting HTTPS address in Google Chrome on the Android phone.
3. Open Chrome's three-dot menu and choose “Install app” or “Add to Home screen” (wording depends on Chrome version).
4. Confirm installation. The ENT Follow-up icon will appear on the phone and open in standalone app mode.
5. Use the same HTTPS address on the device where you first entered records. Local data is tied to that browser/app installation and is not automatically shared with other devices.

MANUAL BACKUP / RESTORE
- Tap “Download encrypted backup”. Choose a backup password of at least 10 characters and confirm it.
- Save the downloaded JSON file somewhere secure. Keep the password separately.
- To restore, tap “Restore backup”, select the JSON file, and enter its backup password.
- A Version 8 backup can be restored on another device because its encryption password is chosen for the backup itself.

FILES
- index.html: application
- manifest.webmanifest: install metadata
- sw.js: offline app shell caching
- icon-192.png / icon-512.png: app icons
