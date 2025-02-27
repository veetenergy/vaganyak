CREATE TABLE `cars` (
  `car_id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT UNSIGNED,
  `car_model` VARCHAR(50),
  `car_color_id` INT UNSIGNED,
  FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`),
  FOREIGN KEY (`car_color_id`) REFERENCES `car_colors`(`car_color_id`)
);


INSERT INTO `cars` (`user_id`, `car_model`, `car_color_id`) VALUES
  (1, 'Toyota Camry', 1),  -- Иванов владеет Toyota Camry черного цвета
  (1, 'BMW X5', 2);         -- Иванов владеет BMW X5 белого цвета
