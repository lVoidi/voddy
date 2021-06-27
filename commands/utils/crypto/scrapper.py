import cryptocompare

def get_info(crypto : str) -> dict:
  crypto = cryptocompare.get_avg(crypto.upper())
  
  if crypto == None:
    return None
  
  return dict(
    low=crypto['LOW24HOUR'],
    high=crypto['HIGH24HOUR'],
    actual = crypto['PRICE']
  )
  
