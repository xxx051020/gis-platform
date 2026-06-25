CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE IF NOT EXISTS points_of_interest (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    description TEXT DEFAULT '',
    lng DOUBLE PRECISION NOT NULL,
    lat DOUBLE PRECISION NOT NULL,
    geom GEOMETRY(POINT, 4326)
);

CREATE TABLE IF NOT EXISTS regions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    label VARCHAR(100) DEFAULT '',
    description TEXT DEFAULT '',
    geom GEOMETRY(POLYGON, 4326)
);

-- Sample POIs for Guangzhou
INSERT INTO points_of_interest (name, category, description, lng, lat, geom) VALUES
('广州塔', 'landmark', '广州地标建筑，塔高600米', 113.3245, 23.1095, ST_GeomFromText('POINT(113.3245 23.1095)', 4326)),
('白云山', 'park', '国家5A级旅游景区', 113.2969, 23.1867, ST_GeomFromText('POINT(113.2969 23.1867)', 4326)),
('天河体育中心', 'landmark', '位于天河区核心地段', 113.3230, 23.1350, ST_GeomFromText('POINT(113.3230 23.1350)', 4326)),
('广州南站', 'transport', '华南地区最大高铁枢纽', 113.2722, 22.9884, ST_GeomFromText('POINT(113.2722 22.9884)', 4326)),
('陈家祠', 'landmark', '岭南建筑艺术明珠', 113.2481, 23.1279, ST_GeomFromText('POINT(113.2481 23.1279)', 4326)),
('珠江新城', 'landmark', '广州CBD核心区域', 113.3249, 23.1199, ST_GeomFromText('POINT(113.3249 23.1199)', 4326)),
('越秀公园', 'park', '广州最大的综合性公园', 113.2678, 23.1411, ST_GeomFromText('POINT(113.2678 23.1411)', 4326)),
('广州白云国际机场', 'transport', '华南航空枢纽', 113.3000, 23.3924, ST_GeomFromText('POINT(113.3000 23.3924)', 4326));