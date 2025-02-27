DROP TABLE users;

CREATE TABLE `users` (
  `user_id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `user_login` VARCHAR(50) UNIQUE,
  `user_password_hash` CHAR(60),
  `user_email` VARCHAR(255),
  `is_user_active` TINYINT(1),
  `user_last_name` VARCHAR(50),
  `user_first_name` VARCHAR(50),
  `user_patronymic` VARCHAR(50),
  `user_job_position` VARCHAR(100),
  `user_contact_info` VARCHAR(255),
  `user_short_description` VARCHAR(255),
  `user_full_description` TEXT,
  `user_children_count` TINYINT UNSIGNED,
  `user_birth_date` DATE,
  `user_created_at` TIMESTAMP,
  `user_updated_at` TIMESTAMP
);


INSERT INTO `users` (
  `user_id`, `user_login`, `user_password_hash`, `user_email`, `is_user_active`,
  `user_last_name`, `user_first_name`, `user_patronymic`, `user_job_position`,
  `user_short_description`, `user_full_description`, `user_children_count`,
  `user_birth_date`, `user_created_at`, `user_updated_at`) VALUES
  (1, 'ivan_89', 'qwerty123hashxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'ivan89@example.com', 1,
  'Иванов', 'Иван', 'Александрович', 'Программист',
  'Люблю программировать.', 'Работаю разработчиком более 10 лет.', 2,
  '1989-04-15', '2024-02-13 12:00:00', '2024-02-13 12:00:00'),
  (2, 'petr_92', 'securehash456xxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'petr92@example.com', 1,
  'Петров', 'Петр', 'Викторович', 'Системный администратор',
  'Обеспечиваю стабильную работу серверов.', 'Работаю в сфере IT с 2015 года.', 1,
  '1992-07-22', '2024-02-13 12:00:00', '2024-02-13 12:00:00');
