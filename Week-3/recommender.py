def get_recommendations(user_input):
    user_input = user_input.lower()

    recommendations = []

    if "movie" in user_input:
        recommendations += ["Avengers", "Inception", "Interstellar"]

    if "music" in user_input:
        recommendations += ["Spotify Top Hits", "Arijit Singh Playlist", "Trending Songs"]

    if "cricket" in user_input or "sports" in user_input:
        recommendations += ["IPL Highlights", "ICC World Cup Videos", "Cricket Best Moments"]

    if "tech" in user_input:
        recommendations += ["AI News", "Python Tutorials", "Latest Gadgets"]

    if len(recommendations) == 0:
        return "No recommendations found. Try: movies, music, sports, tech"

    return recommendations


print("=== AI Recommendation System ===")

while True:
    user_input = input("\nEnter your interests: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    result = get_recommendations(user_input)

    print("\nRecommended Items:")
    print(result)