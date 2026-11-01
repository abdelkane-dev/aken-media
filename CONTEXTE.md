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
- En attente des réponses de l'utilisateur (méthode de clonage, pubs payantes ou posts normaux, détails sur la mascotte).
