-- mysql create user pin
  CREATE USER 'pin'@'%' IDENTIFIED VIA mysql_native_password USING 'pin';  
  GRANT ALL PRIVILEGES ON *.* TO 'pin'@'%' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;CREATE DATABASE IF NOT EXISTS `pin`;
  GRANT ALL PRIVILEGES ON `pin`.* TO 'pin'@'%';

-- drops
  /*
    drop table agendamentos;
    drop table contato;
    drop table profissional;
  */

-- ajustar sql_modes
show variables like 'sql_mode'; --NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION
SET sql_mode = '';

-- consutas
select * from agendamentos limit 10;
select * from contato limit 10;
select * from profissional limit 10;