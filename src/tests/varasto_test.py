import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        
    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertEqual(self.varasto.saldo, 0)

    def test_konstruktorissa_asetetaan_tilavuus_oikein_jos_tilavuuden_alkuarvo_nolla_tai_pienempi(self):
        self.varasto = Varasto(-10)
        
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_konstruktorin_alku_saldo_pienempi_kuin_nolla_kuitenkin_saldon_pitaa_on_nolla(self):
        self.varasto = Varasto(10,alku_saldo=-1)
        # puukotetaan alku_saldo attrubuutti negatiiviseksi
        
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivinen_lisays_varastoon_palauttaa_none(self):
        
        self.assertEqual(self.varasto.lisaa_varastoon(-8), None)

    def test_lisays_varastoon_enemmän_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(12)
        #tyhjässä varastossa on oletuksena tilaa 10, yritetään sijoittaa 12, 10 saadaan sopimaan 
        self.assertEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        
        saatu_maara = self.varasto.ota_varastosta(2)
        
        self.assertAlmostEqual(saatu_maara, 2)

    def test_otetaan_negatiivinen_maara(self):
        
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)


    def test_otetaan_enemmän_kuin_varastossa(self):
        self.varasto = Varasto(10,alku_saldo=10)
        
        self.varasto.ota_varastosta(20)
        
        # varastosta on yritetty ottaa kaksinkertaisesti mitä siellä on, saadaan saldon verran
        self.assertAlmostEqual(self.varasto.saldo,0)


    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varaston_status_tulostus(self):
        self.varasto = Varasto(10,alku_saldo=5)
        
        self.assertEqual(self.varasto.__str__(),"saldo = 5, vielä tilaa 5")
