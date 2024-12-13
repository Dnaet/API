CREATE TABLE albums (
    id INTEGER PRIMARY KEY,        
    title TEXT NOT NULL,             
    userId INTEGER NOT NULL         
);

CREATE TABLE photos (
    id INTEGER PRIMARY KEY,               
    title TEXT NOT NULL,                 
    url TEXT NOT NULL,                    
    thumbnailUrl TEXT NOT NULL,       
    albumId INTEGER NOT NULL,            
    FOREIGN KEY (albumId) REFERENCES albums(id)  
);

CREATE TABLE geos (
    id_geo INT AUTO_INCREMENT PRIMARY KEY,
    lat DECIMAL(10, 6),
    lng DECIMAL(10, 6)
);

CREATE TABLE addresses (
    id_address INT AUTO_INCREMENT PRIMARY KEY,
    street VARCHAR(255),
    suite VARCHAR(255),
    city VARCHAR(255),
    zipcode VARCHAR(20),
    geo_id INT,
    FOREIGN KEY (geo_id) REFERENCES geos(id_geo)
);

CREATE TABLE companies (
    id_company INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(255),
    catchPhrase VARCHAR(255),
    bs VARCHAR(255)
);

CREATE TABLE users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    username VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    website VARCHAR(255),
    address_id INT,
    company_id INT,
    FOREIGN KEY (address_id) REFERENCES addresses(id_address),
    FOREIGN KEY (company_id) REFERENCES companies(id_company)
);

CREATE TABLE todos (
    id_todo INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    completed BOOLEAN,
    userId INT,
    FOREIGN KEY (userId) REFERENCES users(id_user)
);

conn.commit()
    conn.close()