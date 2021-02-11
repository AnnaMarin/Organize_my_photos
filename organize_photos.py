import os

def extract_place(file_name):
    return file_name.split("_")[1]


def make_place_directories(places):
    for place in places:
        os.mkdir(place)


def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = []
    for filename in originals:
        place = extract_place(filename)
        if place not in places:
            places.append(place)
#make place directories
    make_place_directories(places)
#move files to directories
    for filename in originals:
        place = extract_place(filename)
        os.rename(filename,os.path.join(place, filename))

organize_photos("Photos")
