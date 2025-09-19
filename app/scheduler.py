import time
from app.ai_responder import generate_reply

def fetch_reviews():
    return [
        {"review_id": 1, "text": "Great hotel! Loved the service."},
        {"review_id": 2, "text": "Room was too small and noisy."}
    ]

def post_reply(review_id, reply_text):
    print(f"Reply to review {review_id}: {reply_text}")

if __name__ == "__main__":
    while True:
        reviews = fetch_reviews()
        for review in reviews:
            reply = generate_reply(review["text"])
            post_reply(review["review_id"], reply)
        time.sleep(600)
