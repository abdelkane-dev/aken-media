# Contexte de reprise — réseaux sociaux Aken (mis à jour le 1er novembre 2026, session 2)

À lire en début de session par Claude avant tout travail réseaux sociaux.

## Règles de l'utilisateur (à appliquer sans redemander)
- Répondre en français, simplement.
- **Marque Aken** : logo et mascotte du site (dépôt `abdelkane-dev/Aken`, dossier `assets`), fond `#0A0A0A`, dégradé orange `#FF3D00 → #FF6B00 → #FFAA00`, titres Montserrat, texte Inter. Style moderne et accrocheur. **Pas de thème malien ou ethnique** (design « bogolan » refusé).
- **Vidéos** : toujours musique accrocheuse + voix off **masculine** + **mascotte qui bouge** (marche, parle, montre, pouce, coucou).
- **Photos** : voix off + musique derrière ; mascotte facultative.
- **Musique** : trouvée en ligne, libre de droits pour usage commercial (Pixabay Music, YouTube Audio Library, Mixkit, Uppbeat), source notée. Un morceau célèbre seulement via le catalogue officiel de la plateforme (Instagram `audioConfiguration` dans Metricool, TikTok `autoAddMusic`). Ne pas composer de musique de A à Z sauf en secours.
- **Voix** : l'utilisateur veut **sa propre voix clonée**. Voix Piper « gilles » jugée trop robotique (secours seulement).
- **Publication** : autorisation générale de publier donnée par l'utilisateur ; montrer le visuel avant si le style change. Prévenir l'utilisateur quand les posts sont prêts pour qu'il fasse LinkedIn en parallèle.
- Rien de fictif présenté comme réel (données de démo marquées « données fictives »).

## Comptes et outils
- **Metricool** (offre gratuite : ~20 posts/mois, pas de LinkedIn) : Facebook, Instagram, TikTok, YouTube, fiche Google. Retrouver le `blogId` avec `getBrandSettings`. Fuseau `Africa/Bamako`. Instagram exige du JPEG. YouTube Short : `youtubeData` (type short, madeForKids false). Fiche Google : `gmbData` type `publication`.
- **Médias** : publiés via les URL brutes de ce dépôt public (`raw.githubusercontent.com/abdelkane-dev/aken-media/main/...`). Google Drive est payant dans Metricool.
- **LinkedIn** : l'utilisateur publie lui-même (programmation native). Skills `linkedin-agent` + `li-human`. Plan de la semaine 1 : `linkedin/semaine-1.md`. Ton : anglais pour ForgeAgent, français pour OrientaML.
- **Nouveaux connecteurs vus en fin de session** (à tester) : vidIQ (`vidiq_voiceover_generate`, `vidiq_generate_music`, tendances), Canva (`remove-background`, `generate-image`), Google Drive (pour récupérer l'enregistrement de voix), OpusClip, Spotify.

## Ce dépôt
- `mascotte/` : 7 poses détourées (PNG transparent) — `coucou`, `pointe`, `pouce`, `marche1`, `marche2`, `bouche-fermee`, `bouche-ouverte`. Mascotte à l'effigie de l'utilisateur ; ne pas modifier son style.
- `outils/animation-mascotte.py` : construit les fonds (slide à 80 % sur fond flou), mixe la voix et génère la bande mascotte (marche, flottement, bouche synchronisée sur le volume de la voix, pop, coucou). Usage : `python3 animation-mascotte.py <dossier> | ffmpeg -f rawvideo -pix_fmt rgba -s 1080x600 -r 30 -i - ...` puis superposition à y=1320, sous-titres en haut (y=110), musique baissée sous la voix (`sidechaincompress`), `loudnorm I=-14`.
- `outils/musique-originale.py` : musique de secours générée (112 BPM). `outils/script-voix-intro.txt` : texte de la vidéo d'intro.
- `2026/10/` : carrousel intro v3 + vidéos publiées. `2026/11/aken-mascotte-demo.mp4` : démo mascotte (voix provisoire), **en attente de l'avis de l'utilisateur**.

## Outils techniques utiles (conteneur neuf)
- `pip install piper-tts rembg onnxruntime` ; voix Piper : `https://github.com/rhasspy/piper/releases/download/v0.0.2/voice-fr-gilles-low.tar.gz` (homme) ou `voice-fr-siwis-medium.tar.gz` (femme).
- Police sous-titres : `/usr/share/fonts/opentype/inter/InterDisplay-SemiBold.otf`, `drawtext` avec `expansion=none` (sinon « % » casse) ; une phrase trop longue déborde à 52 px : la couper en deux.

## À faire (par ordre)
1. **Réseau** : l'utilisateur doit autoriser dans l'environnement (Network access → Allowed domains) : `pixabay.com`, `cdn.pixabay.com`, `huggingface.co`, `cdn-lfs.huggingface.co`, `cas-bridge.xethub.hf.co`. Vérifier avec `curl -I https://pixabay.com`.
2. **Voix de l'utilisateur** : il enregistre ~1 min au dictaphone (texte fourni dans la conversation : présentation d'Aken, site, boutique Wave/Orange Money, appli, devis WhatsApp) et la dépose dans un dépôt **privé** (`aken-voix` conseillé) ou sur Google Drive. Puis clonage avec Chatterbox multilingue (licence MIT, français) ; sinon proposer ElevenLabs (payant, prix à vérifier) ou tester `vidiq_voiceover_generate`.
3. **Musique** : chercher 2-3 morceaux Pixabay adaptés à chaque vidéo, noter la source.
4. Recueillir l'avis sur la démo mascotte, puis refaire la vidéo d'intro avec sa voix + vraie musique.
5. **Publications quotidiennes** dès lundi 2 novembre dans le quota Metricool ; vérifier d'abord ce qui est déjà programmé (`getScheduledPosts`). Prévenir l'utilisateur pour LinkedIn.
6. Questions encore sans réponse : possède-t-il le domaine `aken.dev` (canonical du site, non rattaché sur Vercel) ? Les témoignages et chiffres du site (5 avis nommés, 5★/12, « +100K membres ») sont-ils réels ?
7. Fiche Google : l'utilisateur remplira les champs plus tard.
8. Côté skills Agensi : l'utilisateur doit envoyer les zips v1.3.1 (dépôt privé `abdelkane-dev/forgeagent-skills`). Le connecteur Agensi est maintenant disponible dans les sessions.

