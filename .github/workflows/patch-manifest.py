#!/usr/bin/env python3
"""Idempotently patch the generated Android manifest:
 - notification / alarm permissions
 - OAuth redirect intent-filter (custom scheme) for Google Drive sign-in
"""
path = "android/app/src/main/AndroidManifest.xml"
txt = open(path, encoding="utf-8").read()

perms = [
    "android.permission.POST_NOTIFICATIONS",
    "android.permission.SCHEDULE_EXACT_ALARM",
    "android.permission.RECEIVE_BOOT_COMPLETED",
]
missing = [p for p in perms if p not in txt]
if missing:
    block = "".join('    <uses-permission android:name="%s" />\n' % p for p in missing)
    idx = txt.index("<application")
    txt = txt[:idx] + block.lstrip() + "    " + txt[idx:]

SCHEME = "com.alfereh.entfollowup"
added_filter = False
if 'android:scheme="%s"' % SCHEME not in txt:
    flt = (
        '        <intent-filter>\n'
        '            <action android:name="android.intent.action.VIEW" />\n'
        '            <category android:name="android.intent.category.DEFAULT" />\n'
        '            <category android:name="android.intent.category.BROWSABLE" />\n'
        '            <data android:scheme="%s" />\n'
        '        </intent-filter>\n' % SCHEME
    )
    end = txt.index("</activity>")          # first activity = MainActivity
    txt = txt[:end] + flt + "        " + txt[end:]
    added_filter = True

open(path, "w", encoding="utf-8").write(txt)
print("permissions added:", missing or "none")
print("oauth intent-filter added:", added_filter)
