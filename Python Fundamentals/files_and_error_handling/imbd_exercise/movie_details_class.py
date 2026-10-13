class MovieDetails:
    def __init__ (self, titleType, primaryTitle, startYear, runtime, genres):
        self.titleType = titleType
        self.primaryTitle = primaryTitle
        self.startYear = startYear
        self.runtime =runtime
        self.genres = genres

    def yearFilter(self):
        included = False
        if int(self.startYear) >= 2010:
            included = True
        return included

    def titleTypeFilter(self):
        included = False
        if self.titleType == "movie":
            included = True
        return included

    def getList(self):
        return [self.titleType, self.primaryTitle, self.startYear, self.runtime, self.genres]



        


