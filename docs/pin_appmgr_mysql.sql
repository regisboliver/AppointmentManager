CREATE TABLE `contato` (
  `id` char(32) PRIMARY KEY DEFAULT (UUID()),
  `criado_em` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `modificado_em` timestamp DEFAULT null,
  `nome` varchar(50) UNIQUE NOT NULL,
  `email` varchar(50) UNIQUE NOT NULL,
  `telefone` varchar(20) UNIQUE NOT NULL,
  `documento` varchar(14) UNIQUE NOT NULL,
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
  `id` char(32) PRIMARY KEY DEFAULT (UUID()),
  `criado_em` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `modificado_em` timestamp DEFAULT null,
  `nome` varchar(50) UNIQUE NOT NULL,
  `registro` integer UNIQUE NOT NULL,
  `sala` varchar(20) NOT NULL,
  `especialidade` varchar(20) NOT NULL,
  `indisponibilidade` varchar(20)
);

CREATE TABLE `agendamentos` (
  `id` char(32) PRIMARY KEY DEFAULT (UUID()),
  `criado_em` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `modificado_em` timestamp DEFAULT null,
  `contato_id` char(32) NOT NULL,
  `profissional_id` char(32) NOT NULL,
  `data` datetime NOT NULL,
  `duracao` integer NOT NULL,
  `observacao` varchar(255) DEFAULT null
);

ALTER TABLE `agendamentos` ADD FOREIGN KEY (`contato_id`) REFERENCES `contato` (`id`);

ALTER TABLE `agendamentos` ADD FOREIGN KEY (`profissional_id`) REFERENCES `profissional` (`id`);
