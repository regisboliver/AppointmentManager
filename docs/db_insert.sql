-- insert contato
select * from contato;
select cast(criado_em as datetime) from contato;
insert into contato (nome, email, telefone) values ('Reginaldo Oliveira', 'reginaldo.oliveira22@gmail.com', '11971959993');
insert into contato (nome, email, telefone) values ('Nicolas Briz', 'nicolaz.briz@gmail.com', '11922223333');
insert into contato (nome, email, telefone) values ('Victor Rommler', 'victor.rommler@gmail.com', '11933334444');

-- insert agendamento
select * from agendamentos;
insert into agendamentos (contato_id, profissional_id, data, duracao) values ('c1bf3699-e6f4-4697-b6fc-0694227881d8', 'c8dff8bd-3146-4518-a31f-549947d2e459', '2024-11-11 08:00:00', '30');
insert into agendamentos (contato_id, profissional_id, data, duracao) values ('c1bf3699-e6f4-4697-b6fc-0694227881d8', 'c8dff8bd-3146-4518-a31f-549947d2e459', '2024-11-11 08:00:00', '30');
insert into agendamentos (contato_id, profissional_id, data, duracao) values ('c1bf3699-e6f4-4697-b6fc-0694227881d8', 'c5a292b6-4c6e-47e8-8c09-caf7eee6c1ee', '2024-11-11 08:00:00', '30');
insert into agendamentos (contato_id, profissional_id, data, duracao) values ('c1bf3699-e6f4-4697-b6fc-0694227881d8', 'c5a292b6-4c6e-47e8-8c09-caf7eee6c1ee', '2024-11-11 08:00:00', '30');
insert into agendamentos (contato_id, profissional_id, data, duracao) values ('53b730da-4daa-4590-ba63-d4c7b09d595f', 'c5a292b6-4c6e-47e8-8c09-caf7eee6c1ee', '2024-11-11 08:00:00', '30');

-- insert profissional
select * from profissional;
insert into profissional (nome, sala, especialidade) values ('Profissional 1', 'Sala 1', 'Especialidade 1');
insert into profissional (nome, sala, especialidade) values ('Profissional 2', 'Sala 2', 'Especialidade 2');
insert into profissional (nome, sala, especialidade) values ('Profissional 3', 'Sala 3', 'Especialidade 3');