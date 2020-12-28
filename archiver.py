from jinja2 import Environment, PackageLoader, select_autoescape

from src.core import films


def main():
    # Start by creating a Jinja2 renderer
    env = Environment(
        loader=PackageLoader("archiver", "templates"),
        autoescape=select_autoescape(["html"]),
    )

    # Set up the dist folder
    film_years = films.get.years()
    films.make.dist(film_years)

    # Create the search page
    render_opts = {
        "page_title": "Search",
        "page_class": "search",
    }
    films.make.page("search.html", data=films.make.render("search", render_opts, env))

    # Next, we are going to generate a site index.
    # The site index will contain a list of links
    # to the available years and, when clicked,
    # will take us to that year's folder
    render_opts = {
        "page_title": "Home",
        "page_class": "index",
        "years": film_years,
    }
    films.make.page("index.html", data=films.make.render("index", render_opts, env))

    # For each year we have films,
    # record the data for the films in that year
    film_data = []
    for year in film_years[0:4]:
        films_in_year = films.get.films_in_year(year)
        film_data.extend(films_in_year)
        print(films_in_year)

    # Create a JSON file that we can use in the final site
    # to provide a basic searchable film directory
    films.make.search_json(film_data)


if __name__ == "__main__":
    main()
