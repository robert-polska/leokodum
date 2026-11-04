#!/usr/bin/env python3
"""Generuje podstrony aplikacji (<slug>/index.html) z danych w tools/aplikacje.py.
Uruchom z katalogu repo: python3 tools/strony_aplikacji.py"""
import html
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from aplikacje import APLIKACJE, GRUPA, MAIL, TEL, TEL_LINK  # noqa: E402

KORZEN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = html.escape


def sekcje(app):
    out = []
    for tytul, punkty in app["sekcje"]:
        lis = "\n".join(f"          <li>{p}</li>" for p in punkty)
        out.append(f"""      <section class="feat">
        <h2>{e(tytul)}</h2>
        <ul>
{lis}
        </ul>
      </section>""")
    return "\n".join(out)


def galeria(app):
    if not app.get("zrzuty"):
        return """    <section class="sec shots-sec">
      <div class="wrap">
        <h2>Zrzuty ekranu</h2>
        <p class="muted">Zrzuty ekranu pojawią się tu wkrótce.</p>
      </div>
    </section>"""
    # zrzuty poziome (np. kadr filmu 16:9) zamiast pionowych z telefonu
    poziome = app.get("poziome", False)
    w, h = (480, 270) if poziome else (270, 480)
    imgs = "\n".join(
        f'          <a href="../{p}" target="_blank" rel="noopener"><img src="../{p}" alt="{e(opis)}" width="{w}" height="{h}" loading="lazy"></a>'
        for p, opis in app["zrzuty"])
    return f"""    <section class="sec shots-sec">
      <div class="wrap">
        <h2>Zrzuty ekranu</h2>
        <div class="shots{' poziome' if poziome else ''}">
{imgs}
        </div>
      </div>
    </section>"""


def film(app):
    if not app.get("film"):
        return ""
    return f"""    <section class="sec">
      <div class="wrap">
        <h2>Film</h2>
        <div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{app['film']}" title="{e(app['nazwa'])} — film" loading="lazy" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
      </div>
    </section>"""


def status(app):
    s = app["status"]
    akcja = ""
    if s == "test":
        akcja = f'<a class="btn" href="{GRUPA}" target="_blank" rel="noopener">Zostań testerem</a>'
        tekst = "Trwa test zamknięty w Google Play. Dołącz do grupy testerów, a potem otwórz link do testu tej aplikacji."
    elif s == "sprawdzanie":
        akcja = f'<a class="btn" href="{GRUPA}" target="_blank" rel="noopener">Dołącz do testerów</a>'
        tekst = "Aplikacja jest sprawdzana przez Google. Potem trafi do testów w grupie testerów."
    elif s == "wewnetrzny":
        akcja = f'<a class="btn" href="mailto:{MAIL}?subject={e(app["nazwa"])}%20-%20chc%C4%99%20testowa%C4%87">Napisz, by testować</a>'
        tekst = "Trwają testy wewnętrzne. Chcesz spróbować? Napisz do nas, a dodamy Cię do testów."
    else:
        tekst = "Aplikacja jest w przygotowaniu do Google Play."
    return f'<div class="status"><p>{tekst}</p>{akcja}</div>'


def strona(app):
    polityka = (f'<a href="polityka-prywatnosci.html">Polityka prywatności</a>'
                if os.path.exists(os.path.join(KORZEN, app["slug"], "polityka-prywatnosci.html")) else "")
    return f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(app['nazwa'])} — LeoKodum</title>
<meta name="description" content="{e(app['krotko'])}">
<link rel="icon" type="image/png" href="../assets/favicon.png">
<link rel="stylesheet" href="../assets/style.css?v=4">
</head>
<body>

<header class="top">
  <div class="wrap top-in">
    <a class="brand" href="../"><img src="../assets/lew.png" alt="" width="40" height="40"><span>LeoKodum</span></a>
    <nav>
      <a href="../#aplikacje">Aplikacje</a>
      <a href="../#kontakt">Kontakt</a>
    </nav>
  </div>
</header>

<main>
  <section class="app-hero">
    <div class="wrap">
      <a class="back" href="../#aplikacje">← Wszystkie aplikacje</a>
      <div class="app-head">
        <img class="app-ico" src="../assets/{app['ikona']}" alt="" width="128" height="128">
        <div>
          <p class="eyebrow">{e(app['tag'])}</p>
          <h1>{e(app['nazwa'])}</h1>
          <p class="lead">{app['wstep']}</p>
        </div>
      </div>
      {status(app)}
    </div>
  </section>

{galeria(app)}
{film(app)}
  <section class="sec">
    <div class="wrap feats">
{sekcje(app)}
    </div>
  </section>

  <section class="sec alt">
    <div class="wrap">
      <p class="muted">{app['uwaga']}</p>
      <p class="links">{polityka}</p>
    </div>
  </section>
</main>

<footer class="foot">
  <div class="wrap">
    <span>© 2026 LeoKodum · <a href="mailto:{MAIL}">{MAIL}</a> · <a href="tel:{TEL_LINK}">{TEL}</a> · <a href="https://www.facebook.com/leokodum" target="_blank" rel="noopener">Facebook</a></span>
  </div>
</footer>

</body>
</html>
"""


for app in APLIKACJE:
    d = os.path.join(KORZEN, app["slug"])
    os.makedirs(d, exist_ok=True)
    for p, _ in app.get("zrzuty", []):
        assert os.path.exists(os.path.join(KORZEN, p)), p
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(strona(app))
    print("ok", app["slug"])
