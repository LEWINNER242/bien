[app]

# Identité de l'application
title = TRIKA.TRAD
package.name = trikatrad
package.domain = org.trikatech
version = 1.0

# Sources et ressources nécessaires à toutes les fonctions de l'application
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,atlas,db,txt,mp4,wav,mp3,json
source.exclude_dirs = .git,.venv,venv,__pycache__,bin,.buildozer

# Kivy + Android + traduction en ligne + IA Groq
requirements = python3,kivy,pyjnius,deep-translator,groq

# Interface
orientation = portrait
fullscreen = 0

# Icône Android
icon.filename = %(source.dir)s/icon.png

# Autorisations
android.permissions = INTERNET,RECORD_AUDIO

# Compatibilité Android
android.api = 34
android.minapi = 24
android.ndk_api = 24
android.ndk = 25c
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = False

# Bootstrap Kivy
p4a.bootstrap = sdl2

# Produire un APK de test
android.debug_artifact = apk
android.release_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
