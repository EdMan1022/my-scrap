import os

import pyeloqua


bulk = pyeloqua.Bulk(
    username=os.environ['USERNAME'],
    password=os.environ['PASSWORD'],
    company=os.environ['COMPANY']
)

print('')
