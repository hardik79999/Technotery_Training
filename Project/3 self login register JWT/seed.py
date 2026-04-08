import random
import os
from dotenv import load_dotenv
from database import database

# Yeh line env variables ko load karegi!
load_dotenv()

def seed_1000_posts():
    # Humare random topics
    topics = ["Python", "SQL", "Flask", "API", "React", "Database", "NodeJS", "Docker", "AWS", "Machine Learning"]
    
    # Alag-alag frequency wale templates taaki hit_count test ho sake
    templates = [
        
        ("Mastering {t} in 2026", "A deep dive into {t}. {t} is the future, so learn {t} now!"),
        ("Basics of {t}", "Simple introduction to {t}."),
        ("{t} for Beginners", "If you are new to {t}, this {t} guide is for you."),
        ("Ultimate {t} Guide: {t} {t}", "{t} {t} {t} {t}. This is heavily packed with {t} to test your search ranking!"),
        ("Why {t} is awesome", "I love {t}. Every developer should try {t} at least once."),
        ("10 Tips for {t} Developers", "Tip 1: Use {t}. Tip 2: Study {t}. Tip 3: Practice {t}. Tip 4: Master {t}."),
        ("Comparing {t} with alternatives", "{t} is usually better than the rest. Choose {t}."),
        ("My journey with {t}", "When I started with {t}, I didn't know much. Now {t} is my favorite."),
        ("Advanced {t} concepts", "Let's talk about memory management and performance in {t}."),
        ("Is {t} still relevant?", "Yes, {t} is very much alive. Keep coding in {t}.")
    ]

    conn = None
    cursor = None

    try:
        conn = database()
        cursor = conn.cursor()

        sql = "INSERT INTO post (title, description, is_active, created_by) VALUES (%s, %s, %s, %s)"
        values_list = []

        print("Generating 1000 posts... Please wait...")
        
        # 1000 baar loop chalayenge
        for _ in range(1000):
            topic = random.choice(topics)
            template = random.choice(templates)
            
            title = template[0].replace("{t}", topic)
            description = template[1].replace("{t}", topic)
            
            # 90% posts active (1) rakhenge, 10% delete (0) rakhenge
            is_active = random.choices([1, 0], weights=[90, 10])[0] 
            created_by = random.randint(1, 3) # user 1, 2, ya 3
            
            values_list.append((title, description, is_active, created_by))

        # executemany 1000 records ko ek sath fast speed mein database mein bhejta hai
        cursor.executemany(sql, values_list)
        conn.commit()

        print(f"Boom! 💥 {cursor.rowcount} dummy posts successfully inserted into database.")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    seed_1000_posts()