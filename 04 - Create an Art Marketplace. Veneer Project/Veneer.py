class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return "{}. '{}'. {}, {}. {}, {}.".format(self.artist, self.title, self.year, self.medium, self.owner.name,
                                                  self.owner.location)


class Marketplace:
    def __init__(self, listings):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, listing):
        self.listings.remove(listing)

    def show_listings(self):
        for item in self.listings:
            print(item)


class Client:
    def __init__(self, name, location='Private Collection', is_museum=True):
        self.name = name
        self.location = location
        self.is_museum = is_museum

    def __repr__(self):
        return "{}. {}. {}".format(self.name, self.location, self.is_museum)

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_list = Listing(artwork, price, self)
            veneer.add_listing(new_list)

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            for listing in veneer.listings:
                if listing.art == artwork:
                    listing.art.owner = self
                    veneer.remove_listing(listing)


class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return "{} for {}".format(self.art.title, self.price)


veneer = Marketplace("New listing")

edytta = Client("Edytta Halpirt", is_museum=False)

girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)', 'oil on canvas', 1910, edytta)

moma = Client("The MOMA", "New York")

edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")

moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)

veneer.show_listings()
