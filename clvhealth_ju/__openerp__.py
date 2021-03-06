# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol                  #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################

{
    'name': 'CLVhealth-Ju',
    'version': '1.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'description': '''
This module will install all the necessary modules for the CLVhealth-Ju solution.
    ''',
    'depends': [
        'clv_base',
        'clv_tag',
        'clv_annotation',
        'clv_person',
        'clv_patient',
        ],
    'data': [
        'clvhealth_ju_view.xml',
        'clv_tag_sequence.xml',
        'clv_annotation_sequence.xml',
        'clv_person_sequence.xml',
        'clv_person_category_sequence.xml',
        'clv_patient_sequence.xml',
        'clv_patient_category_sequence.xml',
        ],
    'test': [],
    'installable': True,
    'active': False,
}
