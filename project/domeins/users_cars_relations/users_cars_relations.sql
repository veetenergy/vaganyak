CREATE TABLE `users_cars_relations` (
  `relation_id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT UNSIGNED,
  `car_id` INT UNSIGNED,
  FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE,
  FOREIGN KEY (`car_id`) REFERENCES `cars`(`car_id`) ON DELETE CASCADE
);


INSERT INTO `users_cars_relations` (`user_id`, `car_id`) VALUES
  (1, 1), -- Иванов владеет черной Toyota Camry
  (1, 2); -- Иванов владеет белой BMW X5
