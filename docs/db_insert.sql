-- insert contato
select * from contato;
/*
  insert into contato (id, nome, email, telefone, documento) values ('53b730da-4daa-4590-ba63-d4c7b09d595f', 'Reginaldo Oliveira', 'reginaldo.oliveira22@gmail.com', '11971959993', 1);
  insert into contato (id, nome, email, telefone, documento) values ('c1bf3699-e6f4-4697-b6fc-0694227881d8', 'Nicolas Briz', 'nicolaz.briz@gmail.com', '11922223333', 2);
  insert into contato (id, nome, email, telefone, documento) values ('6ec3ba76-05a4-4b6e-8fc6-73d9251882dd', 'Victor Rommler', 'victor.rommler@gmail.com', '11933334444', 3);
*/

-- insert profissional
select * from profissional;
/*
  insert into profissional (id, nome, registro, sala, especialidade) values ('c8dff8bd-3146-4518-a31f-549947d2e459', 'Profissional 1', 1, 'Sala 1', 'Especialidade 1');
  insert into profissional (id, nome, registro, sala, especialidade) values ('c5a292b6-4c6e-47e8-8c09-caf7eee6c1ee', 'Profissional 2', 2, 'Sala 2', 'Especialidade 2');
  insert into profissional (id, nome, registro, sala, especialidade) values ('a3ee5385-7ec2-420f-96f8-9ba93233ec03', 'Profissional 3', 3, 'Sala 3', 'Especialidade 3');
*/

-- insert agendamento
select * from agendamentos;
  select format(a.data, 'dd/MM/yyyy HH:mm') "data", concat(a.duracao, ' minutos') "duracao", concat('#', a.codigo) "codigo", c.nome "paciente", p.nome "profissional"
  from agendamentos a
  inner join profissional p on a.profissional_id = p.id
  inner join contato c on a.contato_id = c.id
  order by a.data;

/*
  insert into agendamentos (codigo, contato_id, profissional_id, data, duracao) values (1, 'c1bf3699-e6f4-4697-b6fc-0694227881d8', 'c8dff8bd-3146-4518-a31f-549947d2e459', '2024-11-11 08:00:00', '30');
  insert into agendamentos (codigo, contato_id, profissional_id, data, duracao) values (2, 'c1bf3699-e6f4-4697-b6fc-0694227881d8', 'c8dff8bd-3146-4518-a31f-549947d2e459', '2024-11-11 08:00:00', '30');
  insert into agendamentos (codigo, contato_id, profissional_id, data, duracao) values (3, 'c1bf3699-e6f4-4697-b6fc-0694227881d8', 'c5a292b6-4c6e-47e8-8c09-caf7eee6c1ee', '2024-11-11 08:00:00', '30');
  insert into agendamentos (codigo, contato_id, profissional_id, data, duracao) values (4, 'c1bf3699-e6f4-4697-b6fc-0694227881d8', 'c5a292b6-4c6e-47e8-8c09-caf7eee6c1ee', '2024-11-11 08:00:00', '30');
  insert into agendamentos (codigo, contato_id, profissional_id, data, duracao) values (5, '53b730da-4daa-4590-ba63-d4c7b09d595f', 'c5a292b6-4c6e-47e8-8c09-caf7eee6c1ee', '2024-11-11 08:00:00', '30');
*/
