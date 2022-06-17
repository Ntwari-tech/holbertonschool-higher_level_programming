-- this scripts creates database and table in a given server
CREATE DATABASE IF NOT EXISTS hbtn_0d_cities;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) references hbtn_0d_usa.states(id)
);