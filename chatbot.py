events = [
    {
        "name": "Tech Fest 2026",
        "date": "10 October 2026",
        "venue": "Main Auditorium",
        "description": "A technical event featuring coding competitions, workshops and project exhibitions."
    },
    {
        "name": "Cultural Fest 2026",
        "date": "15 October 2026",
        "venue": "College Open Ground",
        "description": "A cultural celebration with music, dance and various student performances."
    },
    {
        "name": "Hackathon 2026",
        "date": "20 October 2026",
        "venue": "Innovation Lab",
        "description": "A coding event where participants develop innovative solutions to real-world problems."
    }
]


def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! 👋 I'm EventEase. I can help you find information about events and announcements."

    if "event" in user_input or "events" in user_input:
        response = "📅 Upcoming Events:\n\n"

        for event in events:
            response += (
                f"• {event['name']}\n"
                f"  Date: {event['date']}\n"
                f"  Venue: {event['venue']}\n\n"
            )

        return response

    for event in events:
        if event["name"].lower().replace(" ", "") in user_input.replace(" ", ""):
            return (
                f"📌 {event['name']}\n\n"
                f"Date: {event['date']}\n"
                f"Venue: {event['venue']}\n"
                f"Details: {event['description']}"
            )

    if "tech" in user_input:
        return (
            "📌 Tech Fest 2026\n\n"
            "Date: 10 October 2026\n"
            "Venue: Main Auditorium\n"
            "Includes coding competitions, workshops and project exhibitions."
        )

    if "cultural" in user_input:
        return (
            "📌 Cultural Fest 2026\n\n"
            "Date: 15 October 2026\n"
            "Venue: College Open Ground\n"
            "Includes music, dance and student performances."
        )

    if "hackathon" in user_input:
        return (
            "📌 Hackathon 2026\n\n"
            "Date: 20 October 2026\n"
            "Venue: Innovation Lab\n"
            "A coding event focused on developing innovative solutions."
        )

    if "bye" in user_input:
        return "Goodbye! 👋 Have a great day."

    return (
        "I'm sorry, I couldn't understand that. "
        "Try asking about upcoming events, Tech Fest, Cultural Fest or Hackathon."
    )