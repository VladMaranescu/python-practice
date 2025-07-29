monthconversions = {
    "jan":"january",
    "feb":"february",
    "mar":"march",
    "apr":"april",
    "may":"May",
    "jun":"june",
    "jul":"july",
    "aug":"august",
    "sept":"september",  
    "oct":"october",
    "nov":"november", 
    "dec":"december",      
}

print(monthconversions["nov"])
print(monthconversions.get("dec"))
print(monthconversions.get("lov","not valid "))
