from covid import Covid
cases = Covid().get_status_by_country_name("Japan")
for x in cases:
    print(x, ":", cases[x])