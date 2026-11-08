"""Posts photo : diapositives fixes (léger zoom) + voix off + musique."""
from specs import SPECS, V, M
P = lambda n, t: f'<div style="position:absolute;left:80px;top:220px"><span class="pill gbg" style="color:#0A0A0A;font-size:42px;font-family:Montserrat;font-weight:900">{t}</span></div>'
def title(big, small, kicker="ASTUCE"):
    return P(0, kicker) + f'<div class="center h" style="top:560px;font-size:112px">{big}</div><div class="center" style="top:1080px;font-size:48px;color:rgba(255,255,255,.8)">{small}</div>'
def point(n, head, body, icon):
    return f'''<div class="center h grad" style="top:330px;font-size:200px">{n}</div>
      <div class="center" style="top:620px;font-size:150px">{icon}</div>
      <div class="center h" style="top:860px;font-size:82px">{head}</div>
      <div class="center" style="top:1110px;font-size:46px;color:rgba(255,255,255,.8);line-height:1.3">{body}</div>'''

SPECS.update({
 "p-google": dict(voice=V+"p-google.mp3", music=M+"lofi.wav", photo=True,
   text="Astuce gratuite pour ton business : crée ta fiche Google. Quand quelqu'un cherche ton activité à Bamako, il voit ton adresse, tes horaires, ton numéro et tes avis. Ça prend dix minutes, et c'est gratuit. Et pour aller plus loin, un vrai site internet ? C'est Aken.",
   scenes=[("", title('CRÉE TA<br><span class="grad">FICHE GOOGLE</span>', "C'est gratuit, et ça change tout.", "ASTUCE GRATUITE")),
           ("quelqu'un", '<div class="card" style="position:absolute;left:100px;right:100px;top:330px;padding:60px"><div class="h" style="font-size:64px">Ton Business</div><div style="font-size:40px;color:#FFAA00;margin:16px 0">★★★★★ · Bamako</div>'
              + "".join(f'<div style="font-size:44px;margin-top:34px">{i}</div>' for i in ["📍 Ton adresse", "🕘 Tes horaires", "📞 Ton numéro", "💬 Les avis de tes clients"]) + '</div><div class="tag" style="left:0;right:0;text-align:center;top:1210px;font-size:30px">Exemple de fiche · illustration</div>'),
           ("dix minutes", '<div class="center h grad" style="top:520px;font-size:220px">10 min</div><div class="center h" style="top:820px;font-size:90px">C\'EST GRATUIT</div>'),
           ("plus loin", '<div class="center h" style="top:560px;font-size:100px">ET POUR ALLER<br><span class="grad">PLUS LOIN ?</span></div><div class="center" style="top:960px;font-size:52px">Un vrai site internet, avec Aken.</div>')]),
 "p-vitrine": dict(voice=V+"p-vitrine.mp3", music=M+"amapiano.wav", photo=True,
   text="Un site vitrine, c'est quoi exactement ? Une page d'accueil qui présente ton activité. Tes services et tes prix. Tes photos et les avis de tes clients. Et un bouton pour t'écrire directement sur WhatsApp. Tout ça, à partir de soixante-quinze mille francs CFA chez Aken.",
   scenes=[("", title('UN SITE VITRINE,<br><span class="grad">C\'EST QUOI ?</span>', "Ce qu'il y a dedans, simplement.", "SITE VITRINE")),
           ("accueil", point("1", "Accueil", "Ton activité présentée<br>en un coup d'œil", "🏠")),
           ("services", point("2", "Services & prix", "Tes photos et<br>les avis de tes clients", "🧾")),
           ("bouton", point("3", "Bouton WhatsApp", "Le client t'écrit<br>en un clic", "💬")),
           ("Tout ça", '<div class="center" style="top:420px;font-size:50px;color:rgba(255,255,255,.8)">À partir de</div><div class="center h grad" style="top:520px;font-size:190px">75 000</div><div class="center h" style="top:740px;font-size:80px">FCFA</div>')]),
 "p-securite": dict(voice=V+"p-securite.mp3", music=M+"afrohouse.wav", photo=True, music_db=-20,
   text="Trois réflexes pour protéger ton business en ligne. Un : un mot de passe différent pour chaque compte. Deux : active la validation en deux étapes sur WhatsApp et Facebook. Trois : sauvegarde tes fichiers importants chaque semaine. Et pour un vrai contrôle, Aken fait l'audit de sécurité de ton entreprise.",
   scenes=[("", title('3 RÉFLEXES<br><span class="grad">SÉCURITÉ</span>', "pour protéger ton business en ligne", "SÉCURITÉ")),
           ("mot de passe", point("1", "1 compte = 1 mot de passe", "Jamais le même<br>mot de passe partout", "🔑")),
           ("validation", point("2", "Validation en 2 étapes", "Active-la sur WhatsApp<br>et sur Facebook", "🛡️")),
           ("sauvegarde", point("3", "Sauvegarde chaque semaine", "Tes fichiers importants<br>en lieu sûr", "💾")),
           ("vrai contrôle", '<div class="center h" style="top:560px;font-size:96px">AUDIT DE<br><span class="grad">SÉCURITÉ</span></div><div class="center" style="top:930px;font-size:52px">Aken vérifie ton entreprise.</div>')]),
 "p-appli": dict(voice=V+"p-appli.mp3", music=M+"amapiano.wav", photo=True,
   text="Une application mobile, c'est pour qui ? Pour le restaurant qui veut prendre les commandes. Pour l'école qui veut informer les parents. Pour le transporteur qui veut suivre ses livraisons. Si tes clients reviennent souvent, une appli les garde près de toi. Android et iPhone, avec Aken.",
   scenes=[("", title('UNE APPLI,<br><span class="grad">C\'EST POUR QUI ?</span>', "3 exemples concrets", "APPLICATION MOBILE")),
           ("restaurant", point("", "Le restaurant", "qui prend les commandes<br>directement dans l'appli", "🍽️")),
           ("école", point("", "L'école", "qui informe les parents<br>en temps réel", "🎓")),
           ("transporteur", point("", "Le transporteur", "qui suit ses livraisons", "🚚")),
           ("reviennent", '<div class="center h" style="top:560px;font-size:96px">TES CLIENTS<br><span class="grad">RESTENT PROCHES</span></div><div class="center" style="top:930px;font-size:52px">Android et iPhone, avec Aken.</div>')]),
 "p-whatsapp": dict(voice=V+"p-whatsapp.mp3", music=M+"lofi.wav", photo=True,
   text="Tu vends sur WhatsApp ? Alors utilise au moins WhatsApp Business. Ajoute ton catalogue, avec photos et prix. Programme un message d'absence pour la nuit. Et crée des réponses rapides pour les questions qui reviennent. Quand ça ne suffit plus… c'est le moment de passer à la boutique en ligne.",
   scenes=[("", title('VENDS MIEUX<br>SUR <span class="grad">WHATSAPP</span>', "3 réglages de WhatsApp Business", "ASTUCE")),
           ("catalogue", point("1", "Le catalogue", "Tes articles avec<br>photos et prix", "🛍️")),
           ("absence", point("2", "Message d'absence", "Programmé pour la nuit", "🌙")),
           ("réponses", point("3", "Réponses rapides", "Pour les questions<br>qui reviennent", "⚡")),
           ("suffit", '<div class="center h" style="top:560px;font-size:96px">QUAND ÇA<br><span class="grad">NE SUFFIT PLUS</span></div><div class="center" style="top:930px;font-size:52px">Passe à la boutique en ligne.</div>')]),
})

