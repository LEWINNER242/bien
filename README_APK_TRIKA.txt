TRIKA.TRAD — PROJET PREPARE POUR COMPILATION ANDROID
====================================================

CONTENU
-------
- main.py : application Kivy principale
- gemini_ai.py : assistant Groq avec bascule entre modèles disponibles
- dictionnaire_trika_nouvelle.db : dictionnaire SQLite (438 entrées)
- trika_knowledge.txt : base de connaissances de TRIKA IA
- presentation.mp4 : vidéo affichée directement dans l'application
- logo.png, drapeau.png, icon.png : ressources graphiques
- buildozer.spec : configuration de compilation Android

CORRECTIONS EFFECTUEES
----------------------
1. La base SQLite est copiée au premier démarrage dans le dossier privé
   et inscriptible de l'application Android. L'historique ne tente donc
   plus d'écrire dans les fichiers internes de l'APK.
2. TRIKA IA utilise des chemins explicites pour la base SQLite et la base
   de connaissances.
3. La clé Groq précédemment présente dans le code a été retirée.
   Une nouvelle clé doit être saisie dans Paramètres > Clé API Groq.
4. Les fichiers logo.png et drapeau.png ont été convertis en vrais PNG :
   leurs anciennes extensions ne correspondaient pas à leur format réel.
5. L'icône Android a été normalisée en PNG 512 x 512.
6. Le nom de fichier du drapeau a été harmonisé avec drapeau.png.
7. Les modèles Groq ont été actualisés : gpt-oss-20b, gpt-oss-120b,
   qwen3.8-27b. Le code passe au modèle suivant si le précédent échoue.
8. La vidéo MP4 et la dépendance ffpyplayer sont conservées.
9. Buildozer est configuré pour python-for-android v2026.05.09,
   Android API 35, NDK 25b et architectures ARM 64/32 bits.

IMPORTANT — CLÉ GROQ
-------------------
La clé qui figurait dans l'ancien fichier gemini_ai.py doit être révoquée
immédiatement dans le compte Groq. Ne la réutilisez pas.
Après installation de l'APK, créez une nouvelle clé puis ouvrez :
Paramètres > Clé API Groq > Enregistrer la clé IA.

La clé est stockée dans l'espace privé de l'application sur le téléphone.
Cela évite de la publier dans le code source, mais une clé placée dans une
application cliente ne peut jamais être considérée comme totalement secrète.
Pour une distribution publique à grande échelle, il faudra idéalement
faire passer les appels IA par un serveur sécurisé.

COMPILATION
-----------
Ce dossier est le dossier racine du projet. Depuis Ubuntu/WSL, placez-vous
à l'intérieur de ce dossier (celui qui contient buildozer.spec), puis :

  python3 -m venv .venv
  source .venv/bin/activate
  pip install --upgrade pip setuptools wheel
  pip install buildozer==1.6.0 Cython==0.29.36
  buildozer -v android debug

L'APK de test doit apparaître dans le dossier bin/.
Ne lancez pas buildozer init : le buildozer.spec est déjà fourni.

ETAT DES VERIFICATIONS
----------------------
- Syntaxe Python : vérifiée (py_compile).
- Présence des ressources : vérifiée.
- Lecture de la base SQLite : vérifiée, 438 entrées dans dictionnaire.
- Formats PNG : vérifiés après conversion.
- Vidéo : conteneur MP4 et flux vidéo H.264 détectés.
- Compilation Android réelle et test sur téléphone : NON effectués ici.
  La réussite finale dépendra du téléchargement et de la compilation des
  recettes Android (notamment FFmpeg/ffpyplayer) sur l'environnement de build.
