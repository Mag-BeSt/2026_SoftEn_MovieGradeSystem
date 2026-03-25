import csv

def load_movies():
    movies = []
    try:
        with open('movies.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Ensure row has a year key for compatibility
                if 'year' not in row:
                    row['year'] = ''
                # Convert grade to float when possible
                g = row.get('grade', '').strip()
                if g == '':
                    row['grade'] = ''
                else:
                    try:
                        row['grade'] = float(g)
                    except Exception:
                        row['grade'] = g
                movies.append(row)
    except FileNotFoundError:
        pass
    return movies

def save_movies(movies):
    # Define explicit fieldnames to include year
    fieldnames = ['title', 'grade', 'year']
    if movies is None:
        movies = []
    with open('movies.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        # Ensure each movie has all fields
        rows = []
        for m in movies:
            row = {k: m.get(k, '') for k in fieldnames}
            rows.append(row)
        writer.writerows(rows)

def add_movie(movies):
    title = input("Enter movie title: ")
    # Accept float grades (e.g. 8.5)
    while True:
        grade_input = input("Enter grade (1-10, e.g. 8.5): ")
        try:
            grade = float(grade_input)
            break
        except ValueError:
            print("Invalid grade — enter a number like 8.5")
    year = input("Enter release year (optional): ")
    movies.append({'title': title, 'grade': grade, 'year': year})

def list_movies(movies):
    def _grade_value(m):
        g = m.get('grade', '')
        try:
            return float(g)
        except Exception:
            return 0.0
    sorted_movies = sorted(movies, key=_grade_value, reverse=True)

    # Top header line
    print("---- Movies (sorted by highest score) ----")

    if not sorted_movies:
        print("(no movies)")
    else:
        for movie in sorted_movies:
            year = movie.get('year', '')
            year_str = f" ({year})" if year else ''
            g = movie.get('grade', '')
            if isinstance(g, float):
                grade_str = str(int(g)) if g.is_integer() else str(g)
            else:
                grade_str = str(g)
            print(f"{movie['title']}{year_str}: {grade_str}")

    # Bottom footer line with count
    print(f"---- End of list ({len(sorted_movies)} movies) ----")

def main():
    movies = load_movies()
    while True:
        print("1. Add movie")
        print("2. List movies")
        print("3. Save and exit")
        choice = input("Choose: ")
        if choice == '1':
            add_movie(movies)
        elif choice == '2':
            list_movies(movies)
        elif choice == '3':
            save_movies(movies)
            break

if __name__ == "__main__":
    main()