from bing_image_urls import bing_image_urls

def get_image_by_word(word):
    image = bing_image_urls(word, limit=1)
    return image[0]

def get_image_for_place(places, settlement):
    for place in places:
        place["image_url"] = get_image_by_word(place['name'] + " " + settlement['settlement'])
    return places