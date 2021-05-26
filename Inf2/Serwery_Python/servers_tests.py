# <Łukasz> <Orpik>, <302892>

# !/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from collections import Counter

server_types = (ListServer, MapServer)


class ErrorTest(unittest.TestCase):
    def test_throw_error(self):
        products = [Product('PP234', 2), Product('Pa235', 3), Product('Pc234', 2), Product('Pd235', 3),
                    Product('Pe234', 2), Product('Pf235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertRaises(TooManyProductsFoundError, client.get_total_price(2))


class ServerTest(unittest.TestCase):

    def test_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([products[2], products[1]]), Counter(entries))

    def test_get_entries_returns_sorted_entries(self):
        products = [Product('PA12', 142), Product('PP234', 5), Product('PP235', 8)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([products[1], products[2], products[0]]), Counter(entries))


class ClientTest(unittest.TestCase):
    def test_total_price_for_normal_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(5, client.get_total_price(2))

    def test_total_price_for_abnormal_execution(self):
        # list zgodnych produktow jest za dluga
        products = [Product('PP234', 2), Product('Pa235', 3), Product('Pc234', 2), Product('Pd235', 3),
                    Product('Pe234', 2), Product('Pf235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(None, client.get_total_price(2))

        # list zgodnych produktow jest pusta
        print('teraz pusta  ')
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(None, client.get_total_price(5))


if __name__ == '__main__':
    unittest.main()