# ---------- Format v2 : accroche visible dès l'image 1, voix dès 0 s, 10-15 s ----------
def hook(big, sub=""):
    return (f'<div class="center h" style="top:470px;font-size:118px">{big}</div>'
            + (f'<div class="center" style="top:1010px;font-size:52px;color:rgba(255,255,255,.85)">{sub}</div>' if sub else ""))
def step(n, head, body, icon):
    return (f'<div class="center h grad" style="top:260px;font-size:210px">{n}</div>'
            f'<div class="center" style="top:560px;font-size:150px">{icon}</div>'
            f'<div class="center h" style="top:790px;font-size:78px">{head}</div>'
            f'<div class="center" style="top:1060px;font-size:46px;color:rgba(255,255,255,.85);line-height:1.3">{body}</div>')
def cta(big, small):
    return (f'<div class="center h" style="top:520px;font-size:104px">{big}</div>'
            f'<div class="center" style="top:900px"><span class="pill gbg" style="font-size:40px;padding:20px 36px;white-space:nowrap;color:#0A0A0A;font-family:Montserrat;font-weight:900">{small}</span></div>')

SPECS.update({
 "v2-erreurs": dict(voice=V+"v2-erreurs.mp3", music=M+"afrohouse.wav", photo=True, music_db=-18,
   text="Ta page Facebook ne vend pas ? Voici trois erreurs. Un : aucun prix affiché. Deux : pas de bouton WhatsApp. Trois : des photos sombres et floues. Corrige ça aujourd'hui. Et écris SITE sur WhatsApp, si tu veux qu'on t'aide.",
   scenes=[("", hook('TA PAGE<br><span class="grad">NE VEND PAS&nbsp;?</span>', "3 erreurs à corriger")),
           ("aucun prix", step("1", "AUCUN PRIX AFFICHÉ", "Affiche au moins<br>un prix de départ", "🏷️")),
           ("bouton", step("2", "PAS DE BOUTON WHATSAPP", "Un clic doit suffire<br>pour t'écrire", "💬")),
           ("photos sombres", step("3", "PHOTOS SOMBRES OU FLOUES", "Lumière du jour<br>et objectif propre", "📷")),
           ("Corrige", hook('CORRIGE ÇA<br><span class="grad">AUJOURD\'HUI</span>')),
           ("écris SITE", cta('ÉCRIS<br><span class="grad">« SITE »</span>', "sur WhatsApp · +223 93 78 99 16"))]),
 "v2-offre": dict(voice=V+"v2-offre.mp3", music=M+"amapiano.wav", photo=True, music_db=-18,
   text="Personne ne comprend ce que tu vends ? Écris ton offre en une phrase. Le modèle : j'aide qui, à obtenir quoi, en combien de temps. Exemple : j'aide les restaurants à recevoir des commandes sur leur téléphone. Écris ta phrase en commentaire.",
   scenes=[("", hook('PERSONNE NE COMPREND<br><span class="grad">CE QUE TU VENDS ?</span>')),
           ("Écris ton offre", hook('ÉCRIS TON OFFRE<br><span class="grad">EN UNE PHRASE</span>')),
           ("modèle", '<div class="center" style="top:300px;font-size:54px;color:rgba(255,255,255,.7)">LE MODÈLE</div><div class="card center" style="top:420px;padding:70px 50px;font-size:70px;font-weight:800;line-height:1.35;font-family:Montserrat">J\'aide <span class="grad">QUI</span><br>à obtenir <span class="grad">QUOI</span><br>en <span class="grad">COMBIEN DE TEMPS</span></div>'),
           ("Exemple", '<div class="center" style="top:300px;font-size:54px;color:rgba(255,255,255,.7)">EXEMPLE</div><div class="card center" style="top:420px;padding:70px 50px;font-size:64px;font-weight:700;line-height:1.35">« J\'aide <span class="grad">les restaurants</span> à <span class="grad">recevoir des commandes</span> sur leur téléphone. »</div>'),
           ("Écris ta phrase", cta('ÉCRIS TA PHRASE<br><span class="grad">EN COMMENTAIRE</span>', "👇 on la lit tous"))]),
 "v2-photos": dict(voice=V+"v2-photos.mp3", music=M+"lofi.wav", photo=True, music_db=-17,
   text="Tes photos produit ne donnent pas envie ? Trois astuces avec ton téléphone. Un : place-toi près d'une fenêtre, jamais de flash. Deux : fond uni, une seule chose dans l'image. Trois : essuie l'objectif avant chaque photo. Simple, gratuit, et ça change tout.",
   scenes=[("", hook('TES PHOTOS PRODUIT<br><span class="grad">NE DONNENT PAS ENVIE ?</span>')),
           ("Trois astuces", hook('3 ASTUCES<br><span class="grad">AVEC TON TÉLÉPHONE</span>')),
           ("fenêtre", step("1", "PRÈS D'UNE FENÊTRE", "Lumière du jour,<br>jamais de flash", "🪟")),
           ("fond uni", step("2", "FOND UNI", "Une seule chose<br>dans l'image", "🛍️")),
           ("essuie", step("3", "ESSUIE L'OBJECTIF", "Avant chaque photo", "🧽")),
           ("Simple", hook('SIMPLE. GRATUIT.<br><span class="grad">ÇA CHANGE TOUT.</span>'))]),
})


