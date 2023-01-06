farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
user_input = input("select a farm: NE, W or SiE").lower()

for farm in farms:
    if farm.get("name").lower() == user_input + " farm":
        print(farm.get("agriculture"))
