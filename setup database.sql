CREATE TABLE `api`.`user` (
  `name` VARCHAR(40) NOT NULL,
  `user_name` VARCHAR(40) NOT NULL,
  `password` VARCHAR(30) NOT NULL);

INSERT INTO api.user (name, user_name, password) VALUES ("John Doe", "jdoe", 'badpassword123');
INSERT INTO api.user (name, user_name, password) VALUES ("Jim Doe", "jimdoe", 'badpassword456');
INSERT INTO api.user (name, user_name, password) VALUES ("Adam McCormack", "amccormack", 'adamspassword123');
INSERT INTO api.user (name, user_name, password) VALUES ("Brian Baggs", "brianbaggs", 'briansbadpass123');
INSERT INTO api.user (name, user_name, password) VALUES ("Leeroy Jenkins", "leeeroy", 'jenkins123456');