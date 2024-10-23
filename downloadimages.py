from simple_image_download import simple_image_download as simp
response = simp.simple_image_download
keywords = [
    'surf exel soap bar and its expiry date',
    'closeup toothpaste packed with and without expiry date',
    'dabur almond oil 290 ml and its expiry date',
    'medimix soap 625gm and its expiry date',
    'nivea cream 300ml and its expiry date',
    'pears soap and its expiry date',
    'steelobrite scrubpad',
    'Shri Rajbhog Premium Lotus Seeds (Makhana)',
    'tropicana 125ml mixed fruits juice and its expiry date',
    'tropicana 180ml mixed fruits juice and its expiry date',
    'tropicana 180ml pomegranate delight juice and its expiry date',
    'pepsi 2.25L bottle and its expiry date',
    'pepsi 400ml bottle and its expiry date',
    'gits dhokla mix pack of 1 and its expiry date',
    'gits dhokla mix pack of 4 and its expiry date',
    'knorr soup and its expiry date',
    'chings vegetable noodles and its expiry date',
    'milky bikis biscuits and its expiry date',
    'treat orange wafers and its expiry date',
    'crax masti masala snack and its expiry date',
    'haldiram fata fat bhel and its expiry date',
    'PVR 4700 Popcorn and its expiry date',
    'Aachi Sambar Powder 100g and its expiry date'
]
for keyword in keywords:
  response().download(keyword,10)
  