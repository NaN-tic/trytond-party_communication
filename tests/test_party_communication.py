#!/usr/bin/env python
#This file is part party_communication module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
import unittest
import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends
from trytond.tests.test_tryton import doctest_setup, doctest_teardown


class PartycommunicationTestCase(unittest.TestCase):
    '''Test Party Communication module'''

    def setUp(self):
        trytond.tests.test_tryton.install_module('party_communication')

    def test0005views(self):
        '''Test views'''
        test_view('party_communication')

    def test0006depends(self):
        '''Test depends'''
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PartycommunicationTestCase))
    return suite
