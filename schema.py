import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="reddit",
    user="postgres",
    password="root"
)

# Create a cursor object
cur = conn.cursor()

# Create the table
cur.execute("""
    DROP TABLE IF EXISTS reddit_posts;
    CREATE TABLE reddit_posts (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        post_id VARCHAR(255) NOT NULL UNIQUE,
        title VARCHAR(500) NOT NULL,
        author VARCHAR(255) NOT NULL,
        url VARCHAR(255) NOT NULL,
        score INTEGER NOT NULL,
        created_utc TIMESTAMP NOT NULL,
        num_comments INTEGER NOT NULL,
        upvote_ratio FLOAT NOT NULL
    );
""")

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()