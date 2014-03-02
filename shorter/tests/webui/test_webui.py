# -*- coding: utf-8 -*-
# Copyright (c) 2014 Ionuț Arțăriși <ionut@artarisi.eu>
# This file is part of shorter.

# shorter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# shorter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with shorter. If not, see <http://www.gnu.org/licenses/>.

import unittest

from selenium import webdriver

from shorter import config


class UITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_shorter_says_hello(self):
        self.driver.get(config.base_url)

        banner = self.driver.find_element_by_id('banner')
        self.assertIn('Hi', banner.text)

    def test_index_has_form(self):
        self.driver.get(config.base_url)

        form = self.driver.find_element_by_id('shorten')
        self.assertEqual(form.tag_name, 'form')
