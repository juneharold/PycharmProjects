from covid import Covid
cases = Covid().get_status_by_country_id(1)
for x in cases:
    print(x, ":", cases[x])