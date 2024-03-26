import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    # Tämä failaa nykyisellä toteutuksella
    def test_rahan_lataaminen_ei_onnistu_jos_negatiivinen_talletus(self):
        self.maksukortti.lataa_rahaa(-1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortin_saldo_vahenee_oikein_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_kortin_saldo_vahenee_nollaan_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.00 euroa")

    def test_kortin_saldo_ei_vahene_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_metodi_palauttaa_true_jos_rahat_riittavat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(999), True)

    def test_metodi_palauttaa_false_jos_rahat_eivat_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1001), False)

    def test_metodi_palauttaa_saldon_euroina(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)
