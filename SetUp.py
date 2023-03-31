import pandas


english = [
    "Sana'a", "Aden", "Taiz", "Al hudaydah", "Ibb", "Dhamar", "Hadramaut", "Al mahwit", "Al jawf", "Lahij", "Shabwah", "Marib", "Raymah", "Al bayda", "Hajjah", "Sa'dah", "Amran", "Al dhale'e", "Abyan", "Al mahra", "Socotra"
]

arabic = [
    "صنعاء", "عدن", "تعز", "الحديدة", "إب", "ذمار", "المحويت", "حضرموت", "الجوف", "لحج", "شبوة", "مأرب", "ريمة", "البيضاء", "حجة", "صعدة", "عمران", "الضالع", "أبين", "المهرة", "سقطرى"
]

yemen_governorate = {
    'City': english,
    'x': [-365, -320, -410, -480, -375, -375, 0, -440, -265, -335, -185, -275, -420, -295, -465, -420, -400, -345, -220, 215, 420],
    'y': [0, -250, -200, -60, -140, -95, 50, -30, 65, -210, -85, -20, -90, -120, 45, 110, 50, -160, -170, 90, -280]
}

new = pandas.DataFrame(yemen_governorate)
new.to_csv('Cities.csv')
