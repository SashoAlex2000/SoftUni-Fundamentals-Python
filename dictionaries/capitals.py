def capitals():
    countries = input().split(", ")
    capitals_data = input().split(", ")

    result = dict(zip(countries, capitals_data))

    # print(result)

    for country, capital in result.items():
        print(f"{country} -> {capital}")


capitals()