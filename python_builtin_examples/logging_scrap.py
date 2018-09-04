import logging
logging.basicConfig(format='%(asctime)s %(message)s')

try:
    raise NotImplementedError

except Exception as e:
    logging.error(': Exception raised', exc_info=True)
    raise e

print('lol')