# ---------- Posts « vrais projets » (faits tirés des README publics) ----------
def listcard(items, top=360):
    rows = "".join(f'<div class="card" style="position:absolute;left:110px;right:110px;top:{top + i*150}px;height:124px;display:flex;align-items:center;gap:34px;padding:0 44px;font-size:48px;font-weight:700" data-anim="pop" data-at="{0.15 + i*0.28:.2f}"><span style="font-size:64px">{e}</span><span>{t}</span></div>' for i, (e, t) in enumerate(items))
    return rows
def proj(title, sub):
    return (f'<div style="position:absolute;left:80px;top:220px"><span class="pill gbg" style="color:#0A0A0A;font-size:40px;font-family:Montserrat;font-weight:900">PROJET · CODE PUBLIC</span></div>'
            f'<div class="center h" style="top:520px;font-size:96px">{title}</div>'
            f'<div class="center" style="top:1000px;font-size:50px;color:rgba(255,255,255,.85)">{sub}</div>')
def repo(name):
    return ('<div class="center h" style="top:470px;font-size:100px">CODE PUBLIC<br><span class="grad">SUR GITHUB</span></div>'
            '<div class="card center" style="top:880px;padding:36px 20px"><div style="font-size:32px;color:rgba(255,255,255,.7)">github.com/abdelkane-dev/</div>'
            f'<div style="font-size:46px;font-weight:800;margin-top:10px;font-family:Montserrat">{name}</div></div>')

