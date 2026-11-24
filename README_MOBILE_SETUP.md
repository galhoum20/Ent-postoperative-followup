# ENT Follow-up V12 — Mobile setup (Android Chrome + GitHub)

**Status: source code only. No APK has been built by me.** The build runs on GitHub Actions; I could not run npm/Gradle in my sandbox (no network).

## Diagnosis of the two Actions errors

1. **`Could not read package.json`** — the workflow ran on `main`, but `package.json` only existed on `V12-build`. Fix: put every file in the **repo root of the branch the workflow runs on**, and do not hard-code a `ref:`. The workflow now checks out whatever branch triggered it.
2. **`Invalid workflow file … line 17`** — your pasted file had a YAML indentation error under `jobs:`. Separately, the workflow in the original ZIP had a second bug that GitHub rejects: `if: ${{ secrets.ANDROID_KEYSTORE_BASE64 != '' }}` (the `secrets` context is not allowed in a step `if`). The signed-release step was removed; the new file passes YAML parsing and has no `secrets` usage.

## Required repo layout (all at the repo root, same branch)

```
index.html  sw.js  manifest.webmanifest  icon-192.png  icon-512.png
package.json  capacitor.config.ts
scripts/patch-manifest.py
.github/workflows/build-android-apk.yml
```
No `www/` folder is needed; the workflow creates it.

## Upload steps (Android Chrome, GitHub site)

Easiest: work on `main` only and ignore `V12-build`.

1. Chrome → open `https://github.com/galhoum20/Ent-postoperative-followup`. Menu (⋮) → **Desktop site**.
2. Unzip this package on the phone (Files app → long-press ZIP → Extract).
3. Branch selector → choose **main**.
4. **Add file → Upload files**. Select: `index.html, sw.js, manifest.webmanifest, icon-192.png, icon-512.png, package.json, capacitor.config.ts`. Replace existing. Commit directly to `main`.
5. Folders: GitHub mobile upload cannot pick folders. Instead use **Add file → Create new file**:
   - Name: `scripts/patch-manifest.py` → paste the file contents → Commit.
   - Name: `.github/workflows/build-android-apk.yml` → paste the contents → Commit. (Typing `/` creates folders.)
6. Remove old duplicates: delete any `www/` folder or old workflow file in other locations.

## Build and download the APK

1. **Actions** tab → **Build Android APK (V12)** → **Run workflow** (branch `main`) → Run. (It also starts automatically on a push to `main`.)
2. Wait ~5–10 min for the green check. If red, open the failed step and send me the log text.
3. Open the finished run → scroll to **Artifacts** → download `AlFereh-ENT-Followup-V12-APK` → unzip → install `app-debug.apk` (allow "install unknown apps" for Chrome/Files).

GitHub Pages (`https://galhoum20.github.io/Ent-postoperative-followup/`) serves the same `index.html` from `main`.

## What changed in the app

- Daily 11:00 reminder rewritten. Old code scheduled one *repeating* notification with text frozen at scheduling time, so it would show stale lists. Now: 30 separate notifications, each with that day's own "today / tomorrow" text; rebuilt on app open and after every data change/sync.
- **Notifications show counts only** ("Today: 2 / Tomorrow: none due"). No patient names or file numbers ever enter a notification.
- Asks for the Android exact-alarm setting if denied.
- Removed `smallIcon: ic_stat_icon_config_sample` (resource may not exist).
- Notification IDs: 1100–1199 daily, 1999 test. Storage keys, encryption, backups untouched.

## Google Drive sign-in inside the APK (new)

Google blocks sign-in in embedded WebViews, so the APK now opens the **system browser**, signs in with OAuth + PKCE (no client secret), and receives the result through the `com.alfereh.entfollowup:/oauth2redirect` link. A refresh token lets later syncs run silently. Chrome/PWA keeps the original web sign-in.

**You must create one thing in Google Cloud (I cannot, and did not invent it):**
1. Google Cloud Console → same project as your Web client → **APIs & Services → Credentials → Create credentials → OAuth client ID → Android**.
2. Package name: `com.alfereh.entfollowup`.
3. SHA-1: after a successful Actions run, open the step **Print APK signing SHA-1** and copy the `SHA1:` value.
4. Copy the new Android client ID. In the app: Settings → **Android OAuth Client ID** → paste → save → Connect Google Drive.
5. If the consent screen is in "Testing", add your Gmail as a test user.

**Caveats:** GitHub's debug keystore is regenerated on every build, so the SHA-1 changes each run. If Google rejects sign-in after a rebuild, update the SHA-1 on the Android client (or tell me and I will add a fixed keystore via GitHub Secrets). The refresh token is stored in the app's local storage like your passphrase, so use a screen lock. Disconnecting revokes it.

## Feature checklist

| Feature | Status |
|---|---|
| Arabic RTL / English LTR, file number digits-only, Day 0, Friday→Saturday, WhatsApp, CSV | Present in code, **unchanged; not re-tested by me** |
| Storage keys `entFollowupEncryptedV5` / `SaltV5` / `AutoSyncSecretV7` + backup format | Unchanged (no migration) |
| JS syntax of app | Checked (`node --check`) |
| Workflow YAML | Parses; manifest-patch script tested on a sample manifest |
| Local notifications in APK | **Implemented, untested on a device** |
| Notification when app not opened for 30+ days, or for patients added on another device and not yet synced | **Not possible** — refresh happens only when app opens |
| Drive sync in Chrome/PWA | Code present (encrypted, `drive.file`, keep-both conflict prompt); **untested** |
| Drive sign-in inside APK | **Implemented (system-browser PKCE), untested** — needs the Android OAuth client ID from the section above. Not validated against Google's servers. |
| Notification text | Counts only (tested logic in Node: patient name never appears) |
| Sync every 5 min | Only while the app is open (`setInterval`); **no background sync** |
| APK built | **No** |

## Privacy

Use dummy data when testing. Never commit a client secret, passphrase, or keystore. Notification text contains patient names; the private channel hides it on a secure lock screen only if a screen lock is set.
