CREATE TABLE `contato` (
  `id` integer PRIMARY KEY,
  `criado_em` timestamp,
  `nome` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `telefone` varchar(20) NOT NULL,
  `documento` varchar(14) DEFAULT null,
  `endereco_rua` varchar(50) DEFAULT null,
  `endereco_numero` varchar(10) DEFAULT null,
  `endereco_bairro` varchar(50) DEFAULT null,
  `endereco_cidade` varchar(50) DEFAULT null,
  `endereco_uf` varchar(2) DEFAULT null,
  `endereco_cep` varchar(8) DEFAULT null,
  `endereco_complemento` varchar(50) DEFAULT null,
  `observacao` varchar(255) DEFAULT null
);

CREATE TABLE `profissional` (
  `id` integer PRIMARY KEY,
  `criado_em` timestamp,
  `nome` varchar(50) NOT NULL,
  `sala` varchar(20) NOT NULL,
  `especialidade` varchar(20) NOT NULL,
  `indisponibilidade` varchar(20)
);

CREATE TABLE `agendamentos` (
  `id` integer PRIMARY KEY,
  `criado_em` timestamp,
  `contato_id` integer NOT NULL,
  `profissional_id` integer NOT NULL,
  `data` datetime NOT NULL,
  `duracao` integer NOT NULL,
  `observacao` varchar(255) DEFAULT null
);

ALTER TABLE `agendamentos` ADD FOREIGN KEY (`contato_id`) REFERENCES `contato` (`id`);

ALTER TABLE `agendamentos` ADD FOREIGN KEY (`profissional_id`) REFERENCES `profissional` (`id`);
