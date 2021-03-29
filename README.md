# Movie-Recommendation-API
An API which recommends movie based on title provided or IMDb ID provided.

**Recommend Movie**
----
  Returns json data with movie recommendations.

* **URL**

  /recommend_movies

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `title=[string]`
        or
   `imdb_id=[string]`

   **Optional:**

   `limit=[integer]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"query": {"limit": 5, "q": "tt0499549", "type": "imdb_id"}, "result": [{"index": 94, "original_title": "Guardians of the Galaxy", "overview": "Light years from Earth, 26 years after being abducted, Peter Quill finds himself the prime target of a manhunt after discovering an orb wanted by Ronan the Accuser.", "release_date": "2014-07-30", "title": "Guardians of the Galaxy", "cast": "Chris Pratt Zoe Saldana Dave Bautista Vin Diesel Bradley Cooper", "director": "James Gunn", "genres": "Action Science Fiction Adventure", "imdb_title_id": "tt2015381", "keywords": "marvel comic spaceship space outer space orphan"}, {"index": 2403, "original_title": "Aliens", "overview": "When Ripley's lifepod is found by a salvage crew over 50 years later, she finds that terra-formers are on the very planet they found the alien species. When the company sends a family of colonists out to investigate her story, all contact is lost with the planet and colonists. They enlist Ripley and the colonial marines to return and search for answers.", "release_date": "1986-07-18", "title": "Aliens", "cast": "Sigourney Weaver Michael Biehn James Remar Paul Reiser Lance Henriksen", "director": "James Cameron", "genres": "Horror Action Thriller Science Fiction", "imdb_title_id": "tt0090605", "keywords": "android extraterrestrial technology space marine spaceman cryogenics"}, {"index": 47, "original_title": "Star Trek Into Darkness", "overview": "When the crew of the Enterprise is called back home, they find an unstoppable force of terror from within their own organization has detonated the fleet and everything it stands for, leaving our world in a state of crisis.  With a personal score to settle, Captain Kirk leads a manhunt to a war-zone world to capture a one man weapon of mass destruction. As our heroes are propelled into an epic chess game of life and death, love will be challenged, friendships will be torn apart, and sacrifices must be made for the only family Kirk has left: his crew.", "release_date": "2013-05-05", "title": "Star Trek Into Darkness", "cast": "Chris Pine Zachary Quinto Zoe Saldana Karl Urban Simon Pegg", "director": "J.J. Abrams", "genres": "Action Adventure Science Fiction", "imdb_title_id": "tt1408101", "keywords": "spacecraft friendship sequel futuristic space"}, {"index": 56, "original_title": "Star Trek Beyond", "overview": "The USS Enterprise crew explores the furthest reaches of uncharted space, where they encounter a mysterious new enemy who puts them and everything the Federation stands for to the test.", "release_date": "2016-07-07", "title": "Star Trek Beyond", "cast": "Chris Pine Zachary Quinto Karl Urban Simon Pegg Zoe Saldana", "director": "Justin Lin", "genres": "Action Adventure Science Fiction", "imdb_title_id": "tt2660888", "keywords": "sequel stranded hatred space opera"}, {"index": 3158, "original_title": "Alien", "overview": "During its return to the earth, commercial spaceship Nostromo intercepts a distress signal from a distant planet. When a three-member team of the crew discovers a chamber containing thousands of eggs on the planet, a creature inside one of the eggs attacks an explorer. The entire crew is unaware of the impending nightmare set to descend upon them when the alien parasite planted inside its unfortunate host is birthed.", "release_date": "1979-05-25", "title": "Alien", "cast": "Tom Skerritt Sigourney Weaver Veronica Cartwright Harry Dean Stanton John Hurt", "director": "Ridley Scott", "genres": "Horror Action Thriller Science Fiction", "imdb_title_id": "tt0078748", "keywords": "android countdown space marine space suit beheading"}]}`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{"query": {"limit": 5, "q": "tt049954", "type": "imdb_id"}, "result": [], "error": "Movie not in Database."}`

  OR

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{"query": {"limit": 5, "q": "", "type": ""}, "result": [], "error": "Empty query."}`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/recommend_movies?imdb_id=tt0499549",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```

Refered article: https://medium.com/@sumanadhikari/building-a-movie-recommendation-engine-using-scikit-learn-8dbb11c5aa4b
