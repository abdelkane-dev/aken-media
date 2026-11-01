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
if __name__ == "__main__":
    import sys, build
    for n in sys.argv[1:]: build.make(n, **SPECS[n])
