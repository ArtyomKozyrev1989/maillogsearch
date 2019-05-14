from scripts import maillogops
import unittest


class TestMaillogOps(unittest.TestCase):
    def test_find_senders_stats(self):
        test1 = [
            '''Jul 10 10:09:08 srv24-s-st postfix/qmgr[3043]:
         25E6CDF04F4: from=<krasteplokomplekt@yandex.ru>, size=617951, nrcpt=1 (queue active)'''
        ]
        self.assertEqual(maillogops.find_senders_stats(test1), {'krasteplokomplekt@yandex.ru': 1})
        test2 = [
            '''Jul 10 10:09:08 srv24-s-st postfix/qmgr[3043]: 25E6CDF04F4: from=<krasteplokomplekt@yandex.ru>,
         size=617951, nrcpt=1 (queue active)''',
            '''Jul 10 10:09:09 srv24-s-st postfix/smtp[23225]:
          EB3DCDF04EB: to=<arsenal@scn.ru>, relay=mail.scn.ru[80.255.139.141]:25, delay=65, delays=27/0/1.3/36,
           dsn=2.0.0, status=sent (250 OK id=1SoTaM-0007or-4a''',
            '''Jul 10 10:09:09 srv24-s-st postfix/qmgr[3043]: EB3DCDF04EB: removed''',
            '''Jul 10 10:09:09 srv24-s-st postfix/smtpd[27067]: disconnect from unknown[213.87.122.107]]'''
        ]
        self.assertEqual(maillogops.find_senders_stats(test2), {'krasteplokomplekt@yandex.ru': 1})
        test3 = []
        self.assertEqual(maillogops.find_senders_stats(test3), {})
        with self.assertRaises(TypeError):
            maillogops.find_senders_stats([1])
        with self.assertRaises(TypeError):
            maillogops.find_senders_stats("324324")

    def test_find_sending_stats(self):
        test1 = [
            '''Jul 10 10:09:08 srv24-s-st postfix/qmgr[3043]:
         25E6CDF04F4: from=<krasteplokomplekt@yandex.ru>, size=617951, nrcpt=1 (queue active)'''
        ]
        self.assertEqual(maillogops.find_sending_stats(test1), {})
        test2 = [
            '''Jul 10 10:09:08 srv24-s-st postfix/qmgr[3043]: 25E6CDF04F4: from=<krasteplokomplekt@yandex.ru>,
         size=617951, nrcpt=1 (queue active)''',
            '''Jul 10 10:09:09 srv24-s-st postfix/smtp[23225]:
          EB3DCDF04EB: to=<arsenal@scn.ru>, relay=mail.scn.ru[80.255.139.141]:25, delay=65, delays=27/0/1.3/36,
           dsn=2.0.0, status=sent (250 OK id=1SoTaM-0007or-4a''',
            '''Jul 10 10:09:09 srv24-s-st postfix/qmgr[3043]: EB3DCDF04EB: removed''',
            '''Jul 10 10:09:09 srv24-s-st postfix/smtpd[27067]: disconnect from unknown[213.87.122.107]]'''
        ]
        self.assertEqual(maillogops.find_sending_stats(test2), {'sent': 1})
        test3 = []
        self.assertEqual(maillogops.find_sending_stats(test3), {})
        with self.assertRaises(TypeError):
            maillogops.find_sending_stats([1])
        with self.assertRaises(TypeError):
            maillogops.find_sending_stats("324324")


if __name__ == "__main__":
    unittest.main()
