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
    # zrzuty poziome (np. kadr filmu 16:9) albo kwadratowe (rozłożony Fold) zamiast pionowych z telefonu
    poziome = app.get("poziome", False)
    kwadratowe = app.get("kwadratowe", False)
    w, h = (480, 270) if poziome else (400, 400) if kwadratowe else (270, 480)
    klasa = " poziome" if poziome else " kwadratowe" if kwadratowe else ""
    imgs = "\n".join(
        f'          <a href="../{p}" target="_blank" rel="noopener"><img src="../{p}" alt="{e(opis)}" width="{w}" height="{h}" loading="lazy"></a>'
        for p, opis in app["zrzuty"])
    return f"""    <section class="sec shots-sec">
      <div class="wrap">
        <h2>Zrzuty ekranu</h2>
        <div class="shots{klasa}">
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
        akcja = '<a class="btn" href="../testuj/">Zostań testerem</a>'
        tekst = "Trwa test zamknięty w Google Play. Dołącz do grupy testerów i pobierz aplikację przed premierą."
    elif s == "sprawdzanie":
        akcja = '<a class="btn" href="../testuj/">Dołącz do testerów</a>'
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
<link rel="stylesheet" href="../assets/style.css?v=8">
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


def testuj():
    """Strona /testuj/: jak zostać testerem; z przeglądarki Facebooka przełącza do Chrome."""
    karty = []
    # najpierw test zamknięty (grupa), potem testy wewnętrzne (na e-mail)
    for app in sorted(APLIKACJE, key=lambda a: a["status"] != "test"):
        if app["status"] == "test":
            przyciski = (f'<a class="btn" href="https://play.google.com/apps/testing/{app["pakiet"]}" target="_blank" rel="noopener">Zostań testerem</a>'
                         f'<a class="btn ghost" href="https://play.google.com/store/apps/details?id={app["pakiet"]}" target="_blank" rel="noopener">Pobierz ze Sklepu</a>')
        elif app["status"] == "wewnetrzny":
            przyciski = f'<a class="btn ghost" href="mailto:{MAIL}?subject={e(app["nazwa"])}%20-%20chc%C4%99%20testowa%C4%87">Napisz, by testować</a>'
        else:
            continue
        karty.append(f"""        <div class="t-app">
          <a href="../{app['slug']}/"><img src="../assets/{app['ikona']}" alt="" width="72" height="72"></a>
          <div class="t-txt"><h3><a href="../{app['slug']}/">{e(app['nazwa'])}</a></h3><p>{e(app['krotko'])}</p></div>
          <div class="t-btns">{przyciski}</div>
        </div>""")
    lista = "\n".join(karty)
    return f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zostań testerem — LeoKodum</title>
<meta name="description" content="Sprawdź aplikacje LeoKodum przed premierą w Google Play. Dołącz do grupy testerów i pobierz aplikacje.">
<link rel="icon" type="image/png" href="../assets/favicon.png">
<link rel="stylesheet" href="../assets/style.css?v=8">
<script>
// Przeglądarka wbudowana w Facebooka/Messengera/Instagram nie zna logowania Google — przełącz do Chrome.
(function () {{
  var ua = navigator.userAgent || "";
  var wbudowana = /FBAN|FBAV|FB_IAB|FBIOS|Messenger|Instagram/i.test(ua);
  if (!wbudowana) return;
  document.documentElement.className += " wbudowana";
  if (/Android/i.test(ua)) {{
    var cel = location.host + location.pathname;
    location.href = "intent://" + cel + "#Intent;scheme=https;package=com.android.chrome;S.browser_fallback_url=" + encodeURIComponent(location.href) + ";end";
  }}
}})();
</script>
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
      <div class="chrome-info">
        <p><strong>Otwórz tę stronę w Chrome.</strong> Przeglądarka w Facebooku nie widzi Twojego konta Google, więc dołączenie do testów się nie uda.</p>
        <a class="btn" id="do-chrome" href="intent://leokodum.pl/testuj/#Intent;scheme=https;package=com.android.chrome;end">Otwórz w Chrome</a>
        <p class="muted">Nie działa? Dotknij ⋮ w prawym górnym rogu i wybierz „Otwórz w przeglądarce”.</p>
      </div>
      <p class="eyebrow">Testy w Google Play</p>
      <h1>Zostań testerem</h1>
      <p class="lead">Sprawdź nasze aplikacje przed premierą. Potrzebny jest telefon z Androidem i konto Google. Testy są bezpłatne.</p>
    </div>
  </section>

  <section class="sec">
    <div class="wrap steps">
      <div class="step">
        <span class="nr">1</span>
        <div>
          <h2>Dołącz do grupy testerów</h2>
          <p>Otwórz grupę w Chrome, na swoim koncie Google, i kliknij „Dołącz do grupy”. Jeśli widzisz komunikat o braku dostępu, najpierw zaloguj się na konto Google.</p>
          <a class="btn" href="{GRUPA}" target="_blank" rel="noopener">Dołącz do grupy</a>
        </div>
      </div>
      <div class="step">
        <span class="nr">2</span>
        <div>
          <h2>Wybierz aplikację</h2>
          <p>Przy wybranej aplikacji kliknij „Zostań testerem”, a potem „Pobierz ze Sklepu”. Gdy Sklep jeszcze jej nie pokazuje, odczekaj kilka minut po dołączeniu do grupy.</p>
        </div>
      </div>
      <div class="step">
        <span class="nr">3</span>
        <div>
          <h2>Korzystaj przez 14 dni</h2>
          <p>Nie odinstalowuj aplikacji przez 14 dni. Uwagi i błędy wysyłaj na <a href="mailto:{MAIL}">{MAIL}</a>. Każda opinia bardzo nam pomaga.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="sec alt">
    <div class="wrap">
      <h2>Aplikacje do testowania</h2>
      <div class="t-list">
{lista}
      </div>
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


os.makedirs(os.path.join(KORZEN, "testuj"), exist_ok=True)
with open(os.path.join(KORZEN, "testuj", "index.html"), "w", encoding="utf-8") as f:
    f.write(testuj())
print("ok testuj")

for app in APLIKACJE:
    d = os.path.join(KORZEN, app["slug"])
    os.makedirs(d, exist_ok=True)
    for p, _ in app.get("zrzuty", []):
        assert os.path.exists(os.path.join(KORZEN, p)), p
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(strona(app))
    print("ok", app["slug"])
