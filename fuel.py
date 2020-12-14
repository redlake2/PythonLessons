import feedparser
import operator
from datetime import date
from flask import Flask
app = Flask(__name__)

# Function to get the fuel
def get_fuel(product_id, which_day):
    data = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Suburb=WILLETTON'+'&Day='+str(which_day))
    return data['entries']

# Function to sort the list by Price
def ByPrice(item):
   return item[0]
  
FuelTypeUnleaded = 1
thisday = 'today'
temp_list = get_fuel(FuelTypeUnleaded, thisday)

today_prices = []
for dictionary in temp_list:
  today_prices.append([float(dictionary['price']),dictionary['updated'],dictionary['trading-name']])

#print(today_prices)

thisday = 'tomorrow'
temp_list = get_fuel(FuelTypeUnleaded, thisday)

tomorrow_prices = []
for dictionary in temp_list:
  tomorrow_prices.append([float(dictionary['price']),dictionary['updated'],dictionary['trading-name']])

#print ('--------------------------------------')
#print(tomorrow_prices)

# Add the two lists together first
bothListsTemp = today_prices + tomorrow_prices

# Sort my list so that it shows the cheapest price first
AllFuelPrices = sorted(bothListsTemp, key=ByPrice)
print(AllFuelPrices)

#SortedList = sorted(AllFuelPrices, key=operator.itemgetter(1, 2))
#print(SortedList)
# Should the list be sorted so that we can have the relevant stations matching?   

#---------------------------------------------------------------------
# We are now going to format the output in the list into a html file.
# Set up our header and end details
my_html_list = ''
html_header_start = '<!DOCTYPE html><html><head><title>Denise''s Fuel List</title>'
html_header_end = '</head><body>'
html_end = '</body></html>'

# Create my style
html_style_detail = '''<style type="text/css">
	body {
		font-family:Arial
	}
	th {
		color: blue;
		text-decoration: bold;
		text-size: 1em;
	}
	.price {
		text-align: right;
	}
</style>'''

ColourPink = "pink"
ColourNone = "white"
today = date.today()
dateStr = today. strftime("%Y-%m-%d")

# Put the fuel values into a table formated in the right order
my_html_list += '<table><tr><th width="300">Name</th><th width="50">Price</th><th width="100">Date</th></tr>'
for word in AllFuelPrices:

    if dateStr != word[1]:
    	my_html_list += f'<tr style ="background-color: lime"><td class="price">{word[2]}</td><td class="price">{word[0]}</td><td class="price">{word[1]}</td></tr>'
    else:
    	my_html_list += f'<tr style ="background-color: pink"><td class="price">{word[2]}</td><td class="price">{word[0]}</td><td class="price">{word[1]}</td></tr>'

my_html_list += '</table>'

# Add all the detail together for the output
my_html = f'''
{html_header_start}
{html_style_detail}
{html_header_end}
<h1>My Fuel List</h1>
<p>This is a list of fuel prices for the Suburb of Willetton and surrounding areas.</p>
{my_html_list}
{html_end}
'''
f = open('fuel.html', 'w')
f.write(my_html)
f.close()






