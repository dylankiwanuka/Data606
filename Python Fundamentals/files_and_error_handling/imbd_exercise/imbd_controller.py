import csv
from movie_details_class import MovieDetails
def extract(file):
    try:
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")

            #print(csv_reader)

            iterable_csv = iter(csv_reader) 
            next(iterable_csv)
            return(list(iterable_csv))

    except FileNotFoundError as errmsg:
        print("There has been a FileNotFoundError")
        print(errmsg)

def transform(data):
    transformedData = []
    for row in data:
        movie = MovieDetails(row[0],row[1],row[4],row[6],row[7])
        if movie.yearFilter() == True and movie.titleTypeFilter() == True:
            transformedData.append(movie.getList())
    return transformedData

def load(transformedData, newFile):
    try:
        with open(newFile, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(["titleType", "primaryTitle", "startYear", "runtime", "genres"])
                writer.writerows(transformedData)

    except FileNotFoundError as errmsg:
        print("There has been a FileNotFoundError")

load(transform(extract("imdbtitles.csv")), "completedTask.csv")


    


