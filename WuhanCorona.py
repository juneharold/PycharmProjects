from covid import Covid
cases = Covid().get_status_by_country_id(160)
for x in cases:
    print(x, ":", cases[x])