"""A Yelp-powered Restaurant Recommendation Program"""

from abstractions import *
from data import ALL_RESTAURANTS, CATEGORIES, USER_FILES, load_user_file
from ucb import main, trace, interact
from utils import distance, mean, zip, enumerate, sample
from visualize import draw_map

##################################
# Phase 2: Unsupervised Learning #
##################################

def find_closest(location, centroids):
    """Return the centroid in centroids that is closest to location.
    If multiple centroids are equally close, return the first one.
    
    >>> find_closest([3.0, 4.0], [[0.0, 0.0], [2.0, 3.0], [4.0, 3.0], [5.0, 5.0]])
    [2.0, 3.0]
    """
    # BEGIN Question 3
    right_centroids = min(centroids, key = lambda x: distance(location, x))
    return right_centroids
    
    # END Question 3


def group_by_first(pairs):
    """Return a list of pairs that relates each unique key in the [key, value]
    pairs to a list of all values that appear paired with that key.

    Arguments:
    pairs -- a sequence of pairs

    >>> example = [ [1, 2], [3, 2], [2, 4], [1, 3], [3, 1], [1, 2] ]
    >>> group_by_first(example)
    [[2, 3, 2], [2, 1], [4]]
    """
    keys = []
    for key, _ in pairs:
        if key not in keys:
            keys.append(key)
    return [[y for x, y in pairs if x == key] for key in keys]
    """
    刚开始时，Keys 序列是空的。随后让pairs序列进入，其中key,_ 分别代表第零个元素和第一个元素。for语句的判断条件是，第零个元素不能重复出现.
    所以，keys = [1, 3, 2]。程序进入return 语句，在小的结构中，判断 x == key, 其中key 是大结构中的 'for key in keys',所以外层循环是 对key序列，
    分别等于 1, 3, 2 时。for example, 当 key == 1 时，进行小循环，在pairs 序列中，寻找符合条件 'x == key'即为 'x == 1', 选出其中的 x = 1 
    所以先会得出[2, 3, 2], 接下来进行 key == 3 的循环，找出 pairs 序列中的 [2, 1],最后是 key ==2。最终得出结论，[[2, 3, 2], [2, 1], [2]].
    """


def group_by_centroid(restaurants, centroids):
    """Return a list of clusters, where each cluster contains all restaurants
    nearest to a corresponding centroid in centroids. Each item in
    restaurants should appear once in the result, along with the other
    restaurants closest to the same centroid.
    """
    # BEGIN Question 4
   
    unmodified_list = [[find_closest(restaurant_location(r), centroids), r] for r in restaurants]
    return group_by_first(unmodified_list)
     
    # END Question 4


def find_centroid(cluster):
    """Return the centroid of the locations of the restaurants in cluster."""
    # BEGIN Question 5
   
    centroid_location_list = [restaurant_location(restaurant) for restaurant in cluster]
    centroid_location_lon = mean([x[0] for x in centroid_location_list])
    centroid_location_lat = mean([x[1] for x in centroid_location_list])
    return [centroid_location_lon, centroid_location_lat]


    # END Question 5


def k_means(restaurants, k, max_updates=100):
    """Use k-means to group restaurants by location into k clusters."""
    assert len(restaurants) >= k, 'Not enough restaurants to cluster'
    old_centroids, n = [], 0
    # Select initial centroids randomly by choosing k different restaurants
    centroids = [restaurant_location(r) for r in sample(restaurants, k)]

    while old_centroids != centroids and n < max_updates:
        old_centroids = centroids
        # BEGIN Question 6
        restaurant_list = group_by_centroid(restaurants, centroids)

        centroid = [find_centroid(x) for x in restaurant_list]

        # END Question 6
        n += 1
    return centroids


################################
# Phase 3: Supervised Learning #
################################


def find_predictor(user, restaurants, feature_fn):
    """Return a rating predictor (a function from restaurants to ratings),
    for a user by performing least-squares linear regression using feature_fn
    on the items in restaurants. Also, return the R^2 value of this model.

    Arguments:
    user -- A user
    restaurants -- A sequence of restaurants
    feature_fn -- A function that takes a restaurant and returns a number
    """
    reviews_by_user = {review_restaurant_name(review): review_rating(review)
                       for review in user_reviews(user).values()}

    xs = [feature_fn(r) for r in restaurants]
    ys = [reviews_by_user[restaurant_name(r)] for r in restaurants]

    # BEGIN Question 7
    Sxx = sum([(i - mean(xs))**2 for i in xs])
    Syy = sum([(i - mean(ys))**2 for i in ys])
    Sxy = sum([(i - mean(xs)) * (j + mean(ys)) for i, j in zip(xs, ys)])
    
    b = Sxy/Sxx
    a = mean(ys) - b*mean(xs)
    r_squared = (Sxy**2)/(Sxx * Syy)


    def predictor(restaurant):
        return b * feature_fn(restaurant) + a

    return predictor, r_squared


