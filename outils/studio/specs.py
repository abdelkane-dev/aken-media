"""Contenu des vidéos de la semaine (textes = voix off exactes)."""
V = "../../brouillons/semaine/voix/"
M = "../../brouillons/semaine/musique/"
AV = "../../brouillons/avatar3d/"

def sc(start, end, inner, style=""):
    return f'<div class="scene" data-start="{start}" data-end="{end}" style="{style}">{inner}</div>'

# ---------- Dimanche 1er nov. : présentation de l'avatar ----------
def dim1(T, d):
    return sc(0, 3.2, '''<div class="center" style="top:150px"><span class="pill gbg" style="color:#0A0A0A;font-family:Montserrat;font-weight:900;font-size:40px" data-anim="pop">NOUVEAU CHEZ AKEN</span></div>''') + \
           sc(T(5), d, '''<div class="center" style="top:150px"><span class="pill card" style="font-size:40px" data-anim="down">Site · Boutique · Appli</span></div>''')

# ---------- Lundi : 3 signes ----------
def lundi(T, d):
    s = sc(0, T(4), f'''
      <div class="center h" style="top:430px;font-size:118px" data-anim="up">TON BUSINESS<br><span class="grad">PERD DES<br>CLIENTS</span></div>
      <div class="center" style="top:1010px;font-size:46px;color:rgba(255,255,255,.75)" data-anim="fade" data-at=".7">chaque jour… sans le savoir</div>
      <div style="position:absolute;left:440px;top:1120px;width:200px;height:200px;border-radius:50%;border:8px solid #FF3D00;display:flex;align-items:center;justify-content:center;font-size:110px;font-family:Montserrat;font-weight:900;color:#FF3D00" data-anim="pop" data-at="1.1">↓</div>''')
    s += sc(T(4), T(9), f'''
      <div style="position:absolute;left:80px;top:230px" class="h"><span class="pill gbg" style="color:#0A0A0A;font-size:44px;font-family:Montserrat;font-weight:900" data-anim="left">SIGNE 1</span></div>
      <div class="phone" style="left:280px;top:390px" data-anim="up" data-at=".1"><div class="notch"></div><div class="scr">
        <div class="tag" style="top:60px;left:40px">Client · en ligne</div>
        <div class="bub in" data-anim="left" data-at=".5">Bonjour 👋 Vous avez un site internet ?</div>
        <div class="bub out" data-anim="right" data-at="1.4">Non… écrivez-moi sur WhatsApp 😅</div>
        <div class="bub in" data-anim="left" data-at="2.3">Ah… d'accord, je vais voir ailleurs.</div>
      </div></div>''')
    s += sc(T(9), T(14), f'''
      <div style="position:absolute;left:80px;top:230px"><span class="pill gbg" style="color:#0A0A0A;font-size:44px;font-family:Montserrat;font-weight:900" data-anim="left">SIGNE 2</span></div>
      <div class="card" style="position:absolute;left:80px;right:80px;top:420px;height:130px;border-radius:70px;display:flex;align-items:center;padding:0 50px;font-size:44px;background:#fff;color:#222" data-anim="up">
        <span style="color:#888;margin-right:24px">🔍</span><span data-anim="type" data-at=".3" data-dur="1.2">ton business Bamako</span></div>
      <div class="card" style="position:absolute;left:80px;right:80px;top:610px;padding:40px" data-anim="up" data-at="1.6">
        <div style="font-size:28px;color:#8ab4f8">concurrent.ml</div><div style="font-size:44px;font-weight:700;margin-top:8px">Ton concurrent</div>
        <div style="font-size:30px;color:rgba(255,255,255,.65);margin-top:10px">Site, horaires, avis, itinéraire…</div></div>
      <div class="card" style="position:absolute;left:80px;right:80px;top:900px;padding:40px;opacity:.5" data-anim="up" data-at="1.9">
        <div style="font-size:28px;color:#8ab4f8">autre-concurrent.ml</div><div style="font-size:44px;font-weight:700;margin-top:8px">Un autre concurrent</div></div>
      <div class="h" style="position:absolute;left:560px;top:1120px;font-size:80px;color:#FF3D00;border:8px solid #FF3D00;padding:10px 30px;border-radius:20px" data-anim="stamp" data-at="2.6">ET TOI ?</div>''')
    s += sc(T(14), T(18), f'''
      <div style="position:absolute;left:80px;top:230px"><span class="pill gbg" style="color:#0A0A0A;font-size:44px;font-family:Montserrat;font-weight:900" data-anim="left">SIGNE 3</span></div>
      ''' + "".join(f'<div class="bub in" style="position:absolute;left:{90 + (i % 2) * 330}px;top:{380 + i * 120}px;font-size:40px" data-anim="pop" data-at="{0.2 + i * 0.28:.2f}">{q}</div>'
                    for i, q in enumerate(["C'est combien ?", "C'est dispo ?", "Vous livrez ?", "C'est combien ?", "Vous êtes où ?", "C'est combien ??", "Dispo en noir ?"])) + '''
      <div class="h grad" style="position:absolute;right:90px;top:1200px;font-size:150px" data-anim="pop" data-at="2.2">×100</div>''')
    s += sc(T(18), d, f'''
      <div class="center h" style="top:520px;font-size:110px" data-anim="up">TU TE<br><span class="grad">RECONNAIS ?</span></div>
      <div class="center" style="top:900px;font-size:48px" data-anim="up" data-at=".5">Aken s'occupe du reste.</div>''')
    return s