## Session du 1er novembre 2026 (suite)
- **Voix reçue** : enregistrement de l'utilisateur, 2 min 03, m4a AAC 44,1 kHz stéréo, propre, pauses régulières. **Ne jamais la mettre dans ce dépôt public** (dépôt privé `aken-voix` ou Google Drive seulement).
- **Réseau** : `huggingface.co` passe, mais les fichiers de modèles sont bloqués (`cas-server.xethub.hf.co`, `cas-bridge.xethub.hf.co`, `cdn-lfs.huggingface.co`, `cdn-lfs-us-1.hf.co`) → impossible de télécharger Whisper/Chatterbox. `pixabay.com` / `cdn.pixabay.com` répondent 403.
- **vidIQ voix off** = moteur ElevenLabs. Les voix clonées par l'utilisateur dans vidIQ apparaissent en tête de `vidiq_voiceover_list_voices` (`isCustom=true`). Aucune voix perso pour l'instant. Coût : 14 crédits / 1000 caractères. Piste la plus simple pour le clonage.
- **Retour sur la démo mascotte** : « acceptable » mais la mascotte ne marche que dans un sens, mouvements bizarres → à corriger (marche aller-retour avec retournement, transitions entre poses plus douces, gestes variés).

### Réponses de l'utilisateur (1er nov., suite)
- **Voix clonée sur ElevenLabs** (compte de l'utilisateur, pas via vidIQ). `api.elevenlabs.io` est bloqué par le réseau ; l'ajout de domaines est refusé de son côté. **Méthode retenue** : Claude écrit le texte → l'utilisateur le génère dans ElevenLabs avec sa voix → il dépose le MP3 dans un dossier Google Drive « Aken voix off » → Claude le récupère avec le connecteur Google Drive. Autre piste : connecter le connecteur ElevenLabs sur claude.ai (orienté agents vocaux, synthèse vocale non confirmée).
- **« Posts publicitaires »** = les posts normaux programmés avec Metricool (pas de pubs payantes).
- **Mascotte** : plus de contour blanc d'autocollant (script `outils/detourage-mascotte.py`). Il veut un **avatar façon 3D** qui bouge (pas forcément comme un humain). Démo gratuite façon 2,5D : `outils/avatar-mascotte.py` (respiration, balancement, bouche sur la voix, coucou de fin). Vraie 3D possible avec `vidiq_generate_video` (image vers vidéo), mais vidIQ n'a que **140 crédits** (recharge le 1er déc.) et le prix est seulement annoncé à l'envoi. Figma Weave demande d'abord de lier son compte Figma sur app.weavy.ai.
- **Musique** : Spotify sert à écouter, pas à télécharger, et ses morceaux ne sont pas libres de droits → interdit. Le Chromium du conteneur passe par le même réseau (Pixabay, Mixkit, Uppbeat bloqués). Options : `vidiq_generate_music` (libre de droits, 25 crédits), musique officielle Instagram/TikTok via Metricool, ou musique de secours générée.
- **Connecteurs utiles** : Metricool (programmer/analyser), vidIQ (voix, musique, vidéo IA, tendances), Canva (visuels, détourage), Google Drive (récupérer les voix), OpusClip (montage/sous-titres d'une vidéo), Figma/Gamma (visuels/présentations), Gmail. Apollo, Vercel, Miro, Sheets : hors réseaux sociaux.

### Avatar 3D (1er nov., suite) — démo 2,5D refusée (« pixelise, pas dynamique »)
- L'utilisateur veut un **vrai avatar 3D** cartoon (style film d'animation) qui bouge, parle avec sa voix et resserve pour toutes les vidéos. Cahier des charges complet : squelette, visage expressif, bibliothèque d'animations, studio Three.js, export vidéo sur fond transparent.
- **Connecteur ElevenLabs maintenant connecté** (outils `creative_*`). Voix clonées « Abdoul » (fr, accent africain) : `wVCurQkwZwgv2ptFiiKd`, `8ajUriO8xBZ8dUwW9ayY`, `3CKoXvrhTt2xBTcO2hcc` → demander laquelle garder. Modèles dispo : images (Nano Banana Pro, GPT Image…), vidéo (OmniHuman 1.5 = image + voix → avatar qui parle, Kling 3, Seedance, Veo), détourage vidéo, musique (`eleven_music_v2_5`), bruitages.
- Flux ElevenLabs « Aken – Avatar 3D mascotte » : `77C3kTKJRZ4P42SnPtpI` (références coucou + face déjà posées).
- Estimations (rien n'a été lancé) : rendu 3D ×2 ≈ 4 870 crédits (~0,97 $) ; voix 15 s ≈ 212 ; avatar parlant OmniHuman ≈ 13 900 (~2,78 $) ; clip Kling 3 Pro 5 s ≈ 5 090 (~1,02 $).
- **Limite honnête** : aucun outil accessible ici ne fabrique de modèle 3D riggé (GLB). Meshy/Tripo/Mixamo/Blender sont bloqués par le réseau. Piste GLB : planche de référence générée ici → l'utilisateur la passe dans Meshy ou Tripo (image vers 3D) puis Mixamo (squelette + animations) → Claude construit le studio Three.js. Visage complet (sourire, lèvres) = blendshapes à faire par un graphiste 3D ou Character Creator.
- **Rendus 3D faits** (Nano Banana Pro, 4 872 crédits) : rendu A (sourire bouche fermée, **retenu**) et rendu B (dents visibles), dans le flux ElevenLabs. Format sorti en 16:9 (1376×768) malgré la demande 9:16 → régler `aspect_ratio` sur le nœud la prochaine fois. Attente : choix A ou B, et l'utilisateur supprime 2 des 3 voix « Abdoul » dans ElevenLabs avant la voix d'essai.

### Stockage (règle du 1er nov.) — **plus aucun média sur GitHub**
- L'utilisateur ne veut plus de fichiers stockés sur son GitHub. Ce dépôt ne garde que ce `CONTEXTE.md` et les scripts. Médias → **Google Drive**, dossier « Aken – Réseaux sociaux » (`1MWCOU4YZjAct4Nhs1nB2klHA0ZgrTVby`) : sous-dossiers « Mascotte 3D » (`1hjRWJ3IZCUehG0R31sVCpilXHjs7Bfnp`), « Voix off » (`1ec2odRdMFfks8OjOe9O6GR4DJoq_TfIR`), « Vidéos » (`1z-Imy6oRrQpP2lWSG-nfLzmypdHIn6Qu`).
- Limite : le connecteur Drive n'envoie un fichier qu'en base64 dans l'appel → OK pour petits fichiers, pas pour des vidéos de plusieurs Mo. Les originaux restent dans le flux ElevenLabs (liens signés valables 2 h, utilisables pour Metricool au moment de programmer).
- Voix retenue : **`wVCurQkwZwgv2ptFiiKd`** (identique à l'extrait envoyé par l'utilisateur). Voix d'essai 12,3 s faite (212 crédits). Avatar parlant OmniHuman lancé (11 945 crédits), à partir du rendu A recadré en vertical.
- **Avatar parlant v1 fait** (OmniHuman 1.5, 11 945 crédits) : 12,5 s, 1088×1920, 25 i/s, avec ta voix. Lèvres synchronisées, gestes (mains ouvertes, pouces, doigt levé), clignements. Petites taches claires possibles en haut de l'image → recadrer légèrement au montage. Génération `YhZtFQipmBwRrw4hAHbR` dans le flux ElevenLabs. Total dépensé ce jour ≈ 17 030 crédits ElevenLabs.
- Recette réutilisable pour chaque vidéo : texte → `creative_generate_speech` (voix `wVCurQkwZwgv2ptFiiKd`, eleven_v4) → OmniHuman avec le nœud image `StUWt8aXk9TdVw6XJrRX` (rendu A vertical) → montage (fond Aken, sous-titres, musique) → publication.

## Programmation Metricool faite le 1er nov. 2026 (heure de Bamako)
Règle de l'utilisateur : **une vidéo tous les 3-4 jours**, et entre deux vidéos des **posts photo** (images fixes + voix off + musique). Chaque post différent, jamais répétitif.
Réseaux de chaque post : Facebook Reel + Instagram Reel + TikTok + YouTube Short (déclarés « contenu IA »).

| Date | Heure | Type | Sujet |
|---|---|---|---|
| dim. 1 nov. | 18:00 | Vidéo avatar | « Salut, moi c'est Abdoul » (présentation) |
| lun. 2 | 10:00 | Photo | Astuce : crée ta fiche Google |
| mar. 3 | 18:00 | Photo | Un site vitrine, c'est quoi ? (75 000 FCFA) |
| mer. 4 | 10:00 | Vidéo avatar | Tu vends encore tout sur WhatsApp ? |
| jeu. 5 | 10:00 | Photo | 3 réflexes sécurité (audit Aken) |
| ven. 6 | 12:00 | Photo | Une appli mobile, c'est pour qui ? |
| sam. 7 | 10:00 | Photo | 3 réglages WhatsApp Business |
| dim. 8 | 18:00 | Vidéo animée | 3 signes que ton business perd des clients |
| mer. 11 | 10:00 | Vidéo animée | Combien coûte un site au Mali ? |
| dim. 15 | 18:00 | Vidéo animée | Payer avec Wave / Orange Money |
| mer. 18 | 10:00 | Vidéo animée | Avant/après : cahier → logiciel (données fictives) |
| dim. 22 | 18:00 | Vidéo animée | 3 idées reçues |
| mer. 25 | 10:00 | Vidéo animée | C'est quoi ton business ? (-10 %) |

**À faire ensuite** : posts photo des 9-10, 12-14, 16-17, 19-21, 23-24, 26-30 nov. (nouveaux sujets, voix + musique). Quota Metricool gratuit (~20 posts/mois) : 13 posts déjà en novembre → vérifier la limite avant d'en ajouter.

### Outils de production (dans `outils/studio/`, médias ignorés par git)
- `engine.css/js` + `render.js` : moteur d'animation image par image (Playwright → ffmpeg). `build.py` : voix + sous-titres karaoké calés sur la voix (`align.py`) + musique baissée sous la voix + carton de fin WhatsApp. `specs.py` (vidéos), `photos.py` (posts photo, mode `photo=True` = images fixes avec léger zoom, sans sous-titres).
- Polices Montserrat (npm `@fontsource/montserrat`) et `logo.png` (dépôt `abdelkane-dev/aken`, `assets/logo.png`) à recopier dans `outils/studio/` sur un conteneur neuf.
- **Hébergement pour Metricool** : branche temporaire `tmp-medias` du dépôt → Metricool copie le fichier sur son serveur → branche vidée juste après (accord de l'utilisateur le 1er nov.). Le proxy ne peut pas supprimer la branche : l'utilisateur peut la supprimer sur GitHub.
- **Musiques** : 3 morceaux générés par vidIQ (IA, libres de droits) : `amapiano`, `afrohouse`, `lofi` (60 s). vidIQ : 65 crédits restants (recharge le 1er déc.).
- **ElevenLabs** : forfait 40 000 crédits/mois, **il en reste environ 6 600** → plus d'avatar parlant possible ce mois-ci (≈ 12 000 crédits chacun). Une voix off ≈ 250-400 crédits. L'avatar du 8 nov. a été remplacé par une vidéo animée.
- Analyse concurrents (vidIQ, Afrique de l'Ouest francophone) : ce qui marche = face caméra + accroche forte en 3 s, prix affichés, astuces pratiques (ex. « Wave sans connexion » 609 k vues), sous-titres dynamiques, voix + musique.

### Liberté de diffusion (règle donnée le 1er nov.)
- Claude choisit librement la fréquence et la répartition : une seule vidéo partout, une vidéo + des images, ou vidéos seulement sur TikTok/YouTube et photos ailleurs. Varier.
- Un même contenu peut être publié le même jour sur plusieurs réseaux (même vidéo ou même photo voix + musique).
- **TikTok et YouTube : priorité aux vidéos**, même si ce sont les mêmes que sur les autres réseaux.
- Éviter de republier exactement la même vidéo **sur le même réseau** (TikTok/Instagram baissent la portée des doublons).

### Reste à faire côté utilisateur
- Supprimer la branche vide `tmp-medias` sur GitHub ; supprimer les 2 voix « Abdoul » en trop dans ElevenLabs.
- Répondre aux commentaires (ou les transmettre à Claude pour préparer les réponses) ; LinkedIn en parallèle.
- Réponses (1er nov.) : l'utilisateur **ne possède pas** `aken.dev` ; les avis, notes et chiffres du site sont **faux** → il va les remplacer. **Ne jamais citer ces avis/chiffres dans les posts.** La fiche Google est remplie : publier dessus aussi.
- Prochaine session Claude : bilan des statistiques de la 1re semaine (Metricool), puis posts photo du 9 au 30 nov. dans le quota restant.

### Mise à jour du 1er nov. (suite)
- **Fiche Google ajoutée** à tous les posts programmés (`gmbData.type = photo` : la vidéo du jour va dans la galerie), + 2 actualités texte (`publication`) le mar. 3 à 12 h et le ven. 6 à 10 h. Utiliser tous les réseaux connectés à Metricool (Facebook, Instagram, TikTok, YouTube, Google).
- Rappel de la règle : **une seule vidéo tous les 3-4 jours**, publiée le même jour sur tous les réseaux ; les autres jours, une publication photo (voix + musique) sur tous les réseaux ; on peut ajouter des photos un jour de vidéo.
- **Commentaires** : l'utilisateur autorise Claude à y répondre. YouTube via vidIQ (`vidiq_video_comments` / `vidiq_reply_to_comment`) ; Instagram, Facebook et TikTok ne sont pas accessibles par les outils. Autorisation YouTube donnée par l'utilisateur le 1er nov. : les réponses passent maintenant directement.
- **Commentaire traité (réponse publiée le 1er nov.)** : « Intéressant mais pas de son 😢❤ » (@AïssaTouré-n7y) sur le Short du 31 oct. (`fZv2SSuq2aI`, commentId `UgyrZc64amJphpZ9x_14AaABAg`). Vérifié : cette vidéo est **réellement muette** (fichier `aken-intro-short.mp4`, -91 dB). Réponse prévue : « Merci beaucoup ❤️ Tu as raison, cette version est partie sans le son, désolé 🙏 Une nouvelle vidéo, avec la voix cette fois, arrive ce soir à 18 h sur la chaîne. Et si tu as une question sur ton projet : WhatsApp +223 93 78 99 16 » (à adapter si publiée après le 1er nov. au soir). Toutes les vidéos de novembre ont bien du son (≈ -17 dB).

### Routine quotidienne automatique (demandée le 1er nov.)
L'utilisateur veut une gestion **automatique chaque jour, sans attendre son accord** : vérifier les publications, répondre aux commentaires, analyser les statistiques et les concurrents, compléter le calendrier.
- Une Routine se déclenche chaque jour à **19 h 47 (Bamako)** dans cette même session.
- Musiques vidIQ (liens permanents, à retélécharger sur un conteneur neuf) :
  - amapiano : https://ai-music-tracks.s3.us-east-1.amazonaws.com/019dfbf5-5e17-454f-9317-d8e5a2c09061/f5705de8-eb61-439d-ab2b-8ae5aa4bb8c3.wav
  - afrohouse : https://ai-music-tracks.s3.us-east-1.amazonaws.com/019dfbf5-5e17-454f-9317-d8e5a2c09061/76272922-6e17-4ea9-9e83-798fc26517dd.wav
  - lofi : https://ai-music-tracks.s3.us-east-1.amazonaws.com/019dfbf5-5e17-454f-9317-d8e5a2c09061/5fd99dad-fba3-4b18-9237-7f1025c1c9fd.wav
- Garde-fous : jamais de suppression de posts publiés, jamais de pub payante, jamais de message privé ; aucun avis ni chiffre inventé ; ElevenLabs : garder au moins 2 000 crédits de réserve ; vidIQ : 10 crédits par jour au maximum (65 restants jusqu'au 1er déc.) ; vérifier le quota Metricool avant d'ajouter un post. Commentaire sensible (plainte, insulte, question juridique ou de prix non connu) → réponse polie qui renvoie vers le WhatsApp, et le signaler dans le journal.
- Limites des outils : réponses aux commentaires **YouTube seulement** (vidIQ) ; pas de « j'aime », pas d'accès aux commentaires Instagram, Facebook ou TikTok ; concurrents via vidIQ (recherche de vidéos qui cartonnent) et Metricool (concurrents à ajouter dans Metricool par l'utilisateur).

### Fiche Google (guide donné le 1er nov.)
- Site officiel stable à utiliser partout : **https://aken-two.vercel.app** (domaine de production Vercel). L'adresse en `aken-ihf1sayge-…vercel.app` enregistrée dans Metricool est une adresse de prévisualisation → à remplacer.
- Catégorie principale conseillée « Concepteur de sites Web », zone desservie Bamako, adresse masquée, téléphone/WhatsApp +223 93 78 99 16. Logo carré + couverture 1600×900 (rendu 3D A) envoyés à l'utilisateur.

### Stratégie v2 (8 nov. 2026) — adaptée de la vidéo « Agent Reach » et des chiffres réels
Méthode retenue (celle de la vidéo) : comparer **son compte vs les concurrents** (vues, sujets, accroches) puis décider quoi publier.
- **Chiffres réels du 1er au 7 nov.** (Metricool). Les 7 posts sont partis sur Facebook, Instagram, TikTok, YouTube et Google.
  - Facebook Reels (vues) : « Un site vitrine, c'est quoi ? » **268**, intro avatar 91, astuce fiche Google 62, appli mobile 45, sécurité 19, vendre sur WhatsApp 13, WhatsApp Business 6. **Temps moyen regardé : 1 à 3 s** (sauf 12 s pour « Tu vends encore tout sur WhatsApp ? ») → l'accroche n'arrête pas le pouce.
  - Instagram Reels (vues) : 34 / 15 / 13 / 4 / 4 / 3 / 2 / 2 ; temps moyen 4 à 13 s ; 0 à 3 « j'aime », 3 commentaires en tout.
  - TikTok, YouTube : **aucune donnée via Metricool** (compte TikTok perso, YouTube vide) → demander à l'utilisateur une capture de ses stats TikTok, ou 1 appel vidIQ (5 crédits).
  - Google : 0 vue (fiche pas encore validée). YouTube : aucun nouveau commentaire.
  - Échantillon minuscule (7 posts, < 300 vues) : tendances, pas certitudes.
- **Ce que font les concurrents qui cartonnent** (vidIQ, 1er nov.) : une vraie personne face caméra, une question dès les 3 premières secondes, prix et réponses concrètes (« combien coûte l'envoi », 44× la médiane), astuces pratiques locales (« Wave sans connexion », 609 k vues), portraits d'entrepreneurs.
- **Règles v2 pour tout nouveau post** :
  1. Accroche dans la **première seconde** : question déjà à l'écran à l'image 1 (pas de fondu), voix dès 0 s, vidéo de 10 à 15 s.
  2. Ratio **3 astuces utiles pour 1 offre**. Sujets concrets (prix, photos produit, erreurs courantes), jamais d'avis ni de chiffre inventé.
  3. **Un seul mot-clé d'appel** : « Écris SITE sur WhatsApp » + lien `https://wa.me/22393789916?text=SITE` dans la légende (cliquable sur Facebook, YouTube, Google) → on compte les messages « SITE » pour mesurer.
  4. Questions simples à répondre en commentaire (oui/non, 1-2-3, « écris ta phrase »), pas « tag un ami ».
  5. Montrer du **vrai travail** : captures ou enregistrements d'écran de vrais projets d'Aken. À demander à l'utilisateur 2-3 projets réels qu'il accepte de montrer.
  6. Moins de posts, meilleurs : quota gratuit Metricool limité ; TikTok et YouTube en priorité (vidéos), Facebook ensuite, Instagram après avoir gagné des abonnés.
- **Rappel** : le numéro WhatsApp officiel est +223 93 78 99 16. De vieux commentaires YouTube (2025) donnaient `wa.me/22366378213` : à faire confirmer par l'utilisateur.

### Limites découvertes le 8 nov. (à lire avant de promettre de l'automatique)
- **La routine « 19 h 47 » ne s'exécute pas toute seule.** Elle envoie un rappel dans cette session ; les rappels du 1er au 7 nov. ne sont arrivés que le 7 nov. au soir, d'un coup. Rien n'a été fait automatiquement entre-temps (les posts, eux, sont partis car programmés dans Metricool).
- Une routine créée par l'outil de cette session démarre **sans le dépôt et sans les connecteurs** (Metricool, vidIQ, ElevenLabs, Drive, Vercel) : test réel fait le 8 nov. (session `cse_01Cd7Z1YJaugFkezNVv3JarW`, seuls ffmpeg et git étaient disponibles). Inutilisable telle quelle. Pour une vraie automatisation, l'utilisateur doit créer la routine dans l'interface Routines de claude.ai en y attachant les connecteurs.
- **ElevenLabs héberge maintenant les voix sur `elevenlabsusercontent.com`.** L'utilisateur a d'abord refusé par erreur, puis **autorisé ce site le 8 nov.** (ajouté à l'environnement Default) : les voix se téléchargent à nouveau.
- **Calendrier** (8 nov.) : posts v2 programmés le **9 nov. 10 h** (3 erreurs d'une page Facebook), **10 nov. 18 h** (écris ton offre en une phrase), **12 nov. 10 h** (photos produit au téléphone), sur Facebook, Instagram, TikTok, YouTube, Google. Vidéos déjà prévues : 8 (18 h), 11, 15, 18, 22, 25. **Reste vide : 13, 14 nov.** puis 16-17, 19-21, 23-24, 26-30 (quota gratuit Metricool à surveiller). Mesure : compter les messages WhatsApp qui commencent par « SITE ».
- **Agent Reach** (`Panniantong/Agent-Reach`, MIT, ~110 k étoiles) : outil local en lecture seule (recherche/lecture de X, Reddit, YouTube, GitHub, LinkedIn emplois…), ne publie rien. LinkedIn = uniquement offres d'emploi (chercher/lire). Instagram, Facebook, X = « expérimental », via les cookies du compte principal de l'utilisateur et un navigateur furtif (CloakBrowser) → risque de blocage du compte ; le README conseille un compte secondaire. Non installé ; ne le ferait que sur accord, après lecture des scripts.
- **LinkedIn gratuit et officiel** : programmation native LinkedIn (illimitée) ou Typefully (offre gratuite ~10 posts/mois selon sa page de prix ; vérifier à l'inscription). Metricool gratuit n'inclut pas LinkedIn.

### Mises à jour du 8 nov. (soir) : réponses de l'utilisateur et site akendev.com
- **Numéro officiel confirmé : +223 93 78 99 16.** L'autre (66 37 82 13) est pour une autre activité : ne jamais l'utiliser.
- **Nouveau site : https://akendev.com** (remplace aken-two.vercel.app et l'ancienne adresse de prévisualisation). Cartes de visite mises à jour (`akendev.com`). À changer par l'utilisateur : champ « Site Web » de la fiche Google et du compte Metricool.
- **Voix ElevenLabs** : les 3 voix « Abdoul » étaient les mêmes (créées 3 fois). On garde `wVCurQkwZwgv2ptFiiKd`.
- **Projets : l'utilisateur autorise à parler de tous ses projets publics ; pour les privés, seulement le nom.**
  - Publics (GitHub abdelkane-dev) : `forgeagent` (agents IA Claude, Apache 2.0), `Hotel-management-django` (gestion hôtelière Django : réservations, clients, chambres, personnel, facturation, rôles), `Mes_delice` (gestion de pâtisserie Django : clients commandent et suivent, admin gère produits, stock avec alertes, commandes), `Transport` (**projet académique** de réservation de billets de bus, Django 5 + DRF), `taskflow` (pas de README), `Initiation_git_devops` (projet de cours), `aken-media` (ce dépôt).
  - **Règle de confidentialité (consigne de l'utilisateur) : ne parler publiquement que des dépôts publics, d'OrientaML (en ligne) et des services d'akendev.com. Ne jamais nommer ni détailler d'autres projets privés ; aucun post sur eux. En cas de doute, rester générique.**
  - Ne présenter que des faits tirés des README ; **Transport est académique**, ne pas le présenter comme un projet client.
- **Contenu de akendev.com utilisable** (prix : site vitrine 75 000 FCFA, boutique en ligne 140 000, application mobile 220 000, -10 % 1er projet, acompte 30 %, 30 jours de suivi, hébergement 1 an offert pour le site vitrine ; délais : vitrine 1 à 2 semaines, projet complet 4 à 8 semaines ; paiements Wave, Orange Money, Moov Money, cartes).
- **À NE PAS citer tant que l'utilisateur ne les a pas confirmés** (encore affichés sur akendev.com) : « Avis vérifiés 5.0 » et les 3 témoignages, « +100K membres », « 12 projets réalisés », compteurs « utilisateurs / 0 % satisfaction », résultats chiffrés des études de cas (« 3 h gagnées par jour », « zéro double-réservation », « zéro incident », « des centaines d'utilisateurs »). Il avait dit que les avis et chiffres étaient faux et qu'il les remplacerait.
- **Problèmes du site à signaler à l'utilisateur** : certains liens « Voir le code » pointent vers des dépôts privés (erreur 404) ou un mauvais nom de dépôt ; une étude de cas nomme un projet que l'utilisateur veut garder confidentiel ; zone « Intégrez ici votre widget Cal.com » encore visible ; adresse e-mail `akenkdev@gmail.com`.
- **Posts programmés en plus** (format v2, 5 destinations) : 9 nov. 10 h erreurs d'une page Facebook ; 10 nov. 18 h offre en une phrase ; 12 nov. 10 h photos produit ; **13 nov. 18 h gestion hôtelière (Hotel-management-django)** ; **14 nov. 10 h gestion de pâtisserie (Mes_delice)**. Idées à suivre : Transport (projet académique, à présenter comme tel), ForgeAgent (public), Mes projets privés par leur nom seulement.
- **Reste vide** : 15 nov. (vidéo déjà prévue à 18 h), 16-17, 19-21, 23-24, 26-30 nov.

### Instructions de l'utilisateur du 8 nov. (fin d'après-midi) : projets et services
- **Tous les projets privés peuvent être utilisés** (pas seulement leur nom). Ne pas utiliser les avis/chiffres du site. **Utiliser les services et projets de akendev.com** (page d'accueil) : sites vitrines, boutiques en ligne, applications mobiles, outils de gestion et automatisation, bases de données et tableaux de bord, cybersécurité (audit, protection), formation, marketing digital, systèmes de réservation, plateformes e-learning.
- **Projets « académiques » : ne pas écrire « académique »**, les présenter comme des projets réels. **Limite que je garde** : ne jamais inventer de client, de lieu, de chiffre ni de résultat (ex. `Transport` : « j'ai conçu le backend », sans client). L'utilisateur est l'auteur de ces dépôts.
- **README privés lus le 8 nov.** :
  - `ORIANTAML` (OrientaML) : Django 5.2, ML scikit-learn (ensemble), chatbot OrianIA (Groq/Llama 3 + RAG), analyseur de CV, notifications WebSocket, PWA, abonnements 2 500 / 5 000 / 10 000 FCFA par mois, paiements Orange Money / Moov / Wave prévus ; **en ligne : https://oriantaml.onrender.com**.
  - `devlink` : une ligne (« plateforme panafricaine pour développeurs : apprendre, collaborer, partager, trouver des opportunités »).
- **Posts programmés le 8 nov. (format v2/v3, 5 destinations)** : 9 nov. 10 h erreurs d'une page Facebook ; 10 nov. 18 h offre en une phrase ; 12 nov. 10 h photos produit ; 13 nov. 18 h gestion hôtelière ; 14 nov. 10 h gestion de pâtisserie ; **16 nov. 10 h base de données centrale (remplace les fichiers Excel)** ; **17 nov. 18 h protéger son contenu numérique (générique)** ; **19 nov. 10 h OrientaML** ; **20 nov. 12 h réservation de billets de bus**. Vidéos déjà prévues : 11, 15, 18, 22, 25 nov.
- **Idées suivantes (déjà validées par l'utilisateur)** : audit de sécurité (double authentification, pare-feu, sauvegardes testées, formation de l'équipe), conception offline-first (3G), système de réservation (hôtels, cliniques, salons), plateforme e-learning, automatisation de gestion, ForgeAgent (public), DevLink.
- **Quota Metricool** : 24 publications en novembre (hors posts GMB texte) acceptées sans erreur ; surveiller.
- **Crédits ElevenLabs** (estimation) : ≈ 4 200 restants au 8 nov. soir (réserve minimale 2 000).

## Journal des routines


### 8 nov. (nuit) : purge des projets sensibles
- Post du 17 nov. 18 h remplacé par une vidéo générique « 3 astuces pour protéger un magazine numérique » (Metricool id 420882600, uuid 385825624765319587), sans nom de projet. Spec `v3-contenu` dans `outils/studio/photos.py`.
- Noms et détails des deux projets sensibles retirés du contexte et du code (historique de la branche réécrit en local ; envoi forcé en attente de l'accord de l'utilisateur).

### 8 nov. (nuit) : calendrier complété (posts génériques, aucun nom de projet sensible)
- 21 nov. 10 h sécurité (3 gestes) ; 24 nov. 18 h appli qui marche en 3G ; 27 nov. 10 h système de réservation ; 29 nov. 18 h plateforme e-learning. 5 destinations chacun. Specs `v3-securite`, `v3-offline`, `v3-reservation`, `v3-elearning` dans `outils/studio/photos.py`.
- Jours encore vides : 23 nov., 26 nov., 28 nov., 30 nov. (volontairement, pour ne pas surcharger).
- Crédits ElevenLabs (estimation) : ≈ 2 650 restants (réserve minimale 2 000) → pas de nouvelle voix payante pour l'instant.

### Routine du 9 nov. (soir)
- Metricool : posts du 8 nov. (18 h) et du 9 nov. (10 h) publiés sur les 5 destinations, sans échec. Prévus : 10, 11, 12, 13 nov., puis 14-29 nov. (le calendrier couvre déjà plus de 3 jours).
- Commentaires YouTube : aucun commentaire sans réponse du propriétaire (3 fils récents, tous déjà traités). Aucune réponse publiée.
- Stats détaillées et recherche de concurrents non lancées aujourd'hui (rien de nouveau à publier ; crédits vidIQ économisés). Aucun nouveau post créé, crédits ElevenLabs inchangés (≈ 2 650).
- Une notification de la routine du 8 nov. était arrivée en retard (la routine ne tourne que si la session est éveillée).