SPECS.update({
 "v2-hotel": dict(voice=V+"v2-hotel.mp3", music=M+"afrohouse.wav", photo=True, music_db=-18,
   text="Un hôtel qui gère tout sur papier ? Voici un système de gestion hôtelière que j'ai codé. Réservations, clients, chambres, personnel et facturation, au même endroit. Chaque employé a son propre accès. Le code est public sur GitHub. Écris SITE sur WhatsApp pour le même genre d'outil.",
   scenes=[("", hook('UN HÔTEL QUI GÈRE<br><span class="grad">TOUT SUR PAPIER ?</span>')),
           ("Voici un système", proj('SYSTÈME DE<br><span class="grad">GESTION HÔTELIÈRE</span>', "Fait avec Django")),
           ("Réservations", listcard([("🛏️", "Réservations"), ("👥", "Clients"), ("🚪", "Chambres"), ("🧑‍💼", "Personnel"), ("🧾", "Facturation")])),
           ("Chaque employé", step("", "UN ACCÈS PAR EMPLOYÉ", "Chacun voit<br>ce qui le concerne", "🔐")),
           ("Le code est", repo("Hotel-management-django")),
           ("Écris SITE", cta('ÉCRIS<br><span class="grad">« SITE »</span>', "sur WhatsApp · +223 93 78 99 16"))]),
 "v2-patisserie": dict(voice=V+"v2-patisserie.mp3", music=M+"amapiano.wav", photo=True, music_db=-18,
   text="Tu vends des gâteaux et tu notes les commandes sur un cahier ? Voici un outil de gestion de pâtisserie que j'ai codé. Le client commande et suit sa commande. Toi, tu gères les produits, le stock avec des alertes, et toutes les commandes. Code public sur GitHub. Écris SITE sur WhatsApp.",
   scenes=[("", hook('TU NOTES TES COMMANDES<br><span class="grad">SUR UN CAHIER ?</span>', "🍰")),
           ("Voici un outil", proj('OUTIL DE GESTION<br><span class="grad">DE PÂTISSERIE</span>', "Fait avec Django")),
           ("Le client commande", step("", "CÔTÉ CLIENT", "Il commande<br>et suit sa commande", "👤")),
           ("Toi,", '<div class="center h grad" style="top:230px;font-size:110px">CÔTÉ TOI</div>' + listcard([("🧁", "Tes produits"), ("📦", "Stock avec alertes"), ("📋", "Toutes les commandes")], top=480)),
           ("Code public", repo("Mes_delice")),
           ("Écris SITE", cta('ÉCRIS<br><span class="grad">« SITE »</span>', "sur WhatsApp · +223 93 78 99 16"))]),
})


