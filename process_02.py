import pyproms
import time
from datetime import datetime

# declare Reporting System
rs = pyproms.ProvAgent('Fake NEXIS 02',
                                  uri='http://fake.com/rs/NEXIS',
                                  actedOnBehalfOf=pyproms.ProvAgent('Laura Stanford',
                                                                    uri='http://pid.geoscience.gov.au/person/u15873'))

# use Output 01
with open('output_dataset_01.txt', 'r') as f:
    text = f.read()
# prov log Dataset 01
e1 = pyproms.ProvEntity('Input Dataset 01',
                        'http://pid.geosceince.gov.au/dataset/xyz')


# fake processing
# prov log Activity
startedAtTime = datetime.now()
time.sleep(3)
endedAtTime = datetime.now()


# generate Output 02
# output dataset 1
with open('output_dataset_02.txt', 'w') as f:
    f.write('This is output 2')
e_out = pyproms.ProvEntity('Output Dataset 02',
                           'http://pid.geosceince.gov.au/dataset/xyz_2',
                           #wasAttributedTo=rs,
                           created=endedAtTime)


a = pyproms.ProvActivity('NEXIS processing 2',
                         startedAtTime=startedAtTime,
                         endedAtTime=endedAtTime,
                         wasAssociatedWith=rs,
                         used_entities=[e1],
                         generated_entities=[e_out])

# Report generation
r = pyproms.PromsExternalReport('NEXIS Report 2',
                                reportingSystem=pyproms.PromsReportingSystem('Fake RS'),
                                nativeId='NEXIS run #34 2',
                                reportActivity=a)

with open('report2.ttl', 'w') as f:
    f.write(r.get_graph().serialize(format='turtle'))