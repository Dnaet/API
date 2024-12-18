
CREATE TABLE IF NOT EXISTS albums (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    album_id INT UNIQUE,  
);

CREATE TABLE IF NOT EXISTS photos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    album_id INT, 
    photo_id INT UNIQUE,
    url VARCHAR(255),
    thumbnail_url VARCHAR(255),
    FOREIGN KEY (album_id) REFERENCES albums(album_id) ON DELETE CASCADE 
);