import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_kateisosto_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

    def test_maukkaan_lounaan_kateisosto_toimii(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)

    def test_jos_maksu_riittava_edullinen_lounas_kasvattaa_kateissaldoa_ja_antaa_vaihtorahaa_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(vaihtoraha, 260)

    def test_jos_maksu_riittava_maukas_lounas_kasvattaa_kateissaldoa_ja_antaa_vaihtorahaa_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)
        self.assertEqual(vaihtoraha, 100)

    def test_jos_maksu_riittava_edullinen_lounas_kasvattaa_myytyjen_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_jos_maksu_riittava_maukas_lounas_kasvattaa_myytyjen_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_jos_maksu_ei_riittava_edullinen_lounas_palauttaa_rahat_ja_lounaiden_maara_ei_muutu(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_jos_maksu_ei_riittava_maukas_lounas_palauttaa_rahat_ja_lounaiden_maara_ei_muutu(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_jos_kortilla_riittavasti_rahaa_edullisen_lounaan_osto_toimii_kortilla_ja_palautetaan_true(self):
        osto = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(osto, True)

    def test_jos_kortilla_riittavasti_rahaa_maukkaan_lounaan_osto_toimii_kortilla_ja_palautetaan_true(self):
        osto = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(osto, True)

    def test_jos_kortilla_riittavasti_rahaa_edullisen_lounaan_osto_nostaa_myytyjen_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_jos_kortilla_riittavasti_rahaa_maukkaan_lounaan_osto_nostaa_myytyjen_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_jos_kortilla_ei_riittavasti_rahaa_edullisen_lounaan_osto_ei_muuta_kortin_saldoa_eika_lounaiden_maaraa_ja_palautetaan_false(self):
        maksukortti = Maksukortti(100)
        osto = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(maksukortti.saldo_euroina(), 1.00)
        self.assertEqual(osto, False)

    def test_jos_kortilla_ei_riittavasti_rahaa_maukkaan_lounaan_osto_ei_muuta_kortin_saldoa_eika_lounaiden_maaraa_ja_palautetaan_false(self):
        maksukortti = Maksukortti(100)
        osto = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(maksukortti.saldo_euroina(), 1.00)
        self.assertEqual(osto, False)

    def test_edullisen_lounaan_ostaminen_kortilla_ei_muuta_kassan_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)

    def test_maukkaan_lounaan_ostaminen_kortilla_ei_muuta_kassan_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        
    def test_kortille_rahaa_ladattaessa_kortin_saldo_kasvaa_ja_kassan_kateissaldo_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.00)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1010.00)

    def test_kortille_ei_voi_ladata_negatiivista_maaraa_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