# ---------- Mardi : prix ----------
def mardi(T, d):
    s = sc(0, T(4), '''
      <div class="center h" style="top:470px;font-size:104px" data-anim="up">COMBIEN COÛTE<br>UN SITE<br><span class="grad">AU MALI ?</span></div>
      <div class="center" style="top:1030px;font-size:46px;color:rgba(255,255,255,.75)" data-anim="fade" data-at=".6">On te dit tout, sans détour.</div>''')
    s += sc(T(4), T(11), '''
      <div class="center" style="top:360px;font-size:44px;color:rgba(255,255,255,.75)" data-anim="fade">Site vitrine · à partir de</div>
      <div class="center h grad" style="top:450px;font-size:190px" data-anim="count" data-to="75000" data-at=".2" data-dur="1.6">0</div>
      <div class="center h" style="top:660px;font-size:80px" data-anim="up" data-at=".6">FCFA</div>
      <div class="center" style="top:830px"><span class="pill card" style="font-size:42px" data-anim="pop" data-at="2.4">✓ 30 jours de suivi inclus</span></div>''')
    s += sc(T(11), T(14), '''
      <div style="position:absolute;left:190px;top:420px;width:700px;height:700px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center" class="gbg" data-anim="pop">
        <div class="h" style="font-size:230px;color:#0A0A0A">-10%</div><div class="h" style="font-size:52px;color:#0A0A0A">1er projet</div></div>''')
    s += sc(T(14), d, '''
      ''' + "".join(f'<div class="card" style="position:absolute;left:110px;right:110px;top:{340 + i*190}px;padding:40px 50px;display:flex;justify-content:space-between;font-size:46px;font-weight:700" data-anim="right" data-at="{0.15+i*0.3:.2f}"><span>{n}</span><span class="grad">sur devis</span></div>'
                    for i, n in enumerate(["Boutique en ligne", "Application mobile", "Logiciel de gestion"])) + '''
      <div class="center h" style="top:990px;font-size:76px" data-anim="up" data-at="1.4">Devis <span class="grad">gratuit</span></div>''')
    return s

