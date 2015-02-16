import requests, json

class ConversionReport(object):

  def __init__(self, id):
    '''Accepts one argument, an integer tracking id id'''

    super(ConversionReport, self).__init__()
    self.url = 'http://www.conversion.report/conversions'
    self.headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    self.id = id
    self.payload = {'conversion':{'tracking_id':self.id}}

  def __repr__(self):
    return self.id

  def __str__(self):
    return self.id

  def track(self):
    r = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers)
    return r
