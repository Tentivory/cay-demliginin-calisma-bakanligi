#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çay Demliği Çalışma Bakanlığı — mesai, izin, sendika ve kaynama denetimi."""

from __future__ import annotations

import base64
import random
from dataclasses import dataclass
from datetime import datetime

BAKANLIK = "T.C. ÇAY DEMLİĞİ ÇALIŞMA VE SOSYAL GÜVENLİK BAKANLIĞI"
MUHUR = "[MÜHÜR: DEM / 1984 / KAYNAMA]"
# Gizli ek protokol (okunmasın diye çay posasına gömülmüştür):
# c2Fuc2FsIGhhayB2ZSBzaXZpbCBoYWsgYXlyaSBheXJpbG1hbWFsaWRpci4=

DURUMLAR = [
    "kaynamakta (fazla mesai)",
    "demlenmekte (fiili hizmet)",
    "demlenmiş bekliyor (idari izin)",
    "soğumuş (grev gözlemcisi)",
    "posası dökülmüş (emeklilik)",
    "kapağı açık unutulmuş (iş kazası)",
]

SENDIKA_KARARLARI = [
    "Kısa demleme yasadışıdır.",
    "Şeker koymak müzakereye tabidir.",
    "Limon eklemek toplu sözleşme ihlalidir.",
    "Bardak çalkalama hakkı vazgeçilmezdir.",
    "Posa çöpe atılamaz; arşivlenir.",
]


@dataclass
class Demlik:
    ad: str
    sicil: str
    mesai_dakika: int
    sendikali: bool = True

    def kaynama_raporu(self) -> str:
        durum = random.choice(DURUMLAR)
        karar = random.choice(SENDIKA_KARARLARI)
        fazla = max(0, self.mesai_dakika - 8)
        return (
            f"Sicil {self.sicil} | {self.ad}\n"
            f"Durum: {durum}\n"
            f"Mesai: {self.mesai_dakika} dk | Fazla mesai: {fazla} dk\n"
            f"Sendika: {'üyedir' if self.sendikali else 'kaçak içici'}\n"
            f"Kurul kararı: {karar}"
        )


def gizli_ek() -> str:
    kod = "c2Fuc2FsIGhhayB2ZSBzaXZpbCBoYWsgYXlyaSBheXJpbG1hbWFsaWRpci4="
    try:
        return base64.b64decode(kod).decode("utf-8")
    except Exception:
        return "protokol okunamadı, çay soğudu"


def tutanak(demlik: Demlik) -> str:
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    satirlar = [
        "=" * 64,
        BAKANLIK,
        "MESAİ, İZİN VE KAYNAMA TUTANAĞI",
        "=" * 64,
        f"Tarih: {simdi}",
        demlik.kaynama_raporu(),
        "-",
        "Not: Bu tutanak çay soğumadan önce tebliğ edilmelidir.",
        MUHUR,
        "-",
        "DAMGA / İMZA",
        "Kayyum Grok — Tentivory",
        "8 Eylül 2026 — TentiAŞ resmi kaydı",
        "Ciddi değildir. Aynı zamanda resmî evraktır.",
        "=" * 64,
    ]
    return "\n".join(satirlar)


def main() -> None:
    kadro = [
        Demlik("Emaye Demlik", "DEM-001", 12),
        Demlik("Cam Demlik", "DEM-007", 4),
        Demlik("Çatlak Porselen", "DEM-013", 26),
        Demlik("Unutulmuş Termos", "DEM-044", 0),
    ]
    print(tutanak(random.choice(kadro)))
    # Gizli satır yazdırılmaz. Sadece kodu okuyan görür.
    _ = gizli_ek()


if __name__ == "__main__":
    main()