def best_predictor(user, restaurants, feature_fns):
    """Find the feature within feature_fns that gives the highest R^2 value
    for predicting ratings by the user; return a predictor using that feature.

    Arguments:git
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of functions that each takes a restaurant
    """
    reviewed = user_reviewed_restaurants(user, restaurants)
    # BEGIN Question 8
    
    other_key ={}
    for right_func in feature_fns:
        p, r = find_predictor(user, reviewed, right_func)
        other_key[p] = r
    return max(other_key, key = other_key.get)
    
    """
    return max([find_predictor(user, reviewed, i) for i in feature_fns], key = lambda x: x[1])[0]
    """
    # END Question 8


def rate_all(user, restaurants, feature_fns):
    """Return the predicted ratings of restaurants by user using the best
    predictor based on a function from feature_fns.

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of feature functions
    """
    predictor = best_predictor(user, ALL_RESTAURANTS, feature_fns)
    reviewed = user_reviewed_restaurants(user, restaurants)
    
    predictions = {}
    for restaurant in restaurants:
        rest_name = restaurant_name(restaurant)
        if restaurant in reviewed:
            rest_rating = user_rating(user, rest_name)
            predictions[rest_name] = rest_rating
        else:
            predictions[rest_name] = predictor(restaurant)

    return predictions


    # END Question 9



def search(query, restaurants):
    """Return each restaurant in restaurants that has query as a category.

    Arguments:
    query -- A string
    restaurants -- A sequence of restaurants
    """
    # BEGIN Question 10
    
    return [i for i in restaurants if query in restaurant_categories(i)]
    # END Question 10


def feature_set():
    """Return a sequence of feature functions."""
    return [lambda r: mean(restaurant_ratings(r)),
            restaurant_price,
            lambda r: len(restaurant_ratings(r)),
            lambda r: restaurant_location(r)[0],
            lambda r: restaurant_location(r)[1]]


@main
def main(*args):
    import argparse
    parser = argparse.ArgumentParser(
        description='Run Recommendations',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-u', '--user', type=str, choices=USER_FILES,
                        default='test_user',
                        metavar='USER',
                        help='user file, e.g.\n' +
                        '{{{}}}'.format(','.join(sample(USER_FILES, 3))))
    parser.add_argument('-k', '--k', type=int, help='for k-means')
    parser.add_argument('-q', '--query', choices=CATEGORIES,
                        metavar='QUERY',
                        help='search for restaurants by category e.g.\n'
                        '{{{}}}'.format(','.join(sample(CATEGORIES, 3))))
    parser.add_argument('-p', '--predict', action='store_true',
                        help='predict ratings for all restaurants')
    parser.add_argument('-r', '--restaurants', action='store_true',
                        help='outputs a list of restaurant names')
    args = parser.parse_args()

    # Output a list of restaurant names
    if args.restaurants:
        print('Restaurant names:')
        for restaurant in sorted(ALL_RESTAURANTS, key=restaurant_name):
            print(repr(restaurant_name(restaurant)))
        exit(0)

    # Select restaurants using a category query
    if args.query:
        restaurants = search(args.query, ALL_RESTAURANTS)
    else:
        restaurants = ALL_RESTAURANTS

    # Load a user
    assert args.user, 'A --user is required to draw a map'
    user = load_user_file('{}.dat'.format(args.user))

    # Collect ratings
    if args.predict:
        ratings = rate_all(user, restaurants, feature_set())
    else:
        restaurants = user_reviewed_restaurants(user, restaurants)
        names = [restaurant_name(r) for r in restaurants]
        ratings = {name: user_rating(user, name) for name in names}

    # Draw the visualization
    if args.k:
        centroids = k_means(restaurants, min(args.k, len(restaurants)))
    else:
        centroids = [restaurant_location(r) for r in restaurants]
    draw_map(centroids, restaurants, ratings)