# ---------- Services et projets réels (site akendev.com + README) ----------
def proj2(kicker, title, sub):
    return (f'<div style="position:absolute;left:80px;top:220px"><span class="pill gbg" style="color:#0A0A0A;font-size:38px;font-family:Montserrat;font-weight:900">{kicker}</span></div>'
            f'<div class="center h" style="top:500px;font-size:92px">{title}</div>'
            f'<div class="center" style="top:1010px;font-size:50px;color:rgba(255,255,255,.85)">{sub}</div>')
def urlcard(label, url):
    return (f'<div class="center h" style="top:470px;font-size:100px">{label}</div>'
            f'<div class="card center" style="top:880px;padding:40px 20px;font-size:48px;font-weight:800;font-family:Montserrat">{url}</div>')

SPECS.update({
 "v3-db": dict(voice=V+"v3-db.mp3", music=M+"lofi.wav", photo=True, music_db=-17,
   text="Tes stocks et tes clients sont dans des dizaines de fichiers Excel ? Voilà le problème. La solution : une base de données centrale. On migre ton historique en sécurité, puis on crée un tableau de bord des ventes et du stock. Écris SITE sur WhatsApp.",
   scenes=[("", hook('TES STOCKS ET CLIENTS<br>DANS <span class="grad">DES DIZAINES<br>D\'EXCEL ?</span>')),
           ("problème", '<div class="center h grad" style="top:230px;font-size:110px">LE PROBLÈME</div>' + listcard([("📂", "Fichiers éparpillés"), ("❓", "Chiffres contradictoires"), ("🙈", "Décisions à l'aveugle")], top=480)),
           ("La solution", hook('UNE BASE DE DONNÉES<br><span class="grad">CENTRALE</span>', "Une seule source de vérité")),
           ("On migre", step("", "MIGRATION SÉCURISÉE", "De tout ton historique", "🔒")),
           ("tableau de bord", '<div class="center h grad" style="top:230px;font-size:100px">TABLEAU DE BORD</div>' + listcard([("📈", "Les ventes"), ("📦", "Le stock")], top=500)),
           ("Écris SITE", cta('ÉCRIS<br><span class="grad">« SITE »</span>', "sur WhatsApp · +223 93 78 99 16"))]),
 "v3-contenu": dict(voice=V+"v3-contenu.mp3", music=M+"afrohouse.wav", photo=True, music_db=-18,
   text="Comment protéger un magazine numérique ? Trois astuces. Un : le filigrane, l'email de l'acheteur s'affiche sur la page. Deux : l'accès par compte, pas de fichier à partager. Trois : les abonnements qui expirent tout seuls. Écris SITE sur WhatsApp pour ton projet.",
   scenes=[("", hook('COMMENT PROTÉGER<br><span class="grad">UN MAGAZINE<br>NUMÉRIQUE ?</span>')),
           ("Trois astuces", '<div class="center h grad" style="top:230px;font-size:100px">3 ASTUCES</div>' + listcard([("💧", "Le filigrane"), ("🔑", "L'accès par compte"), ("⏳", "Abonnements qui expirent")], top=480)),
           ("le filigrane", step("1", "LE FILIGRANE", "L'email de l'acheteur<br>s'affiche sur la page", "💧")),
           ("l'accès par compte", step("2", "L'ACCÈS PAR COMPTE", "Pas de fichier<br>à partager", "🔑")),
           ("abonnements", step("3", "ABONNEMENTS", "Ils expirent<br>tout seuls", "⏳")),
           ("Écris SITE", cta('ÉCRIS<br><span class="grad">« SITE »</span>', "sur WhatsApp · +223 93 78 99 16"))]),
 "v3-securite": dict(voice=V+"v3-securite.mp3", music=M+"lofi.wav", photo=True, music_db=-18,
   text='Ton entreprise est-elle protégée ? Trois gestes simples. Un : la double authentification sur tes comptes. Deux : des sauvegardes que tu testes vraiment. Trois : une équipe formée aux arnaques. Écris SITE sur WhatsApp pour un audit de sécurité.',
   scenes=[("", hook('TON ENTREPRISE<br>EST-ELLE<br><span class="grad">PROTÉGÉE ?</span>')),
           ('Trois gestes', '<div class="center h grad" style="top:230px;font-size:100px">3 POINTS</div>' + listcard([('🔐', 'Double authentification'), ('💾', 'Sauvegardes testées'), ('🎓', 'Équipe formée')], top=480)),
           ('double authentification', step('1', 'DOUBLE AUTHENTIFICATION', 'Sur tous<br>tes comptes', '🔐')),
           ('sauvegardes', step('2', 'SAUVEGARDES TESTÉES', 'Pas juste<br>des copies', '💾')),
           ('équipe formée', step('3', 'ÉQUIPE FORMÉE', 'Aux arnaques<br>courantes', '🎓')),
           ("Écris SITE", cta('ÉCRIS<br><span class="grad">« SITE »</span>', "sur WhatsApp · +223 93 78 99 16"))]),
 "v3-offline": dict(voice=V+"v3-offline.mp3", music=M+"amapiano.wav", photo=True, music_db=-18,
   text="Une application qui rame quand la connexion est faible ? Trois principes pour qu'elle marche même en 3G. Un : charger peu de données. Deux : garder l'essentiel sur le téléphone. Trois : synchroniser quand le réseau revient. Écris SITE sur WhatsApp pour ton application.",
   scenes=[("", hook('UNE APPLI QUI RAME<br>EN <span class="grad">3G ?</span>')),
           ('Trois principes', '<div class="center h grad" style="top:230px;font-size:100px">3 POINTS</div>' + listcard([('📉', 'Peu de données'), ('📱', "L'essentiel sur le téléphone"), ('🔄', 'Synchro au retour du réseau')], top=480)),
           ('peu de données', step('1', 'PEU DE DONNÉES', 'Charger<br>le strict nécessaire', '📉')),
           ("garder l'essentiel", step('2', "L'ESSENTIEL SUR PLACE", 'Sur le téléphone', '📱')),
           ('synchroniser', step('3', 'SYNCHRONISATION', 'Quand le réseau<br>revient', '🔄')),
           ("Écris SITE", cta('ÉCRIS<br><span class="grad">« SITE »</span>', "sur WhatsApp · +223 93 78 99 16"))]),
 "v3-reservation": dict(voice=V+"v3-reservation.mp3", music=M+"afrohouse.wav", photo=True, music_db=-18,
   text="Tu prends encore tes rendez-vous sur un cahier ? Un système de réservation, c'est simple. Un : le client choisit son créneau. Deux : il reçoit une confirmation. Trois : tu vois ton planning en direct. Pour un hôtel, une clinique ou un salon. Écris SITE sur WhatsApp.",
   scenes=[("", hook('TES RENDEZ-VOUS<br>SUR <span class="grad">UN CAHIER ?</span>')),
           ("c'est simple", '<div class="center h grad" style="top:230px;font-size:100px">3 POINTS</div>' + listcard([('🗓️', 'Le client choisit son créneau'), ('✅', 'Il reçoit une confirmation'), ('📋', 'Ton planning en direct')], top=480)),
           ('créneau', step('1', 'LE CRÉNEAU', 'Le client<br>le choisit', '🗓️')),
           ('confirmation', step('2', 'CONFIRMATION', 'Il la reçoit<br>tout de suite', '✅')),
           ('planning en direct', step('3', 'PLANNING EN DIRECT', 'Tout au même endroit', '📋')),
           ("Écris SITE", cta('ÉCRIS<br><span class="grad">« SITE »</span>', "sur WhatsApp · +223 93 78 99 16"))]),
 "v3-elearning": dict(voice=V+"v3-elearning.mp3", music=M+"lofi.wav", photo=True, music_db=-18,
   text="Tu veux former tes élèves ou ton équipe en ligne ? Une plateforme e-learning, c'est trois choses. Un : des cours accessibles sur téléphone. Deux : un suivi des progrès. Trois : des exercices pour pratiquer. Écris SITE sur WhatsApp pour ta plateforme.",
   scenes=[("", hook('FORMER EN LIGNE<br>TES ÉLÈVES OU<br><span class="grad">TON ÉQUIPE ?</span>')),
           ("trois choses", '<div class="center h grad" style="top:230px;font-size:100px">3 CHOSES</div>' + listcard([("📱", "Cours sur téléphone"), ("📈", "Suivi des progrès"), ("✍️", "Exercices")], top=480)),
           ("cours accessibles", step("1", "COURS SUR TÉLÉPHONE", "Accessibles<br>partout", "📱")),
           ("suivi des progrès", step("2", "SUIVI DES PROGRÈS", "Pour chaque<br>apprenant", "📈")),
           ("exercices", step("3", "DES EXERCICES", "Pour pratiquer", "✍️")),
           ("Écris SITE", cta('ÉCRIS<br><span class="grad">« SITE »</span>', "sur WhatsApp · +223 93 78 99 16"))]),
 "v3-orientaml": dict(voice=V+"v3-orientaml.mp3", music=M+"amapiano.wav", photo=True, music_db=-18,
   text="Trouver un emploi ou une formation au Mali, c'est difficile ? Voici OrientaML, une plateforme que j'ai créée. Elle recommande des offres grâce à l'intelligence artificielle, analyse ton CV, et un assistant répond à tes questions de carrière. Elle est en ligne. Écris SITE sur WhatsApp pour ton projet.",
   scenes=[("", hook('TROUVER UN EMPLOI<br>OU UNE FORMATION<br><span class="grad">AU MALI ?</span>')),
           ("Voici OrientaML", proj2("MON PROJET · EN LIGNE", '<span class="grad">ORIENTAML</span>', "Orientation professionnelle par IA")),
           ("Elle recommande", listcard([("🎯", "Offres recommandées"), ("📄", "Analyse de ton CV"), ("💬", "Assistant carrière")])),
           ("en ligne", urlcard('<span class="grad">EN LIGNE</span>', "oriantaml.onrender.com")),
           ("Écris SITE", cta('ÉCRIS<br><span class="grad">« SITE »</span>', "sur WhatsApp · +223 93 78 99 16"))]),
 "v3-transport": dict(voice=V+"v3-transport.mp3", music=M+"afrohouse.wav", photo=True, music_db=-18,
   text="Tu gères des bus et des réservations à la main ? Voici une application de réservation de billets de bus, dont j'ai conçu le backend. La flotte, les trajets, les places disponibles en temps réel, les annulations. Avec une API pour une future application mobile. Écris SITE sur WhatsApp.",
   scenes=[("", hook('TU GÈRES TES BUS<br>ET TES RÉSERVATIONS<br><span class="grad">À LA MAIN ?</span>')),
           ("Voici une application", proj2("MON PROJET · CODE PUBLIC", 'RÉSERVATION DE<br><span class="grad">BILLETS DE BUS</span>', "Backend Django · API REST")),
           ("La flotte", listcard([("🚌", "La flotte"), ("🗺️", "Les trajets"), ("💺", "Places en temps réel"), ("↩️", "Les annulations")], top=330)),
           ("Avec une API", step("", "UNE API REST", "Prête pour une future<br>application mobile", "🔌")),
           ("Écris SITE", cta('ÉCRIS<br><span class="grad">« SITE »</span>', "sur WhatsApp · +223 93 78 99 16"))]),
})

if __name__ == "__main__":
    import sys, build
    for n in sys.argv[1:]: build.make(n, **SPECS[n])
