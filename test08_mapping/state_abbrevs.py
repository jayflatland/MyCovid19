
state_and_abbrev_pairs = [
    ("Alabama",                 "AL"),
    ("Alaska",                  "AK"),
    ("Arizona",                 "AZ"),
    ("Arkansas",                "AR"),
    ("California",              "CA"),
    ("Colorado",                "CO"),
    ("Connecticut",             "CT"),
    ("Delaware",                "DE"),
    ("District of Columbia",    "DC"),
    ("Florida",                 "FL"),
    ("Georgia",                 "GA"),
    ("Guam",                    "GU"),
    ("Hawaii",                  "HI"),
    ("Idaho",                   "ID"),
    ("Illinois",                "IL"),
    ("Indiana",                 "IN"),
    ("Iowa",                    "IA"),
    ("Kansas",                  "KS"),
    ("Kentucky",                "KY"),
    ("Louisiana",               "LA"),
    ("Maine",                   "ME"),
    ("Maryland",                "MD"),
    ("Massachusetts",           "MA"),
    ("Michigan",                "MI"),
    ("Minnesota",               "MN"),
    ("Mississippi",             "MS"),
    ("Missouri",                "MO"),
    ("Montana",                 "MT"),
    ("Nebraska",                "NE"),
    ("Nevada",                  "NV"),
    ("New Hampshire",           "NH"),
    ("New Jersey",              "NJ"),
    ("New Mexico",              "NM"),
    ("New York",                "NY"),
    ("North Carolina",          "NC"),
    ("North Dakota",            "ND"),
    ("Ohio",                    "OH"),
    ("Oklahoma",                "OK"),
    ("Oregon",                  "OR"),
    ("Pennsylvania",            "PA"),
    ("Puerto Rico",             "PR"),
    ("Rhode Island",            "RI"),
    ("South Carolina",          "SC"),
    ("South Dakota",            "SD"),
    ("Tennessee",               "TN"),
    ("Texas",                   "TX"),
    ("Utah",                    "UT"),
    ("Vermont",                 "VT"),
    ("Virgin Islands",          "VI"),
    ("Virginia",                "VA"),
    ("Washington",              "WA"),
    ("West Virginia",           "WV"),
    ("Wisconsin",               "WI"),
    ("Wyoming",                 "WY"),
]


state_to_abbrev = {
    k: v for (k, v) in state_and_abbrev_pairs
}

abbrev_to_state = {
    k: v for (k, v) in state_and_abbrev_pairs
}