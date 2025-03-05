class Media:
    def __init__(self, title=""):
        self.title = title
        self.reviews = []

    def set_title(self, title):
        self.title=title
    def get_title(self):
        return self.title
    def aggiungi_valutazione(self, voto):
        if voto == 1<voto<5:
            self.reviews.append(voto)
        return self.reviews
    def get_media(self):
        for elem in self.reviews:
            somma= sum(elem)
            media= somma//len(self.reviews)
        return round(media)
    def get_rate(self):
        if self.reviews:
            pass
    def rate_percentage(self, voto):
        pass
    def recensione(self):
        pass