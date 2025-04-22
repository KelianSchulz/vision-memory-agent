# 🧠 Reflection Agent – Forschungstagebuch

## Projektidee

Ein visueller Agent, der erkennt, wenn sein Ziel fehlerhaft ist,  
und sich sprachgestützt ein neues Ziel vorschlagen lässt.  
Er verändert sein Verhalten in Schleifen, bis er erfolgreich ist.

---

## Aktueller Zustand

- Ziel: visuell relevante Bilder zu einem gegebenen Zieltext finden
- Mechanismus:
  - CLIP zur Bewertung der Relevanz
  - GPT zur Zielreflexion bei Misserfolg
  - Selbstständiges Weiterlaufen mit neuem Ziel
- Erfolgskriterium: mindestens 5 relevante Treffer bei Score > 0.29

---

## Erste Forschungsfrage (Entwurf)

> Wie erkennt ein Agent, dass sein Ziel fehlerhaft ist –  
und wie effektiv ist sprachbasierte Zielreflexion im Vergleich zu alternativen Mechanismen?

---

## Was funktioniert bisher

- Agent erkennt Zielversagen (`len(agent_memory) < threshold`)
- GPT generiert neue Zielvorschläge
- Agent übernimmt erstes GPT-Ziel automatisch
- Zielpfade sind nachvollziehbar (werden geloggt)
- Bilder werden korrekt gespeichert und visualisiert

---

## Offene Fragen

- Wie stark driften Zielvorschläge semantisch vom Ausgangspunkt ab?
- Wie relevant sind die Vorschläge im Verhältnis zum Dataset?
- Wie könnte der Agent aus früheren Erfolgen lernen?
- Braucht es eine semantische Metrik zwischen Zielen?

---

## Nächste Schritte

- Zielverlauf automatisch loggen (mit Scores, GPT-Vorschlägen, Trefferquote)
- Vergleich: GPT vs. statische Alternativen vs. CLIP-basierte Reflektion
- Visualisierung als Entscheidungsgraph (Ziel → GPT → Ziel → Erfolg)
- Paper-Skizze anlegen?