# ---------- Jeudi : avant / après ----------
def jeudi(T, d):
    lines = "".join(f'<div style="position:absolute;left:40px;right:40px;top:{70+i*62}px;height:2px;background:#9fb7d9"></div>' for i in range(12))
    scrib = "".join(f'<div style="position:absolute;left:{60+(i*37)%120}px;top:{95+i*62}px;font-family:cursive;font-size:34px;color:#2b3a67;transform:rotate({(-3+i%5)}deg)">{t}</div>' for i, t in enumerate(["Ventes 12/10 : ???", "Stock riz : 14 → 9 ?", "Facture Diallo ✗", "Crédit Awa 5 000", "Total : ... à recompter", "Stock huile ??", "Facture perdue", "Reçu ?"]))
    s = sc(0, T(2), '''<div class="center h" style="top:560px;font-size:120px" data-anim="up">FINI LE<br><span class="grad">CAHIER<br>DE VENTES</span></div>''')
    s += sc(T(2), T(8), f'''
      <div style="position:absolute;left:80px;top:230px"><span class="pill" style="background:#3a3a3a;font-size:44px;font-family:Montserrat;font-weight:900" data-anim="left">AVANT</span></div>
      <div style="position:absolute;left:130px;top:380px;width:820px;height:900px;background:#f4f1e8;border-radius:16px;box-shadow:0 30px 80px rgba(0,0,0,.6);transform:rotate(-3deg);overflow:hidden" data-base="rotate(-3deg)" data-anim="up">{lines}{scrib}</div>
      <div class="h" style="position:absolute;left:300px;top:700px;font-size:120px;color:#FF3D00;border:10px solid #FF3D00;padding:10px 40px;border-radius:24px" data-anim="stamp" data-at="2.6">STOP</div>''')
    bars = "".join(f'<div style="position:absolute;bottom:0;left:{30+i*62}px;width:40px;height:{h}px;border-radius:10px 10px 0 0" class="gbg" data-anim="grow" data-at="{0.5+i*0.08:.2f}"></div>' for i, h in enumerate([90, 140, 120, 190, 170, 240, 280]))
    s += sc(T(8), d, f'''
      <div style="position:absolute;left:80px;top:230px"><span class="pill gbg" style="color:#0A0A0A;font-size:44px;font-family:Montserrat;font-weight:900" data-anim="left">APRÈS</span></div>
      <div class="phone" style="left:280px;top:340px" data-anim="up"><div class="notch"></div><div class="scr">
        <div style="font-size:26px;color:rgba(255,255,255,.6)">Aujourd'hui</div>
        <div class="h" style="font-size:64px;margin-top:6px" data-anim="count" data-to="186500" data-suffix=" F" data-at=".3" data-dur="1.4">0</div>
        <div style="font-size:26px;color:#4ade80;margin-top:6px">▲ +18 % cette semaine</div>
        <div style="position:relative;height:300px;margin-top:40px">{bars}</div>
        <div class="card" style="padding:22px;margin-top:30px;font-size:26px;border-radius:24px" data-anim="up" data-at="1.3">Stock riz : <b>42 sacs</b> · Huile : <b>18 bidons</b></div>
        <div class="card" style="padding:22px;margin-top:16px;font-size:26px;border-radius:24px" data-anim="up" data-at="1.6">Facture n°0127 envoyée ✓</div>
      </div></div>
      <div class="tag" style="left:0;right:0;text-align:center;top:1415px;font-size:26px">Exemple · données fictives</div>''')
    return s

# ---------- Vendredi : Wave / Orange Money ----------
def vendredi(T, d):
    s = sc(0, T(2), '''<div class="center h" style="top:500px;font-size:110px" data-anim="up">TON CLIENT<br>VEUT PAYER<br><span class="grad">AVEC WAVE ?</span></div>''')
    s += sc(T(2), d, '''
      <div class="phone" style="left:280px;top:300px" data-anim="up"><div class="notch"></div><div class="scr">
        <div style="font-size:28px;color:rgba(255,255,255,.6)">Ma Boutique</div>
        <div style="height:330px;border-radius:30px;margin-top:20px" class="gbg"></div>
        <div style="font-size:36px;font-weight:700;margin-top:24px">Baskets montantes</div>
        <div class="h grad" style="font-size:54px;margin-top:6px">25 000 F</div>
        <div id="w" style="margin-top:40px;padding:30px;border-radius:26px;background:#1DC3F2;color:#0A0A0A;font-weight:800;font-size:34px;text-align:center" data-anim="tap" data-at="{a}">Payer avec Wave</div>
        <div style="margin-top:20px;padding:30px;border-radius:26px;background:#FF7900;color:#0A0A0A;font-weight:800;font-size:34px;text-align:center">Orange Money</div>
      </div>
      <div style="position:absolute;inset:0;background:#111;display:flex;flex-direction:column;align-items:center;justify-content:center" data-anim="fade" data-at="{b}">
        <div style="width:200px;height:200px;border-radius:50%;background:#22c55e;display:flex;align-items:center;justify-content:center;font-size:120px" data-anim="pop" data-at="{b2}">✓</div>
        <div class="h" style="font-size:50px;margin-top:40px">Paiement validé</div></div>
      </div>
      <div class="card" style="position:absolute;left:90px;right:90px;top:180px;padding:34px 40px;display:flex;gap:26px;align-items:center;background:rgba(30,30,30,.95)" data-anim="down" data-at="{c}">
        <div style="width:90px;height:90px;border-radius:24px;flex:none" class="gbg"></div>
        <div><div style="font-size:34px;font-weight:800">🔔 Nouvelle commande</div><div style="font-size:30px;color:rgba(255,255,255,.7)">Baskets montantes · payée par Wave</div></div></div>
      ''' .replace("{b2}", f"{T(12)-T(2)+.2:.2f}").replace("{a}", f"{T(9)-T(2):.2f}").replace("{b}", f"{T(12)-T(2):.2f}").replace("{c}", f"{T(15)-T(2):.2f}"))
    for i, (n, at) in enumerate([("1", T(4)), ("2", T(6)), ("3", T(8))]):
        pass
    return s

