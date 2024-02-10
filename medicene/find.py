import googlemaps

def find_nearby_pharmacies(api_key, location, radius=5000, keyword='pharmacy'):
    gmaps = googlemaps.Client(key=api_key)
    places = gmaps.places_nearby(location=location, radius=radius, keyword=keyword)

    if 'results' in places:
        pharmacies = places['results']
        return pharmacies
    else:
        return None

def main():
    api_key = 'your_api_key_here'  # Replace with your Google API key
    location = (latitude, longitude)  # Replace with your latitude and longitude coordinates

    pharmacies = find_nearby_pharmacies(api_key, location)

    if pharmacies:
        print("Nearby pharmacies:")
        for pharmacy in pharmacies:
            print(pharmacy['name'], "-", pharmacy.get('vicinity', 'Address not available'))
    else:
        print("No pharmacies found nearby.")

if __name__ == "__main__":
    main()
