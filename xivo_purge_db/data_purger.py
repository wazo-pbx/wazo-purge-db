# -*- coding: utf-8 -*-

# Copyright (C) 2015 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import logging

logger = logging.getLogger(__name__)


class DataPurger(object):

    def __init__(self, table_purgers):
        self.table_purgers = table_purgers

    def delete_old_entries(self, days_to_keep, session):
        logger.info('Deleting entries older than {0} days'.format(days_to_keep))
        for table in self.table_purgers:
            table.purge(days_to_keep, session)
            logger.debug('{purger} executed'.format(purger=table.__class__.__name__))
