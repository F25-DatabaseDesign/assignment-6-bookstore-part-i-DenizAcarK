from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)
categories = [
    [1, "Self-help"],
    [2, "Language Learning"],
    [3, "Artificial Inteligence and Computer Networks"],
    [4, "Poetry"]
]

books = [
    [1, 1, "The Element", "Sir Ken Robinson", "18-9900", 18.50, "element.jpg", 1],
    [2, 1, "48 Laws of Power", "Robert Greene", "18-9901", 25.5, "48rules.jpg", 0],
    [3, 1, "Walking Beside the Edge", "Lori A. Caputo", "18-9902", 9.99, "beside_the_edge.jpg", 0],
    [4, 1, "Tao Te Ching", "Laozi", "18-9903", 27.99, "laozi.jpg", 0], 
    [5, 2, "How to Learn a Foreign Language", "Paul Pimsleur", "18-9904", 16.50, "learn_languages.jpg", 0],
    [6, 2, "Intermediate Langauge Lessons", "Emma Serl", "18-9905", 22.50, "language_lessons.jpg", 0], 
    [7, 2, "Latin 101: Learning a Classical Language", "Hans-Friedrich Mueller", "18-9906", 27.99, "latin.jpg", 0], 
    [8, 2, "The Principles of Language Learning and Teaching", "H. Douglas Brown", "18-9907", 28.50, "principles_of_lang.jpg", 0], 
    [9, 3, "Technologies et Protocoles Internet", "Promethee Spathis", "18-9908", 79.99, "spathis.jpg", 1],
    [10, 3, "Artificial Intelligence and Quantum Computing for Advanced Wireless Networks", "Savo Glisic", "18-9909", 49.99, "quantum.jpg", 0],
    [11, 3, "Computer Networking: A Top Down Approach", "Kurose Ross", "18-9910", 36.99, "comp_networking.jpg", 0],
    [12, 3, "Artificial Intelligence for Autonomous Networks", "Mazin Gilbert", "18-9911", 42.00, "autonomous_net.jpg", 0],
    [13, 4, "The Sonnets", "William Shakespeare", "18-9912", 22.50, "the_sonnets.png", 0],
    [14, 4, "The Divine Comedy", "Dante Alighieri", "18-9913", 32.10, "divine_comedy.jpg", 0],
    [15, 4, "Paradise Lost", "John Milton", "18-9914", 19.99, "paradise_lost.jpg", 0],
    [16, 4, "The Iliad", "Homer", "18-9915", 12.00, "iliad.jpg", 0]

]
# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]



# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template("index.html", categories=categories)

@app.route('/category')
def category():
    #store the categoryId passed as a URL parameter into a variable
    category_id = request.args.get("categoryId", type=int)

    # Create a new list called selected_books containing a list of books that have the selected category
    selected_books = [b for b in books if b[1] == category_id]

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    return render_template(
        "category.html",
        selectedCategory=category_id,
        categories=categories,
        books = selected_books
    )

@app.route('/search', methods=['POST'])
def search():
    #Link to the search results page.
    return render_template('error.html', error="Search functionality not yet implemented")

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
