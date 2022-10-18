#detect double spaces in a string
quotes="Many of life’s failures are people who   did not realize how close they were to success when they gave up."
a=quotes.find("  ")
print(a)

b = quotes.replace("  ","")
print(b)