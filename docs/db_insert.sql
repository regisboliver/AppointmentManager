-- insert contato
select * from contato;
insert into contato (nome, email, telefone) values ('Reginaldo Oliveira', 'reginaldo.oliveira22@gmail.com', '11971959993');
insert into contato (nome, email, telefone) values ('Nicolas Briz', 'nicolaz.briz@gmail.com', '11922223333');
insert into contato (nome, email, telefone) values ('Victor Rommler', 'victor.rommler@gmail.com', '11933334444');

-- insert agendamento
select * from agendamentos;
insert into agendamentos (contato_id, profissional_id, data, duracao) values ('6d7cfb9a-9ee9-11ef-a3d0-d8bbc16e0872', '85405688-9ee9-11ef-a3d0-d8bbc16e0872', '2024-11-11 08:00:00', '30');
insert into agendamentos (contato_id, profissional_id, data, duracao) values ('6d7cfb9a-9ee9-11ef-a3d0-d8bbc16e0872', '85405688-9ee9-11ef-a3d0-d8bbc16e0872', '2024-11-11 08:00:00', '30');
insert into agendamentos (contato_id, profissional_id, data, duracao) values ('6d7d3e6c-9ee9-11ef-a3d0-d8bbc16e0872', '854099e3-9ee9-11ef-a3d0-d8bbc16e0872', '2024-11-11 08:00:00', '30');
insert into agendamentos (contato_id, profissional_id, data, duracao) values ('6d7d3e6c-9ee9-11ef-a3d0-d8bbc16e0872', '854099e3-9ee9-11ef-a3d0-d8bbc16e0872', '2024-11-11 08:00:00', '30');
insert into agendamentos (contato_id, profissional_id, data, duracao) values ('6d7d7ef6-9ee9-11ef-a3d0-d8bbc16e0872', '854099e3-9ee9-11ef-a3d0-d8bbc16e0872', '2024-11-11 08:00:00', '30');

-- insert profissional
select * from profissional;
insert into profissional (nome, sala, especialidade) values ('Profissional 1', 'Sala 1', 'Especialidade 1');
insert into profissional (nome, sala, especialidade) values ('Profissional 2', 'Sala 2', 'Especialidade 2');
insert into profissional (nome, sala, especialidade) values ('Profissional 3', 'Sala 3', 'Especialidade 3');