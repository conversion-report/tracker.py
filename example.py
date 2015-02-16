from conversion_report import ConversionReport

def collect_money(num_dollars):
  '''example function you might want to track conversions in'''

  try:
    put_money_in_bank(num_dollars)
    cr = ConversionReport('HRXPC5JR')
    cr.track()
  except:
    handle_exception()
    raise

def put_money_in_bank(num_dollars):
  pass

def handle_exeption():
  pass
