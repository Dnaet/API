
CREATE TABLE IF NOT EXISTS albums (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    album_id INT,
    title VARCHAR(255)
)

CREATE TABLE IF NOT EXISTS photos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    album_id INT,
    photo_id INT,
    title VARCHAR(255),
    url VARCHAR(255),
    thumbnail_url VARCHAR(255)
)

