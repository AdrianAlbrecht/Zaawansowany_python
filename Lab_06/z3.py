import os
import stat

def main():
    os.makedirs("PoryRoku", exist_ok=True)

    seasons = ["wiosna", "lato", "jesień", "zima"]
    months = ["marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień", "styczeń", "luty"]

    for i in range(len(seasons)):
        season_path = os.path.join("PoryRoku", seasons[i])
        os.makedirs(season_path, exist_ok=True)

        for j in range(0+(i*3), 3+(i*3)):
            month_path = os.path.join(season_path, months[j])
            os.makedirs(month_path, exist_ok=True)

    os.chmod("PoryRoku", stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)


if __name__ == "__main__":
    main()
