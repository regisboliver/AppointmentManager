-- mysql - criando usuário e banco de dados
  -- drop database appmgr;
  -- drop user 'appmgr'@'%';

  create database appmgr;
  create user 'appmgr'@'%' identified by 'masterkey';
  grant select, insert, delete, update on appmgr.* to 'appmgr'@'%';

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
  select * from contato limit 10;
    select concat('- Id: ', id, ', Nome: ', nome, ', Email: ', email, ', Telefone: ', telefone, ', Documento: ', documento) from contato
    --insert into contato (id, nome, email, telefone, documento) values (1, 'teste', 'teste', 'teste', 'teste');
  select * from agendamentos limit 10;
  select * from profissional limit 10;