# ---------- Samedi : 3 idées reçues ----------
def samedi(T, d):
    s = sc(0, T(3), '''<div class="center h" style="top:500px;font-size:112px" data-anim="up">3 IDÉES<br>REÇUES<br><span class="grad">QUI TE BLOQUENT</span></div>''')
    myths = [("« Un site, c'est pour les grandes entreprises »", "Même une petite boutique peut avoir le sien.", 3, 10, 7),
             ("« Mes clients sont sur Facebook, ça suffit »", "Sur Google, ils cherchent déjà ce que tu vends.", 10, 18, 14),
             ("« C'est trop compliqué à gérer »", "On te livre un outil simple, et on t'accompagne.", 18, 25, 21)]
    for i, (m, r, a, b, f) in enumerate(myths):
        fa = T(f) - T(a)
        s += sc(T(a), T(b), f'''
          <div class="center h grad" style="top:260px;font-size:150px" data-anim="pop">{i+1}</div>
          <div class="card center" style="top:520px;padding:60px 50px;font-size:58px;font-weight:700;line-height:1.2" data-anim="up" data-at=".2">{m}</div>
          <div class="h" style="position:absolute;left:330px;top:880px;font-size:130px;color:#FF3D00;border:10px solid #FF3D00;padding:6px 40px;border-radius:24px" data-anim="stamp" data-at="{fa:.2f}">FAUX</div>
          <div class="center" style="top:1150px;font-size:46px;color:rgba(255,255,255,.85)" data-anim="up" data-at="{fa+.5:.2f}">{r}</div>''')
    s += sc(T(25), d, '''<div class="center h" style="top:560px;font-size:100px" data-anim="up">LAQUELLE<br><span class="grad">TU CROYAIS ?</span></div>
      <div class="center" style="top:900px;font-size:50px" data-anim="pop" data-at=".5">💬 Réponds en commentaire</div>''')
    return s

# ---------- Dimanche 8 : question + offre ----------
def dim8(T, d):
    icons = [("🍽️", "Restaurant"), ("🛍️", "Boutique"), ("🎓", "École"), ("🚚", "Transport")]
    grid = "".join(f'<div class="card" style="position:absolute;left:{110+(i%2)*450}px;top:{560+(i//2)*360}px;width:410px;height:320px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px" data-anim="pop" data-at="{0.2+i*0.35:.2f}"><div style="font-size:120px">{e}</div><div style="font-size:42px;font-weight:700">{n}</div></div>' for i, (e, n) in enumerate(icons))
    s = sc(0, T(3), '''<div class="center h" style="top:520px;font-size:120px" data-anim="up">C'EST QUOI<br><span class="grad">TON BUSINESS ?</span></div>
      <div class="center" style="top:920px;font-size:50px" data-anim="pop" data-at=".6">💬 Dis-le en commentaire</div>''')
    s += sc(T(3), T(10), f'<div class="center h" style="top:300px;font-size:70px" data-anim="up">Restaurant, boutique,<br>école, transport…</div>{grid}')
    s += sc(T(10), d, '''<div class="center" style="top:300px;font-size:50px" data-anim="fade">Ton premier projet avec Aken</div>
      <div style="position:absolute;left:190px;top:420px;width:700px;height:700px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center" class="gbg" data-anim="pop" data-at=".2">
        <div class="h" style="font-size:230px;color:#0A0A0A">-10%</div></div>''')
    return s

