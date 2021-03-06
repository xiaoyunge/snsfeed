#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Wang Xuerui <idontknw.wang@gmail.com>
#
# This file is part of snsfeed.
#
# snsfeed is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# snsfeed is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
# License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with snsfeed.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals, absolute_import

from ..feed import txweibo

PROVIDER_MAP = {
        't.qq.com': txweibo.TXWeiboFeed,
        }


class ProviderNotSupportedError(Exception):
    pass


def _get_feed_generator(source_type, source_id):
    try:
        feed = PROVIDER_MAP[source_type](source_id)
    except KeyError:
        raise ProviderNotSupportedError

    return feed.generate_feed()


def generate_rss(source_type, source_id):
    fg = _get_feed_generator(source_type, source_id)
    return fg.rss_str()


def generate_atom(source_type, source_id):
    fg = _get_feed_generator(source_type, source_id)
    return fg.atom_str()


# vim:set ai et ts=4 sw=4 sts=4 fenc=utf-8:
