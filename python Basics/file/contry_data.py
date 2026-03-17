countries_data = [
    {"country_name": "Afghanistan", "capital": "Kabul", "population": 43844000, "is_independent": True, "region": "Asia", "currency": "AFN"},
    {"country_name": "Albania", "capital": "Tirana", "population": 2830000, "is_independent": True, "region": "Europe", "currency": "ALL"},
    {"country_name": "Algeria", "capital": "Algiers", "population": 46800000, "is_independent": True, "region": "Africa", "currency": "DZD"},
    {"country_name": "Argentina", "capital": "Buenos Aires", "population": 46300000, "is_independent": True, "region": "South America", "currency": "ARS"},
    {"country_name": "Australia", "capital": "Canberra", "population": 26800000, "is_independent": True, "region": "Oceania", "currency": "AUD"},
    {"country_name": "Austria", "capital": "Vienna", "population": 9000000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Bangladesh", "capital": "Dhaka", "population": 177100000, "is_independent": True, "region": "Asia", "currency": "BDT"},
    {"country_name": "Belgium", "capital": "Brussels", "population": 11700000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Brazil", "capital": "Brasília", "population": 213300000, "is_independent": True, "region": "South America", "currency": "BRL"},
    {"country_name": "Canada", "capital": "Ottawa", "population": 41500000, "is_independent": True, "region": "North America", "currency": "CAD"},
    {"country_name": "Chile", "capital": "Santiago", "population": 19700000, "is_independent": True, "region": "South America", "currency": "CLP"},
    {"country_name": "China", "capital": "Beijing", "population": 1413000000, "is_independent": True, "region": "Asia", "currency": "CNY"},
    {"country_name": "Colombia", "capital": "Bogotá", "population": 52300000, "is_independent": True, "region": "South America", "currency": "COP"},
    {"country_name": "Denmark", "capital": "Copenhagen", "population": 5900000, "is_independent": True, "region": "Europe", "currency": "DKK"},
    {"country_name": "Egypt", "capital": "Cairo", "population": 119600000, "is_independent": True, "region": "Africa", "currency": "EGP"},
    {"country_name": "Ethiopia", "capital": "Addis Ababa", "population": 137800000, "is_independent": True, "region": "Africa", "currency": "ETB"},
    {"country_name": "Finland", "capital": "Helsinki", "population": 5600000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "France", "capital": "Paris", "population": 66600000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Germany", "capital": "Berlin", "population": 83700000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Greece", "capital": "Athens", "population": 10300000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "India", "capital": "New Delhi", "population": 1472400000, "is_independent": True, "region": "Asia", "currency": "INR"},
    {"country_name": "Indonesia", "capital": "Jakarta", "population": 287200000, "is_independent": True, "region": "Asia", "currency": "IDR"},
    {"country_name": "Iran", "capital": "Tehran", "population": 90100000, "is_independent": True, "region": "Asia", "currency": "IRR"},
    {"country_name": "Iraq", "capital": "Baghdad", "population": 46100000, "is_independent": True, "region": "Asia", "currency": "IQD"},
    {"country_name": "Ireland", "capital": "Dublin", "population": 5100000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Israel", "capital": "Jerusalem", "population": 9400000, "is_independent": True, "region": "Asia", "currency": "ILS"},
    {"country_name": "Italy", "capital": "Rome", "population": 58700000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Japan", "capital": "Tokyo", "population": 122700000, "is_independent": True, "region": "Asia", "currency": "JPY"},
    {"country_name": "Kenya", "capital": "Nairobi", "population": 57200000, "is_independent": True, "region": "Africa", "currency": "KES"},
    {"country_name": "Malaysia", "capital": "Kuala Lumpur", "population": 34800000, "is_independent": True, "region": "Asia", "currency": "MYR"},
    {"country_name": "Mexico", "capital": "Mexico City", "population": 132700000, "is_independent": True, "region": "North America", "currency": "MXN"},
    {"country_name": "Morocco", "capital": "Rabat", "population": 38200000, "is_independent": True, "region": "Africa", "currency": "MAD"},
    {"country_name": "Netherlands", "capital": "Amsterdam", "population": 17700000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "New Zealand", "capital": "Wellington", "population": 5300000, "is_independent": True, "region": "Oceania", "currency": "NZD"},
    {"country_name": "Nigeria", "capital": "Abuja", "population": 240800000, "is_independent": True, "region": "Africa", "currency": "NGN"},
    {"country_name": "Norway", "capital": "Oslo", "population": 5500000, "is_independent": True, "region": "Europe", "currency": "NOK"},
    {"country_name": "Pakistan", "capital": "Islamabad", "population": 257800000, "is_independent": True, "region": "Asia", "currency": "PKR"},
    {"country_name": "Peru", "capital": "Lima", "population": 34800000, "is_independent": True, "region": "South America", "currency": "PEN"},
    {"country_name": "Philippines", "capital": "Manila", "population": 117400000, "is_independent": True, "region": "Asia", "currency": "PHP"},
    {"country_name": "Poland", "capital": "Warsaw", "population": 40500000, "is_independent": True, "region": "Europe", "currency": "PLN"},
    {"country_name": "Portugal", "capital": "Lisbon", "population": 10200000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Russia", "capital": "Moscow", "population": 143500000, "is_independent": True, "region": "Europe/Asia", "currency": "RUB"},
    {"country_name": "Saudi Arabia", "capital": "Riyadh", "population": 37500000, "is_independent": True, "region": "Asia", "currency": "SAR"},
    {"country_name": "South Africa", "capital": "Pretoria", "population": 61200000, "is_independent": True, "region": "Africa", "currency": "ZAR"},
    {"country_name": "South Korea", "capital": "Seoul", "population": 51700000, "is_independent": True, "region": "Asia", "currency": "KRW"},
    {"country_name": "Spain", "capital": "Madrid", "population": 47500000, "is_independent": True, "region": "Europe", "currency": "EUR"},
    {"country_name": "Sweden", "capital": "Stockholm", "population": 10600000, "is_independent": True, "region": "Europe", "currency": "SEK"},
    {"country_name": "Switzerland", "capital": "Bern", "population": 8900000, "is_independent": True, "region": "Europe", "currency": "CHF"},
    {"country_name": "Thailand", "capital": "Bangkok", "population": 71800000, "is_independent": True, "region": "Asia", "currency": "THB"},
    {"country_name": "Turkey", "capital": "Ankara", "population": 87800000, "is_independent": True, "region": "Europe/Asia", "currency": "TRY"},
    {"country_name": "United Kingdom", "capital": "London", "population": 68100000, "is_independent": True, "region": "Europe", "currency": "GBP"},
    {"country_name": "United States", "capital": "Washington, D.C.", "population": 348500000, "is_independent": True, "region": "North America", "currency": "USD"},
    {"country_name": "Vietnam", "capital": "Hanoi", "population": 100300000, "is_independent": True, "region": "Asia", "currency": "VND"}
]



# total number countries

# print(f'total number of countries =',len(countries_data))


# total number of Asian countries
# asian_countries=[c.get("country_name") for c in countries_data if c.get("region")=="Asia"]
# print(f'Asian_countries =,{asian_countries}')

# country with highest population

# countries_with_highest_population=max(countries_data,key=lambda c:c.get("population"))
# print(countries_with_highest_population)

# sort countries wrt  population
countries_with_worst_population=sorted(countries_data,key=lambda c:c.get("population"))
print(countries_with_worst_population)


mapped_country=([ c.get("country_name")for c in countries_with_worst_population])
print(mapped_country)

# display all unique region

# unique_region=[c.get("country_name") for c in countries_data  if c.get("region")=="Asia"]
# print(f"unique_region={unique_region}")

# all_unique_region={c.get("country_name") for c in countries_data}
# print(all_unique_region)

#independent country names