SPECS = {
 "dimanche1": dict(voice=V+"dimanche1.mp3", music=M+"amapiano.wav", avatar=AV+"avatar-parle-v1.mp4", scenes=dim1, music_db=-19,
   text="Salut, moi c'est Abdoul, de chez Aken ! Vos clients achètent sur leur téléphone. Et votre boutique, elle est où ? Avec Aken, on crée votre site, votre boutique en ligne et votre appli. Écrivez-nous sur WhatsApp !"),
 "lundi": dict(voice=V+"lundi.mp3", music=M+"afrohouse.wav", scenes=lundi,
   text="Ton business perd des clients chaque jour… et tu ne le sais même pas. Signe numéro un : on te demande ton site, et tu donnes un numéro WhatsApp. Signe numéro deux : on tape ton nom sur Google… et on tombe sur ton concurrent. Signe numéro trois : tu réponds aux mêmes questions, cent fois par jour. Tu te reconnais ? Écris-nous. Aken s'occupe du reste."),
 "mardi": dict(voice=V+"mardi.mp3", music=M+"amapiano.wav", scenes=mardi,
   text="Combien coûte un site internet au Mali ? On te dit tout, sans détour. Un site vitrine chez Aken, c'est à partir de soixante-quinze mille francs CFA. Avec trente jours de suivi inclus après la livraison. Et pour ton premier projet : moins dix pour cent. Boutique en ligne, application, logiciel de gestion ? Le prix dépend de ton besoin. Alors le devis, c'est gratuit, sur WhatsApp."),
 "jeudi": dict(voice=V+"jeudi.mp3", music=M+"lofi.wav", scenes=jeudi,
   text="Fini le cahier de ventes. Avant : des pages raturées, un stock qu'on compte à la main, des factures qui se perdent. Après : tes ventes, ton stock et tes clients, en direct sur ton téléphone. Un logiciel de gestion fait pour ton activité. Par Aken."),
 "vendredi": dict(voice=V+"vendredi.mp3", music=M+"afrohouse.wav", scenes=vendredi,
   text="Ton client veut payer avec Wave ? Regarde comment ça se passe sur une boutique Aken. Un : il choisit son article. Deux : il appuie sur « payer avec Wave » ou « Orange Money ». Trois : il valide sur son téléphone. Et toi ? Tu reçois la commande tout de suite. Simple, rapide, sans espèces."),
 "samedi": dict(voice=V+"samedi.mp3", music=M+"lofi.wav", scenes=samedi,
   text="Trois idées reçues qui empêchent ton business de grandir. Un : « un site, c'est pour les grandes entreprises ». Faux. Même une petite boutique peut avoir le sien. Deux : « mes clients sont sur Facebook, ça suffit ». Faux. Sur Google, ils cherchent déjà ce que tu vends. Trois : « c'est trop compliqué à gérer ». Faux. On te livre un outil simple, et on t'accompagne. Laquelle tu croyais ?"),
 "dimanche8": dict(voice=V+"dimanche8.mp3", music=M+"amapiano.wav", scenes=dim8,
   text="Dis-moi en commentaire : c'est quoi ton business ? Restaurant, boutique, école, transport… Je te réponds avec l'outil qui t'aiderait le plus. Et n'oublie pas : moins dix pour cent sur ton premier projet avec Aken."),
}

def merc(T, d):
    return sc(0, T(4), '''<div class="center" style="top:150px"><span class="pill gbg" style="color:#0A0A0A;font-family:Montserrat;font-weight:900;font-size:40px" data-anim="pop">WHATSAPP OU BOUTIQUE ?</span></div>''') + \
           sc(T(4), d, '''<div class="center" style="top:150px"><span class="pill card" style="font-size:40px" data-anim="down">Paiement Wave · Orange Money</span></div>''')

SPECS["mercredi"] = dict(voice=V+"mercredi.mp3", music=M+"afrohouse.wav", avatar=AV+"avatar-mercredi.mp4", scenes=merc, music_db=-19,
   text="Tu vends encore tout sur WhatsApp ? Les photos, les prix, « c'est combien ? », « c'est dispo ? »… Avec une boutique en ligne, ton client voit tout, choisit, et paie avec Wave ou Orange Money. Même quand tu dors. Ça, c'est Aken.")
